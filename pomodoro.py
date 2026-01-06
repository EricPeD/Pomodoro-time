# pomodoro.py
# Un temporizador Pomodoro personal

import argparse
import time
import sys
from plyer import notification
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.rule import Rule
from rich.progress import Progress, TextColumn, BarColumn, TimeRemainingColumn
import threading
from pynput import keyboard

# Global state for the timer
timer_state = {
    "paused": False,
    "skipped": False,
}

def on_press(key):
    """Handles key presses."""
    global timer_state
    try:
        if key.char == 'p':
            timer_state["paused"] = not timer_state["paused"]
        elif key.char == 's':
            timer_state["skipped"] = True
    except AttributeError:
        pass # Ignore special keys

def input_listener():
    """Starts listening for keyboard input."""
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Pomodoro Timer",
        timeout=10 # Notification will disappear after 10 seconds
    )

def countdown_timer(minutes, session_name, state):
    total_seconds = minutes * 60
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TimeRemainingColumn(),
        console=Console(),
    ) as progress:
        task = progress.add_task(f"[bold]{session_name}[/bold]", total=total_seconds)
        
        is_task_paused = False
        while not progress.finished:
            if state["skipped"]:
                progress.update(task, completed=total_seconds)
                break

            # If the state is paused but the task is not, stop the task
            if state["paused"] and not is_task_paused:
                progress.stop_task(task)
                is_task_paused = True
            
            # If the state is not paused but the task is, start the task
            elif not state["paused"] and is_task_paused:
                progress.start_task(task)
                is_task_paused = False

            if is_task_paused:
                time.sleep(0.1) # Prevent busy-waiting
                continue

            progress.update(task, advance=1)
            time.sleep(1)
    
    # Reset state for the next run
    state["skipped"] = False
    state["paused"] = False

def main():
    parser = argparse.ArgumentParser(description="Un temporizador Pomodoro personalizable.")
    parser.add_argument("--work", type=int, default=25,
                        help="Duración de la sesión de trabajo en minutos (por defecto: 25).")
    parser.add_argument("--short-break", type=int, default=5,
                        help="Duración del descanso corto en minutos (por defecto: 5).")
    parser.add_argument("--long-break", type=int, default=15,
                        help="Duración del descanso largo en minutos (por defecto: 15).")
    parser.add_argument("--rounds", type=int, default=4,
                        help="Número de sesiones de trabajo antes de un descanso largo (por defecto: 4).")
    
    args = parser.parse_args()

    # Initialize rich console
    console = Console()
    console.print("\n")
    console.print(Panel(Text("--- Configuración del Pomodoro ---", justify="center", style="bold yellow"), title="[bold green]Pomodoro Timer[/bold green]"))
    console.print(f"  [cyan]Sesión de trabajo:[/cyan] [bold]{args.work}[/bold] minutos")
    console.print(f"  [blue]Descanso corto:[/blue] [bold]{args.short_break}[/bold] minutos")
    console.print(f"  [purple]Descanso largo:[/purple] [bold]{args.long_break}[/bold] minutos")
    console.print(f"  [magenta]Rondas antes de descanso largo:[/magenta] [bold]{args.rounds}[/bold]\n")

    # Start the keyboard listener in a separate thread
    listener_thread = threading.Thread(target=input_listener, daemon=True)
    listener_thread.start()
    
    console.print(Panel(Text("Pulsa 'p' para pausar/reanudar, 's' para saltar.", justify="center"), style="yellow"))
    console.print()

    work_sessions_completed = 0

    while True:
        work_sessions_completed += 1
        console.print(Rule(f"[bold white]Ronda {work_sessions_completed} de {args.rounds}[/bold white]", style="bold bright_white"))
        send_notification("¡A trabajar!", f"Comienza tu sesión de trabajo de {args.work} minutos.")
        countdown_timer(args.work, "TRABAJO", timer_state)
        send_notification("¡Descanso!", "Sesión de trabajo terminada.")

        if work_sessions_completed % args.rounds == 0:
            console.print(Rule(f"[bold green]Descanso Largo ({args.long_break} minutos)[/bold green]", style="bold green"))
            send_notification("¡Descanso Largo!", f"Tómate un descanso largo de {args.long_break} minutos.")
            countdown_timer(args.long_break, "DESCANSO LARGO", timer_state)
            send_notification("¡De vuelta al trabajo!", "Descanso largo terminado.")
            work_sessions_completed = 0 # Reset for next set of rounds
        else:
            console.print(Rule(f"[bold blue]Descanso Corto ({args.short_break} minutos)[/bold blue]", style="bold blue"))
            send_notification("¡Descanso Corto!", f"Tómate un descanso corto de {args.short_break} minutos.")
            countdown_timer(args.short_break, "DESCANSO CORTO", timer_state)
            send_notification("¡De vuelta al trabajo!", "Descanso corto terminado.")
        console.print(Rule(style="bold white"))


if __name__ == "__main__":
    main()

# pomodoro.py
# Un temporizador Pomodoro personal

import argparse
import time
import sys
from plyer import notification

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Pomodoro Timer",
        timeout=10 # Notification will disappear after 10 seconds
    )

def countdown_timer(minutes, session_name):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{session_name}: {mins:02d}:{secs:02d}"
        sys.stdout.write(timer + '\r')
        sys.stdout.flush()
        time.sleep(1)
        seconds -= 1
    sys.stdout.write(' ' * len(timer) + '\r') # Clear the line
    sys.stdout.flush()

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

    args = parser.parse_args()

    print(f"--- Configuración del Pomodoro ---")
    print(f"  Sesión de trabajo: {args.work} minutos")
    print(f"  Descanso corto: {args.short_break} minutos")
    print(f"  Descanso largo: {args.long_break} minutos")
    print(f"  Rondas antes de descanso largo: {args.rounds}\n")

    work_sessions_completed = 0

    while True:
        work_sessions_completed += 1
        print(f"--- Ronda {work_sessions_completed} de {args.rounds} ---")
        send_notification("¡A trabajar!", f"Comienza tu sesión de trabajo de {args.work} minutos.")
        countdown_timer(args.work, "TRABAJO")
        send_notification("¡Descanso!", "Sesión de trabajo terminada.")

        if work_sessions_completed % args.rounds == 0:
            print(f"--- Descanso Largo ({args.long_break} minutos) ---")
            send_notification("¡Descanso Largo!", f"Tómate un descanso largo de {args.long_break} minutos.")
            countdown_timer(args.long_break, "DESCANSO LARGO")
            send_notification("¡De vuelta al trabajo!", "Descanso largo terminado.")
            work_sessions_completed = 0 # Reset for next set of rounds
        else:
            print(f"--- Descanso Corto ({args.short_break} minutos) ---")
            send_notification("¡Descanso Corto!", f"Tómate un descanso corto de {args.short_break} minutos.")
            countdown_timer(args.short_break, "DESCANSO CORTO")
            send_notification("¡De vuelta al trabajo!", "Descanso corto terminado.")
        print("-" * 30)


if __name__ == "__main__":
    main()

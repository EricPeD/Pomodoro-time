# Pomodoro-time 🍅

Un temporizador Pomodoro personalizable, simple y eficaz para tu terminal. Creado con Python, este proyecto busca ser tanto una herramienta práctica para el día a día como un campo de pruebas para el aprendizaje y la implementación de nuevas tecnologías.

![test]([https://i.imgur.com/example.gif](https://media.discordapp.net/attachments/1257517677895749665/1458064771034120202/image.png?ex=695e4822&is=695cf6a2&hm=06a008ba37e27b2cd01f9171cfafae54e11cfb232cfdef52950b6b285065925e&=&format=webp&quality=lossless)) <!-- ¡Esto es un placeholder! Puedes crear un GIF de la terminal funcionando y reemplazar el link -->

---

## ✨ Características Actuales

-   **Temporizador Personalizable:** Define la duración de tus sesiones de trabajo, descansos cortos y descansos largos directamente desde la línea de comandos.
-   **Notificaciones de Escritorio:** Recibe alertas visuales al inicio y final de cada sesión.
-   **Contador Dinámico:** Visualiza el tiempo restante directamente en tu terminal, actualizándose cada segundo sin saturar la pantalla.
-   **Ciclos Configurables:** Decide cuántas sesiones de trabajo completas un ciclo antes de un descanso largo.

---

## 🚀 Instalación y Uso

### Prerrequisitos

-   Python 3.8+
-   `pip`

### Pasos

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/EricPeD/Pomodoro-time.git
    cd Pomodoro-time
    ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    # Para Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

### Ejecución

-   **Para iniciar con la configuración por defecto (25/5/15 min):**
    ```bash
    python pomodoro.py
    ```

-   **Para personalizar la duración:**
    ```bash
    python pomodoro.py --work 30 --short-break 5 --long-break 20 --rounds 4
    ```

#### Argumentos Disponibles:
| Argumento       | Descripción                                               | Por Defecto |
|-----------------|-----------------------------------------------------------|-------------|
| `--work`        | Duración de la sesión de trabajo en minutos.              | 25          |
| `--short-break` | Duración del descanso corto en minutos.                   | 5           |
| `--long-break`  | Duración del descanso largo en minutos.                   | 15          |
| `--rounds`      | Nº de sesiones de trabajo antes de un descanso largo.     | 4           |

---

## 🗺️ Roadmap del Proyecto

Este proyecto está en desarrollo activo con una visión clara para el futuro. ¡Tu feedback o contribuciones son bienvenidas!

-   **Fase 1: TUI e Interactividad**
    -   Implementar una interfaz de usuario en terminal (TUI) con `rich`.
    -   Añadir una barra de progreso visual.
    -   Incorporar interactividad para **pausar, saltar y reiniciar** sesiones.

-   **Fase 2: Persistencia y Configuración**
    -   Guardar preferencias en un archivo `config.toml`.
    -   Almacenar el historial de sesiones en una base de datos `SQLite`.
    -   Permitir reanudar el ciclo Pomodoro si la aplicación se cierra.

-   **Fase 3: Funcionalidades Adicionales y Empaquetado**
    -   Añadir alertas de sonido.
    -   Crear un comando para visualizar estadísticas de uso.
    -   Empaquetar la aplicación para que sea fácilmente instalable con `pip`.

---

Hecho con ❤️ y Python.

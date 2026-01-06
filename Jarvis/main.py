# main.py
from wake import wait_for_wake_word
from speech import speak, listen
from commands import handle_command
import time
from ai import ask_ai
import commands
print("USING commands.py FROM:", commands.__file__)


def handle_command(command: str):
    """
    Temporary command handler.
    Replace this later with real command routing.
    """
    if not command:
        speak("I did not catch that.")
        return

    command = command.lower()

    if command in {"exit", "quit", "stop"}:
        speak("Goodbye.")
        exit(0)

    # Placeholder behavior
    speak(f"You said {command}")

def main():
    speak("Assistant initialized. Waiting for wake word.")

    while True:
        # 1. Sleep until wake word
        wait_for_wake_word()

        # 2. Acknowledge
        speak("Yes?")

        # 3. Listen for command
        command = listen(duration=5)

        # 4. Handle command
        handled = handle_command(command, speak)

        if not handled:
            response = ask_ai(command)
            speak(response)

        # 5. Short pause before re-entering wake mode
        time.sleep(0.5)

if __name__ == "__main__":
    main()

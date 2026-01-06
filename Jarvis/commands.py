import webbrowser
import datetime
import sys

def handle_command(command: str, speak):
    if not command:
        return True

    if command in {"exit", "quit", "stop"}:
        speak("Goodbye.")
        sys.exit(0)

    if "time" in command:
        speak(datetime.datetime.now().strftime("%I:%M %p"))
        return True

    if "date" in command:
        speak(datetime.date.today().strftime("%B %d, %Y"))
        return True

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")
        return True

    return False

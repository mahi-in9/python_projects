# commands.py
import webbrowser
import datetime
import os
import sys

def handle_command(command: str, speak):
    if not command:
        speak("I did not hear any command.")
        return True

    command = command.lower().strip()

    # EXIT
    if command in {"exit", "quit", "stop"}:
        speak("Goodbye.")
        sys.exit(0)

    # TIME
    if "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")
        return True

    # DATE
    if "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today is {today}")
        return True

    # OPEN WEBSITES
    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")
        return True

    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
        return True

    if "open github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")
        return True

    return False

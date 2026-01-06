from speech import speak, listen
from commands import handle_command
from ai import ask_ai
from dialog import DialogMemory
import time

memory = DialogMemory(max_turns=4)

def main():
    speak("Assistant ready.")

    while True:
        command = listen(duration=3)

        if not command:
            time.sleep(0.15)
            continue

        command = command.strip().lower()
        print("Heard:", command)

        memory.add_user(command)

        handled = handle_command(command, speak)

        if not handled:
            response = ask_ai(command, context=memory.context())
            speak(response)
            memory.add_assistant(response)

        time.sleep(0.6)  # echo protection

if __name__ == "__main__":
    main()

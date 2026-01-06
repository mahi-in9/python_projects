# wake.py
import speech_recognition as sr

WAKE_WORD = "jiya"
recognizer = sr.Recognizer()

def wait_for_wake_word():
    print("Wake listener started (Google Mic)...")

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        while True:
            try:
                print("Listening for wake word...")
                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=3
                )

                text = recognizer.recognize_google(audio).lower().strip()
                print("Heard (wake check):", text)

                if WAKE_WORD in text.split():
                    print("Wake word detected!")
                    return

            except sr.WaitTimeoutError:
                continue
            except sr.UnknownValueError:
                continue
            except sr.RequestError as e:
                print("Wake API error:", e)
                return

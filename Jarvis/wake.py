# wake.py
import speech_recognition as sr
import time

WAKE_WORD = "jarvis"

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
                    timeout=3,
                    phrase_time_limit=3
                )

                text = recognizer.recognize_google(audio)
                text = text.lower().strip()

                print("Heard (wake check):", text)

                # STRICT wake word check (no substring bugs)
                words = text.split()
                if WAKE_WORD in words:
                    print("Wake word detected!")
                    return True

            except sr.WaitTimeoutError:
                continue
            except sr.UnknownValueError:
                continue
            except sr.RequestError as e:
                print("Wake API error:", e)
                time.sleep(1)

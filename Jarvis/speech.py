# speech.py
from gtts import gTTS
import pygame
import os
import time
import wave
import sounddevice as sd
import numpy as np
import tempfile
import speech_recognition as sr

pygame.mixer.init()
recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True

def speak(text: str):
    filename = "temp.mp3"
    gTTS(text=text).save(filename)

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.music.unload()
    os.remove(filename)

def listen(duration=5, samplerate=16000):
    try:
        print("Listening...")
        audio = sd.rec(
            int(duration * samplerate),
            samplerate=samplerate,
            channels=1,
            dtype=np.int16
        )
        sd.wait()

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            with wave.open(f.name, "wb") as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)
                wf.setframerate(samplerate)
                wf.writeframes(audio.tobytes())

        with sr.AudioFile(f.name) as source:
            audio_data = recognizer.record(source)

        text = recognizer.recognize_google(audio_data)
        return text

    except Exception as e:
        print("Listen error:", e)
        return None
    finally:
        if 'f' in locals():
            os.remove(f.name)

from gtts import gTTS
import pygame
import os
import time
import wave
import sounddevice as sd
import numpy as np
import tempfile
import speech_recognition as sr

# ===== AUDIO CONFIG (CRITICAL) =====
MIC_INDEX = 9  # Realtek Microphone (WASAPI)

sd.default.device = (MIC_INDEX, None)

device_info = sd.query_devices(MIC_INDEX, "input")
NATIVE_RATE = int(device_info["default_samplerate"])
CHANNELS = int(device_info["max_input_channels"])
# =================================

pygame.mixer.init()

recognizer = sr.Recognizer()
recognizer.energy_threshold = 250
recognizer.dynamic_energy_threshold = True

def speak(text: str):
    filename = "temp.mp3"
    gTTS(text=text, lang="en").save(filename)

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.05)

    pygame.mixer.music.unload()
    os.remove(filename)

def listen(duration=3):
    try:
        # Record using native channel count
        audio = sd.rec(
            int(duration * NATIVE_RATE),
            samplerate=NATIVE_RATE,
            channels=CHANNELS,
            dtype=np.int16
        )
        sd.wait()

        # Down-mix to mono (average channels)
        if CHANNELS > 1:
            audio = np.mean(audio, axis=1, dtype=np.int16)

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            with wave.open(f.name, "wb") as wf:
                wf.setnchannels(1)          # mono for STT
                wf.setsampwidth(2)          # int16
                wf.setframerate(NATIVE_RATE)
                wf.writeframes(audio.tobytes())

        with sr.AudioFile(f.name) as source:
            audio_data = recognizer.record(source)

        return recognizer.recognize_google(audio_data)

    except Exception as e:
        print("Listen error:", e)
        return None
    finally:
        if "f" in locals():
            os.remove(f.name)

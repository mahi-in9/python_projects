from speech import speak, listen

print("Testing speech output...")
speak("Speech output is working")

print("Testing microphone input...")
text = listen(duration=5)

if text:
    print("You said:", text)
    speak(f"You said {text}")
else:
    print("No speech detected")
    speak("I did not hear anything")

from wake import wait_for_wake_word
from speech import speak

speak("Wake word test started. Say Jarvis.")

wait_for_wake_word()

speak("Yes? I am listening.")

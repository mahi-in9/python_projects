from collections import deque

class DialogMemory:
    def __init__(self, max_turns=6):
        self.history = deque(maxlen=max_turns)

    def add_user(self, text: str):
        self.history.append({"role": "user", "text": text})

    def add_assistant(self, text: str):
        self.history.append({"role": "assistant", "text": text})

    def context(self) -> str:
        return "\n".join(
            f"{'User' if h['role']=='user' else 'Assistant'}: {h['text']}"
            for h in self.history
        )

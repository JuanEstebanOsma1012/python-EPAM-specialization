class Dictionary:
    def __init__(self, entries=None):
        self.entries = entries if entries is not None else {}

    def newentry(self, word, definition):
        self.entries[word] = definition

    def look(self, word):
        return self.entries.get(word, f"Can' find entry for {word}")
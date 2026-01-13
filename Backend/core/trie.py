class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.concept = None
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, phrase: str):
        node = self.root
        words = phrase.lower().split()
        for word in words:
            if word not in node.children:
                node.children[word] = TrieNode()
            node = node.children[word]
        node.is_end = True
        node.concept = phrase

    def detect(self, text: str):
        words = text.lower().split()
        found = set()
        for i in range(len(words)):
            node = self.root
            j = i
            while j < len(words) and words[j] in node.children:
                node = node.children[words[j]]
                if node.is_end:
                    found.add(node.concept)
                j += 1
        return found

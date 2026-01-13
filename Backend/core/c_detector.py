from core.trie import Trie
class ConceptDetector:
    def __init__(self, concepts):
        self.trie = Trie()
        for concept in concepts:
            self.trie.insert(concept)

    def detect_concepts(self, answer: str):
        return self.trie.detect(answer)
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.end_word = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if len(word) <= 0:
            return

        node = self.root
        for s in word:
            if s not in node.children:
                node.children[s] = TrieNode()

            node = node.children[s]
        node.end_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if len(word) <= 0:
            return False

        node = self.root
        for s in word:
            if s in node.children:
                node = node.children[s]
            else:
                return False
        return node.end_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if len(prefix) <= 0:
            return False

        node = self.root
        for s in prefix:
            if s in node.children:
                node = node.children[s]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("somestring")
print(trie.search("key"))
print(trie.search("somestring"))

# Trie Delete Operation... 

class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store children nodes
        self.isEndOfWord = False  # Flag to mark end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()  # Initialize root node

    def insert(self, word):
        current = self.root
        # Traverse through each character in the word
        for char in word:
            # If the character is not in the children, add it
            if char not in current.children:
                current.children[char] = TrieNode()
            # Move to the next node
            current = current.children[char]
        # Mark the end of the word
        current.isEndOfWord = True

    def isEmpty(self, node):
        # Check if the node has no children
        return len(node.children) == 0

    def remove(self, node, key, depth=0):
        if not node:
            return None

        # If reached the end of the key
        if depth == len(key):
            # Unmark the end of word if it's marked
            if node.isEndOfWord:
                node.isEndOfWord = False
            # If the node has no children and not marking the end of any word, delete it
            if self.isEmpty(node) and not node.isEndOfWord:
                del node
                node = None
            return node

        # Get the character at the current depth
        char = key[depth]
        # Recursively call remove on the next character in the key
        node.children[char] = self.remove(node.children[char], key, depth + 1)

        # If the node has no children and not marking the end of any word, delete it
        if self.isEmpty(node) and not node.isEndOfWord:
            del node
            node = None

        return node

    def delete(self, key):
        # Call remove starting from the root
        self.root = self.remove(self.root, key)


# Main function
if __name__ == "__main__":
    trie = Trie()

    # Insert some words
    trie.insert("apple")
    trie.insert("banana")
    trie.insert("app")
    trie.insert("hello")

    # Delete a word
    trie.delete("apple")

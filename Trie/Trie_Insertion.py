# Trie Insert Operation... 

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

    def printTrie(self, node, indent=""):
        # Function to print Trie structure recursively
        if node is None:
            return

        for char, child in node.children.items():
            print(indent + "|--" + char)
            self.printTrie(child, indent + "   ")

        if node.isEndOfWord:
            print(indent + "|--(end)")

    def print(self):
        # Function to initiate Trie printing
        print("Trie Structure:")
        self.printTrie(self.root)


# Main function
if __name__ == "__main__":
    trie = Trie()

    # Insert some words
    trie.insert("apple")
    trie.insert("banana")
    trie.insert("app")
    trie.insert("hello")

    # Print the Trie structure
    trie.print()

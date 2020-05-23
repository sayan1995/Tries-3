'''
Time Complexity: O(m) -> m is the number of queries
Space Complexity: O(n*k) -> n is number of words and k is the length of  word
Did this code successfully run on Leetcode : Yes
Explanation:
Create a trie of the input words in the opposite order and have a flag isWord for the end character of every word in the
trie Now when querying save the query character in a buffer array or string and for every query check if the character
of all the previous query character + the query character are in the trie in the reverse order, if yes return True.
Eg.
i/p - [ab]
Tire is b->a
q1-> a
q2->b
buffer at time b is ab
now start from back of buffer ie check if b is in trie -> it is in trie go to child of b that is a
now check if a is in trie -> yes and then check if isWord = True , answer is yes return True
'''


class Trie:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.isWord = None


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = Trie()
        # save all input characters in buffer
        self.buffer = []
        # construct Trie
        self.construct(words)

    def query(self, letter: str) -> bool:
        # Insert the element in the buffer
        self.buffer.append(letter)
        cursor = self.root

        for i in range(len(self.buffer) - 1, -1, -1):
            ch = self.buffer[i]
            if cursor.children[ord(ch) - ord('a')] == None:
                return False
            cursor = cursor.children[ord(ch) - ord('a')]
            if cursor.isWord:
                return True

        return False

    def construct(self, words):
        for word in words:
            cursor = self.root
            for i in range(len(word) - 1, -1, -1):
                ch = word[i]
                if cursor.children[ord(ch) - ord('a')] == None:
                    cursor.children[ord(ch) - ord('a')] = Trie()
                cursor = cursor.children[ord(ch) - ord('a')]

            cursor.isWord = True

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
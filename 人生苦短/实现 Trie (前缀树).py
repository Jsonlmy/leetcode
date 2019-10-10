'''
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");   
trie.search("app");     // 返回 true
说明:

你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。

链接：https://leetcode-cn.com/problems/implement-trie-prefix-tree
'''
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}
        self.end = False
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tr = self
        for c in word:
            if c not in tr.lookup: tr.lookup[c] = Trie()
            tr = tr.lookup[c]
        tr.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tr = self
        for c in word:
            if c not in tr.lookup: return False
            tr = tr.lookup[c]        
        return tr.end
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tr = self
        for c in prefix:
            if c not in tr.lookup: return False
            tr = tr.lookup[c]
        return True

    

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
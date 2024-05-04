class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._insert_recursive(key, value, self.root)
    
    def _insert_recursive(self, key, value, current_node):
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key, value)
            else:
                self._insert_recursive(key, value, current_node.left)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key, value)
            else:
                self._insert_recursive(key, value, current_node.right)
        else:
            raise ValueError("Key already exists in tree")
        
    def search(self, key):
        return self._search_recursive(key, self.root)
    
    def _search_recursive(self, key, current_node):
        if current_node is None:
            return None
        if key == current_node.key:
            return current_node.value
        elif key< current_node.key:
            return self._search_recursive(key, current_node.left)
        else:
            return self._search_recursive(key, current_node.right)
        

binary_tree = BinaryTree()

# Insert nodes with keys and values
binary_tree.insert(5, "Five")
binary_tree.insert(3, "Three")
binary_tree.insert(7, "Seven")
binary_tree.insert(2, "Two")
binary_tree.insert(4, "Four")
binary_tree.insert(6, "Six")
binary_tree.insert(8, "Eight")

# Query for values of keys
print(binary_tree.search(3))  # Output: "Three"
print(binary_tree.search(7))  # Output: "Seven"
print(binary_tree.search(4))  # Output: "Four"
print(binary_tree.search(9))  # Output: None (key not found)
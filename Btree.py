class Node:
    def __init__(self, key, value, position=None, is_root=False, is_left_child=False, is_right_child=False):
        self.key = key
        self.value = value
        self.position = position
        self.is_root = is_root
        self.is_left_child = is_left_child
        self.is_right_child = is_right_child
        self.left = None
        self.right = None

    def __str__(self):
        node_type = ""
        if self.is_root:
            node_type = "Root Node"
        elif self.is_left_child:
            node_type = "Left Child"
        elif self.is_right_child:
            node_type = "Right Child"
        if self.position is not None:
            return f"{node_type} - Position: {self.position}, Key: {self.key}, Value: {self.value}"
        return f"{node_type} - Key: {self.key}, Value: {self.value}"

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        key = int(key)
        if self.root is None:
            self.root = Node(key, value, position=1, is_root=True)
        else:
            self._insert_recursive(key, value, self.root, position=1)
    
    def _insert_recursive(self, key, value, current_node, position):
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key, value, position=2 * position, is_left_child=True)
            else:
                self._insert_recursive(key, value, current_node.left, 2 * position)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key, value, position=2 * position + 1, is_right_child=True)
            else:
                self._insert_recursive(key, value, current_node.right, 2 * position + 1)
        else:
            raise ValueError("Key already exists in tree")
        
    def search(self, key):
        key = int(key)
        return self._search_recursive(key, self.root)
    
    def _search_recursive(self, key, current_node):
        if current_node is None:
            return None
        if key == current_node.key:
            return current_node.value, current_node, current_node.position, current_node.is_left_child, current_node.is_right_child
        elif key < current_node.key:
            return self._search_recursive(key, current_node.left)
        else:
            return self._search_recursive(key, current_node.right)
        
# Create an instance of BinaryTree
binary_tree = BinaryTree()

# Input Loop
while True:
    # Get user Input for key(string)
    key = input("Enter an integer key to insert into the binary tree or q to quit: ")
    if key.lower() == 'q':
        break

    # Get user input for value (string)
    value = input("Enter a value (string) for the key: ")

    # Insert the key-value pair into the binary tree
    binary_tree.insert(key, value)

# Query loop
while True:
    # Get user input for key to search
    search_key = input("Enter an integer key to search for its value or q to quit: ")
    if search_key.lower() == 'q':
        break

    # Search for the key in the binary tree
    result = binary_tree.search(search_key)
    if result is None:
        print("Key not found")
    else:
        print(f"Value: {result[0]}")
        print(f"Node: {result[1]}")

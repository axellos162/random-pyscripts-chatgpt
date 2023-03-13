# Define a class for Binary Search Tree Node
class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# Define a class for Binary Search Tree
class BST:
    def __init__(self):
        self.root = None

    # Insert a node into the tree
    def insert(self, data):
        if not self.root:
            self.root = BSTNode(data)
            return

        current = self.root
        while True:
            if data < current.data:
                if current.left:
                    current = current.left
                else:
                    current.left = BSTNode(data)
                    break
            elif data > current.data:
                if current.right:
                    current = current.right
                else:
                    current.right = BSTNode(data)
                    break
            else:
                break

    # Print the tree in inorder traversal
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=' ')
            self.inorder_traversal(node.right)

    # Check if the BST is balanced
    def is_balanced(self, node):
        if not node:
            return True

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        if abs(left_height - right_height) > 1:
            return False

        return self.is_balanced(node.left) and self.is_balanced(node.right)

    # Calculate the height of the tree
    def height(self, node):
        if not node:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    # Insert a list of numbers into the tree
    def insert_list(self, numbers):
        for number in numbers:
            self.insert(number)



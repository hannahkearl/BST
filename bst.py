class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def in_order_traversal(self):
        result = []
        self._in_order_traversal_recursive(self.root, result)
        return result

    def _in_order_traversal_recursive(self, node, result):
        if node:
            self._in_order_traversal_recursive(node.left, result)
            result.append(node.value)
            self._in_order_traversal_recursive(node.right, result)

    def find_min(self):
        if not self.root:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.value

    def find_max(self):
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.value

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return -1
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return 1 + max(left_height, right_height)

    def count_leaves(self):
        return self._count_leaves_recursive(self.root)

    def _count_leaves_recursive(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self._count_leaves_recursive(node.left) + self._count_leaves_recursive(node.right)

    def serialize(self):
        return self._serialize_recursive(self.root)

    def _serialize_recursive(self, node):
        if node is None:
            return '#'
        return str(node.value) + ',' + self._serialize_recursive(node.left) + ',' + self._serialize_recursive(node.right)

    def deserialize(self, tree):
        values = tree.split(',')
        self.root = self._deserialize_recursive(values)

    def _deserialize_recursive(self, values):
        if values[0] == '#':
            values.pop(0)
            return None
        root = TreeNode(int(values.pop(0)))
        root.left = self._deserialize_recursive(values)
        root.right = self._deserialize_recursive(values)
        return root

# Example usage:
bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(17)

print(bst.search(7))  # Output: True
print(bst.in_order_traversal())  # Output: [3, 5, 7, 10, 12, 15, 17]
print(bst.find_min())  # Output: 3
print(bst.find_max())  # Output: 17
print(bst.height())  # Output: 2
print(bst.count_leaves())  # Output: 4
serialized_tree = bst.serialize()
print(serialized_tree)  # Output: "10,5,3,#,#,7,#,#,15,12,#,#,17,#,#"
bst.deserialize(serialized_tree)
print(bst.in_order_traversal())  # Output: [3, 5, 7, 10, 12, 15, 17]


class TreeNode:
    def _init_(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, key_value):
        if key_value < self.value:
            if self.left is None:
                self.left = TreeNode(key_value)
            else:
                self.left.insert(key_value)
        else:
            if self.right is None:
                self.right = TreeNode(key_value)
            else:
                self.right.insert(key_value)

    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print(self.value)
        if self.right:
            self.right.in_order_traversal()

    def pre_order_traversal(self):
        print(self.value)
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()

    def post_order_traversal(self):
        if self.left:
            self.left.post_order_traversal()
        if self.right:
            self.right.post_order_traversal()
        print(self.value)

    def find(self, key):
        if key < self.value:
            return self.left.find(key) if self.left else False
        elif key > self.value:
            return self.right.find(key) if self.right else False
        else:
            return True


# 🔥 Driver Code
if __name__== '_main_':
    # Use integers instead of strings
    tree = TreeNode(10)
    tree.insert(5)
    tree.insert(4)
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(22)
    tree.insert(11)
    tree.insert(12)
    tree.insert(13)

    print("In-order Traversal:")
    tree.in_order_traversal()
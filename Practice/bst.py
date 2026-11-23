# BST using Linked List

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.cnt = 0

    def insert(self, new_node):
        self.cnt += 1

        if self.root is None:
            self.root = new_node
            return

        temp = self.root

        while True:
            if new_node.data < temp.data:      # Left subtree
                if temp.left is None:
                    temp.left = new_node
                    return
                temp = temp.left

            else:                             # Right subtree
                if temp.right is None:
                    temp.right = new_node
                    return
                temp = temp.right

    def inorder(self, rt):
        if rt:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            self.inorder(rt.right)

    def preorder(self, rt):
        if rt:
            print(rt.data, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)

    def postorder(self, rt):
        if rt:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data, end=" ")

    def find_min_max(self):
        if self.root is None:
            print("Tree is empty")
            return

        temp = self.root
        while temp.left:
            temp = temp.left
        print("\nMin:", temp.data)

        temp = self.root
        while temp.right:
            temp = temp.right
        print("Max:", temp.data)


# Driver Code
b1 = BST()

b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(0))
b1.insert(Node(65))
b1.insert(Node(300))

print("Inorder:")
b1.inorder(b1.root)

print("\n\nPreorder:")
b1.preorder(b1.root)

print("\n\nPostorder:")
b1.postorder(b1.root)

print("\n\nNo of Nodes:", b1.cnt)

b1.find_min_max()
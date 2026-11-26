from colle













ctions import deque



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):

    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


def level_order(root):

    if root is None:
        return

    q = deque()
    q.append(root)

    while q:

        size = len(q)

        for i in range(size):

            curr = q.popleft()

            print(curr.data, end=" ")

            if curr.left:
                q.append(curr.left)

            if curr.right:
                q.append(curr.right)

        print()


# Driver Code
root = None

arr = [100, 50, 150, 25, 75, 125, 175]

for x in arr:
    root = insert(root, x)

print("Level Order Traversal:")
level_order(root)
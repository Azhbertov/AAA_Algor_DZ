class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)

    current = root
    while True:
        if key == current.key:
            return root

        if key < current.key:
            if current.left is None:
                current.left = Node(key)
                return root
            current = current.left
        else:
            if current.right is None:
                current.right = Node(key)
                return root
            current = current.right


def tree_to_list(root, tree_list):
    if root is None:
        return
    tree_list.append(root.key)
    tree_to_list(root.left, tree_list)
    tree_to_list(root.right, tree_list)


def rotate_left(x):
    y = x.right
    assert y is not None
    x.right = y.left
    y.left = x
    return y


def rotate_right(y):
    x = y.left
    assert x is not None
    y.left = x.right
    x.right = y
    return x


def rotate(root, key, direction):
    if key < root.key:
        root.left = rotate(root.left, key, direction)
        return root
    if key > root.key:
        root.right = rotate(root.right, key, direction)
        return root

    if direction == 'left':
        return rotate_left(root)
    return rotate_right(root)


root = None
N = int(input())
keys = list(map(int, input().split()))
M = int(input())

for key in keys:
    root = insert(root, key)

for _ in range(M):
    command = input().split()
    root = rotate(root, int(command[1]), command[0])
    tree_list = []
    tree_to_list(root, tree_list)
    print(*tree_list)

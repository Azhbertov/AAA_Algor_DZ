# https://contest.yandex.ru/contest/100803/run-report/168484678/
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def tree_to_list(root, tree_list):
    if root is None:
        return
    tree_list.append(root.key)
    tree_to_list(root.left, tree_list)
    tree_to_list(root.right, tree_list)


def height(root):
    return 0 if root is None else root.height

def update(root):
    root.height = 1 + max(height(root.left), height(root.right))


def balance_factor(node):
    return height(node.left) - height(node.right)

def find_min(root):
    if root is None:
        return None

    current = root
    while current.left is not None:
        current = current.left
    return current


def rotate_left(x):
    y = x.right
    assert y is not None
    x.right = y.left
    y.left = x
    update(x)
    update(y)
    return y


def rotate_right(y):
    x = y.left
    assert x is not None
    y.left = x.right
    x.right = y
    update(y)
    update(x)
    return x


def insert(root, key):
    if root is None:
        return Node(key)

    if key == root.key:
        return root

    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    update(root)
    bf = balance_factor(root)

    if bf > 1 and key < root.left.key:
        return rotate_right(root)
    if bf < -1 and key > root.right.key:
        return rotate_left(root)
    if bf > 1 and key > root.left.key:
        root.left = rotate_left(root.left)
        return rotate_right(root)
    if bf < -1 and key < root.right.key:
        root.right = rotate_right(root.right)
        return rotate_left(root)
    return root


def search(root, key):
    current = root
    while current is not None:
        if key == current.key:
            return current
        if key < current.key:
            current = current.left
        else:
            current = current.right
    return None


def balance_check(root):
    update(root)
    bf = balance_factor(root)

    if bf > 1 and balance_factor(root.left) >= 0:
        return rotate_right(root)
    if bf < -1 and balance_factor(root.right) <= 0:
        return rotate_left(root)
    if bf > 1 and balance_factor(root.left) < 0:
        root.left = rotate_left(root.left)
        return rotate_right(root)
    if bf < -1 and balance_factor(root.right) > 0:
        root.right = rotate_right(root.right)
        return rotate_left(root)
    return root


def delete_node(root, key):
    if root is None:
        return None

    if key < root.key:
        root.left = delete_node(root.left, key)
        return balance_check(root)
    if key > root.key:
        root.right = delete_node(root.right, key)
        return balance_check(root)

    if root.left is None and root.right is None:
        return None
    if root.left is None:
        return root.right
    if root.right is None:
        return root.left

    succ = find_min(root.right)
    assert succ is not None
    root.key = succ.key
    root.right = delete_node(root.right, succ.key)
    return balance_check(root)


def successor(root, key):
    current = root
    succ = None
    while current is not None:
        if key < current.key:
            succ = current
            current = current.left
        elif key > current.key:
            current = current.right
        else:
            return current
    return succ


def left_successor(root, key):
    current = root
    left_succ = None
    while current is not None:
        if key > current.key:
            left_succ = current
            current = current.right
        elif key < current.key:
            current = current.left
        else:
            return current
    return left_succ


root = None
Q = int(input())

for _ in range(Q):
    command = input().split()

    if command[0] == 'add':
        root = insert(root, int(command[1]))
    elif command[0] == 'del':
        root = delete_node(root, int(command[1]))
    elif command[0] == 'exists':
        if search(root, int(command[1])):
            print('YES')
        else:
            print('NO')
    elif command[0] == 'next':
        succ = successor(root, int(command[1]))
        if succ is None:
            print('None')
        else:
            print(succ.key)
    elif command[0] == 'prev':
        left_succ = left_successor(root, int(command[1]))
        if left_succ is None:
            print('None')
        else:
            print(left_succ.key)
    elif command[0] == 'root':
        if root is None:
            print('Empty')
        else:
            print(root.key)
    elif command[0] == 'height':
        print(height(root))
    elif command[0] == 'print':
        tree_list = []
        tree_to_list(root, tree_list)
        if tree_list:
            print(*tree_list)
        else:
            print('Empty')

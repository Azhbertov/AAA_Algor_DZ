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


def find_min(root):
    if root is None:
        return None
    
    current = root
    while current.left is not None:
        current = current.left
    return current


def delete_node(root, key):
    if root is None:
        return None

    if key < root.key:
        root.left = delete_node(root.left, key)
        return root
    if key > root.key:
        root.right = delete_node(root.right, key)
        return root

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


def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


def tree_to_list(root, tree_list):
    if root is None:
        return
    tree_list.append(root.key)
    tree_to_list(root.left, tree_list)
    tree_to_list(root.right, tree_list)


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
    elif command[0] == 'height':
        print(height(root))
    elif command[0] == 'print':
        tree_list = []
        tree_to_list(root, tree_list)
        if tree_list:
            print(*tree_list)
        else:
            print('Empty')
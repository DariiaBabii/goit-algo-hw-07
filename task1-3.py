class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

def max_value_node(node):
    current = node
    while current.right:
        current = current.right
    return current

def postorder_traversal(root):
    sum = postorder_traversal_helper(root, 0)
    return sum


def postorder_traversal_helper(node, sum):
    if node:
        sum = postorder_traversal_helper(node.left, sum)
        sum = postorder_traversal_helper(node.right, sum)
        sum += node.val
    return sum

def print_min_value(node):
    print(f"Мінімальне значення: {min_value_node(node).val}")

def print_max_value(node):
    print(f"Максимальне значення: {max_value_node(node).val}")


def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root

# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

root = delete(root, 7)
print(root)
print_min_value(root)  
print_max_value(root)  
print("Сума всіх значень в дереві:", postorder_traversal(root))
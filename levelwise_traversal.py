class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Tree(value)
    elif value < root.value:
        insert(root.left, value)
    else:
        insert(root.right, value)


def levelwise(root):
    front = 0
    queue = [root]
    while not queue:
        temp = queue[front]
        print(temp.value)
        queue.append(temp.left)
        queue.append(temp.right)
        front += 1




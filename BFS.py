from collections import deque

class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

# def findMinimumBFS(root):
#     if not root: return None

#     queue = deque([root])
#     min_val = root.value

#     while queue:
#         node = queue.popleft()

#         if node.value < min_val:
#             min_val = node.value
#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)

#     return min_val

def leveOrderTraversal(root):
    if not root:
        return None
    queue = deque([root])
    depth = 0
    while queue:
        
        for i in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            print(node.value)
            if node.right:
                queue.append(node.right)
        depth += 1

    return depth

root = TreeNode(10)
root.left = TreeNode(5, TreeNode(2), TreeNode(7))
root.right = TreeNode(15, TreeNode(12), TreeNode(20))
print(leveOrderTraversal(root))
# print(findMinimumBFS(root))  # Output → 2
        
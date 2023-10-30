from node import Node
from binary_tree import BinaryTree

# left = Node(6)
# right = Node(13)
# a_new_node = Node(24)
# head = Node(9)

# head.left = left
# head.right = right

# print(head)
# print(head.left)
# print(head.right)

binary_tree = BinaryTree(Node(9))
for num in [6,7,3,8,4,2,1,11,12,13,45678,14,44444444444]:
    binary_tree.add(Node(num))
    print(f"Node {num} has been added to the binary tree.")

print(f"Binary tree's head is {binary_tree.head}.")
print(f"Binary tree's left is {binary_tree.head.left}.")
print(f"Binary tree's right is {binary_tree.head.right}.")

# binary_tree.inorder()

# binary_tree.preorder()

binary_tree.find(12)
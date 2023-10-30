from node import Node

class BinaryTree:
    def __init__(self, head: Node):
        self.head = head
    
    def add(self, new_node: Node):
        current_node = self.head
        while current_node:
            if new_node.value == current_node.value:
                raise ValueError("A node with that value already exists.")
            elif new_node.value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break
            elif new_node.value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node 
                    break
    
    def find(self, value: int):
        current_node = self.head
        while current_node:
            if value == current_node.value:
                return current_node
            elif value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    break
            elif value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    break

    def inorder(self):
        return self._inorder_recursive(self.head)
    
    def _inorder_recursive(self, current_node):
        if not current_node:
            return
        self._inorder_recursive(current_node.left)
        print(current_node)
        self._inorder_recursive(current_node.right)

    def preorder(self):
        return self._preorder_recursive(self.head)
    
    def _preorder_recursive(self, current_node):
        if not current_node:
            return
        print(current_node)
        self._preorder_recursive(current_node.left)
        self._preorder_recursive(current_node.right)

    def find_parent(self, value: int) -> Node:
        if self.head and self.head.value == value: #This is because the head doen't have a parent.
            return self.head   
        current_node = self.head
        while current_node:
            if(current_node.left and current_node.left.value == value) or\
                (current_node.right and current_node.right.value == value):
                return current_node
            elif value > current_node.value:
                current_node = current_node.right
            elif value < current_node.value:
                current_node = current_node.left

    def find_rightmost(self, node: Node) -> Node:
        current_node = node
        while current_node.right:
            current_node = current_node.right
        return current_node
    
    def delete(self, value: int):
        to_delete = self.find(value)
        parent_of_to_delete = self.find_parent(value)

        if to_delete.left and to_delete.right:
            #It has 2 children
            rightmost = self.find_rightmost(to_delete.left)
            rightmost_parent =self.find_parent(rightmost.value)
            
            if rightmost_parent != to_delete:
                    rightmost_parent.right = rightmost.left
                    rightmost.left = to_delete.left

            if to_delete == parent_of_to_delete.left:
                rightmost.right = to_delete.right
                parent_of_to_delete.left = rightmost
            
            elif to_delete == parent_of_to_delete.right:
                rightmost.right = to_delete.right
                parent_of_to_delete.right = rightmost
            
            else:
                rightmost.right = to_delete.right
                self.head = rightmost

        elif to_delete.left or to_delete.right:
            #It has 1 child.
            if parent_of_to_delete.left == to_delete:
                parent_of_to_delete.left = to_delete.right or to_delete.left
            elif parent_of_to_delete.right == to_delete:
                parent_of_to_delete.right = to_delete.left or to_delete.right
            else:
                self.head = to_delete.right or to_delete.left    
        else:
            #No children
            if parent_of_to_delete.right == to_delete:
                parent_of_to_delete.right = None
            elif parent_of_to_delete.left == to_delete:
                parent_of_to_delete.left = None
            else:
                self.head = None


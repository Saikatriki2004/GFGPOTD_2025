# Node Class:
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def inOrder(self, root: Node):
        result = []
        current = root
        
        while current:
            if current.left is None:
                # If there is no left child, visit this node and move to right child.
                result.append(current.data)
                current = current.right
            else:
                # Find the inorder predecessor of current
                predecessor = current.left
                while predecessor.right is not None and predecessor.right != current:
                    predecessor = predecessor.right
                
                if predecessor.right is None:
                    # Establish a temporary thread to the current node.
                    predecessor.right = current
                    current = current.left
                else:
                    # Thread exists: remove it and visit the current node.
                    predecessor.right = None
                    result.append(current.data)
                    current = current.right
        
        return result

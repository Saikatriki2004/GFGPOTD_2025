#User function Template for python3

'''
# Node class
class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''
# Note: Build tree and return root node
class Solution:
    def buildTree(self, inorder, preorder):
        if not inorder or not preorder:
            return None
        root_val=preorder[0]
        root=Node(root_val)
        mid_val=inorder.index(root_val)
        root.left=self.buildTree(inorder[:mid_val],preorder[1:mid_val+1])
        root.right=self.buildTree(inorder[mid_val+1:],preorder[mid_val+1:])
        return root

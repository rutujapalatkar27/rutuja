class node:
    def __init__(self, data=None):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
    def insert(self, data):
        if self.root==None:
            self.root=node(data)
        else:
            self._insert(data, self.root)
    def _insert(self, data, cur_node):
        if(data < cur_node.data):
            if(cur_node.left==None):
                cur_node.left=node(data)
            else:
                self._insert(data, cur_node.left)
        elif(data > cur_node.data):
            if(cur_node.right ==None):
                cur_node.right=node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("The number is already present in the tree")
    def find(self, data):
        if(self.root==None):
            return None
        else:
            is_found=self._find(self, data, self.root)
            if(is_found):
                return True
            else:
                return False
    def _find(self, data, cur_node):
        if(data < cur_node.data and cur_node.left):
            return self._find(data, cur_node.left)
        elif(data > cur_node.data and cur_node.right):
            return self._find(data, cur_node.right)
        if(data == cur_node.data):
            return True
    def print_tree(self, start, traversal_type):
        """root->left->right"""
        if(traversal_type=="preorder"):
            return self.preorder_print(bst.root, "")
        elif(traversal_type=="inorder"):
            return self.inorder_print(bst.root, "")
        elif(traversal_type=="postorder"):
            return self.postorder_print(bst.root, "")
        else:
            print("traversal type"+"str(traversal_type)"+ "is not supported")
            return False

    def preorder_print(self, start, traversal):
        #root->left->right
        if start:
            traversal+=(str(start.data)+"-")
            traversal=self.preorder_print(start.left, traversal)
            traversal=self.preorder_print(start.right,traversal)
        return traversal
        #leetcode_question 94
    # def inorderTraversal(self, root):
    #     if root:
    #         tree_vls=self.inorderTraversal(root.left)
    #         tree_vls.append(root.data)
    #         tree_vls=self.inorderTraversal(root.right)           
    #         return tree_vls
    def inorder_print(self, start, traversal):
        #left->root->right
        if start:
            traversal=self.inorder_print(start.left, traversal)
            traversal+=(str(start.data)+"-")
            traversal=self.inorder_print(start.right,traversal)
        return traversal
    def postorder_print(self, start, traversal):
        #left->right->root
        if start:
            traversal=self.postorder_print(start.left,traversal)
            traversal=self.postorder_print(start.right,traversal)
            traversal+=(str(start.data)+"-")
        return traversal
        

bst= BST()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)
#print(bst.print_tree(4, "preorder"))
print(bst.print_tree(4, "inorder"))



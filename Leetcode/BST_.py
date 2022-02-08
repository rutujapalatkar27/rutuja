class node:
    def __init__(self,data=None):
        self.data=data
        self.right=None
        self.left=None
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
    def print(self, node):
        print(node.data)
    def inorder(self, node):
        self.inorder(node.left)
        self.print(node)
        self.inorder(node.right)

bst= BST()

bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)

bst.inorder()






   

            

# required for method postordereval, to evaluate the
# expression in the parse tree after completion of
# the tree.
import operator 

class BinaryTree:
    """
    A recursive implementation of Binary Tree
    Using links and Nodes approach.

    Modified to allow for trees to be constructed
    from other trees rather than always creating
    a new tree in the insertLeft or insertRight
    """

    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):

        if isinstance(newNode, BinaryTree):
            t = newNode
        else:
            t = BinaryTree(newNode)

        if self.leftChild is not None:
            t.leftChild = self.leftChild

        self.leftChild = t

    def insertRight(self,newNode):
        if isinstance(newNode,BinaryTree):
            t = newNode
        else:
            t = BinaryTree(newNode)

        if self.rightChild is not None:
            t.rightChild = self.rightChild
        self.rightChild = t

    def isLeaf(self):
        return ((not self.leftChild) and (not self.rightChild))

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self,):
        return self.key

    def preorder(self): # internal preorder method
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def postorder(self): # internal postorder method
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key)
    
    #Evaluate an expression stored in a parse tree
    # internal postorder eval with return vice print
    def postordereval(self): 
        # imported operators or functions
        opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
        
        leftC = None
        rightC = None
        
        if self.leftChild:
            # get LC of current node, run recursive eval
            leftC = self.leftChild.postordereval()  #// \label{pe left}
        
        if self.rightChild:
            # get LC of current node, run recursive eval
            rightC = self.rightChild.postordereval() #// \label{pe right}
        if leftC and rightC:    # if both None, current is leaf
            
            # if not both None, look up the operator in current node
            # apply opers of key to results from recursive eval of LC and RC
            return opers[self.key](leftC,rightC) #// \label{total pe eval}
        else:
            return self.key   # None, no LC or RC, return root
    
    #internal inorder method, prints keys without parenthesis
    def inorder(self): 
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key)
        if self.rightChild:
            self.rightChild.inorder()
    
    # prints expression with parenthesis; uses inorder traversal
    def printexp(self):
        if self.leftChild:
            print('(', end=' ')
            self.leftChild.printexp()
        print(self.key, end=' ')
        if self.rightChild:
            self.rightChild.printexp()
            print(')', end=' ')

    def height(self, tree):
        if tree == None:
            return -1
        else:
            return 1 + max(height(tree.leftChild),height(tree.rightChild))


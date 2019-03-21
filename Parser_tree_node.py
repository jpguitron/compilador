class Tree_Node:
    #When a Tree_Node is created it should receive a root value and 
    def __init__(self, root):
        self.root = root
        self.children = []

    #When a child is added a new Tree_Node is created
    def addChild(self,child):
        self.children.append(child)

    #Print the tree, this function receive a start identation
    def Tree_Node_Print(self,indentation):
        print("\t" * indentation,self.root)
        for child in self.children:
            child.Tree_Node_Print(indentation+1)
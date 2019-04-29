def declare_glob_variables(tree,generator):
    for node in tree.children:
        if node.root == "int":
            if len(node.children) != 1:
               generator.write(".space "+str(node.children[2].root * 4)) 
            generator.write(str(node.children[0].root)+": .word 0")
            #remove de variable from the tree
            tree.children.remove(node)

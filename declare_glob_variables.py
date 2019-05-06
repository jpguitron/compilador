def declare_glob_variables(tree,generator):
   remove_list = []
   for node in tree.children:
      if node.root == "int":
         generator.variables_directory[node.children[0].root] = node.children[0].root
         if len(node.children) != 1:
            generator.global_arrays[node.children[0].root] = node.children[2].root
            generator.write(".space "+str((node.children[2].root * 4)+4)) 
            generator.write(str(node.children[0].root)+": .word 0")
         else:
            generator.write(str(node.children[0].root)+": .word 4")
         #remove de variable from the tree
         remove_list.append(node)
         #tree.children.remove(node)
   for node in remove_list:
      tree.children.remove(node)


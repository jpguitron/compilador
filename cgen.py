compare_types = ["+","-","*","/","<","<=",">",">=","==","!=","="]
class Code_generator:

    #Get the name for the file
    def __init__(self, file):
        self.file_name = file

    #to open the file
    def openFile(self):
        self.file = open(self.file_name,"w+")

    #to close the file
    def closeFile(self):
        self.file.close()

    #For writing in a file
    def write(self,line):
        self.file.write(line)
        self.file.write("\n")

variables_directory = {}
offset = 0

def generateCode(tree,generator):
    global offset, variables_directory

    if tree.root == "int":
        generator.write("li $a0 0")
        generator.write("sw $a0 0($sp)")
        generator.write("addiu $sp $sp -4")
        variables_directory[tree.children[0].root] = offset
        offset += 4

    elif tree.root == "output":
        output_code(tree.children[0].children[0].children[0].root,generator)

    elif findOperators(tree,generator):
        pass

    elif tree.root not in compare_types:
        for node in tree.children:
            generateCode(node,generator)

#check operators
def findOperators(tree,generator):
    global offset, variables_directory

    if tree.root in compare_types:

        leftChild = tree.children[0]
        rightChild = tree.children[1]

        #when = operation
        if tree.root == "=":
            #When the rightChild is an integer
            if represents_int(rightChild.root):
                offset_local = str(offset-variables_directory[leftChild.root])
                generator.write("li $a0 "+str(rightChild.root))
                generator.write("sw $a0 "+str(offset_local)+"($sp)")
                
                
            #when the rightChild is a character
            elif rightChild.root in compare_types:
                findOperators(rightChild,generator)
                generator.write("addiu $sp $sp 4")
                offset -= 4
                offset_local = str(offset-variables_directory[leftChild.root])
                generator.write("sw $a0 "+str(offset_local)+"($sp)")
                

            #when is equal to another variable
            else: 
                last_child = tree.children[len(tree.children)-1]
                if represents_int(last_child.root):
                    generator.write("li $a0 "+str(last_child.root))

                elif last_child.root in compare_types:
                    findOperators(last_child,generator)
                    generator.write("addiu $sp $sp 4")
                    offset -= 4

                else:
                    offset_local = str(offset-variables_directory[leftChild.root])
                    generator.write("lw $a0 "+str(offset_local)+"($sp)")

                for i in range(len(tree.children)-1):
                    offset_local = str(offset-variables_directory[tree.children[i].root])
                    generator.write("sw $a0 "+str(offset_local)+"($sp)")

        #when + operation
        if tree.root == "+":

            if(represents_int(leftChild.root)):
                generator.write("li $a0 "+str(leftChild.root))
                generator.write("sw $a0, 0($sp)")
                generator.write("addiu $sp $sp -4")
                offset += 4

            else:
                findOperators(leftChild,generator)

            if(represents_int(rightChild.root)):
                generator.write("li $a1 "+str(rightChild.root))
                generator.write("sw $a1, 0($sp)")
                generator.write("addiu $sp $sp -4")
                offset += 4
            else:
                findOperators(rightChild,generator)
            
            offset -= 4
            generator.write("lw $a0, 4($sp)")
            
            offset -= 4
            generator.write("lw $a1, 8($sp)")

            generator.write("add $a0 $a0 $a1")
            generator.write("addiu $sp $sp 8")

            generator.write("sw $a0, 0($sp)")
            generator.write("addiu $sp $sp -4")
            offset += 4
        pass

    #elif represents_int(tree.root):

#To print te value of a variable
def output_code(var,generator):
    offset_local = str(offset-variables_directory[var])
    generator.write("li $v0 1")
    generator.write("lw $a0 "+str(offset_local)+"($sp)")
    generator.write("syscall")


#Check if string can be cast to int
def represents_int(num):
    try: 
        int(num)
        return True
    except ValueError:
        return False

#ver que onda con el analizador semantico
def codeGen(tree,file):

    if tree != None:
        generator = Code_generator(file)
        generator.openFile()

        #to write the headers in the file
        generator.write(".text")
        generator.write(".globl main")
        generator.write("main:")
        
        generateCode(tree,generator)

        generator.write("li $v0, 10")
        generator.write("syscall")

        generator.closeFile()


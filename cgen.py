#estos dos van en findOperators
#falta caso a = func()
#a = b[1]

compare_types = ["+","-","*","/","<","<=",">",">=","==","!=","="]
class Code_generator:

    #Get the name for the file
    def __init__(self, file):
        self.file_name = file
        self.offset = 0
        self.variables_directory = {}

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


def generateCode(tree,generator):

    #if a int is founded
    if tree.root == "int":
        generator.write("li $a0 0")
        generator.write("sw $a0 0($sp)")
        generator.write("addiu $sp $sp -4")
        generator.variables_directory[tree.children[0].root] = generator.offset
        generator.offset += 4

    #if output is founded
    elif tree.root == "output":
        output_code(tree.children[0].children[0].children[0].root,generator)

    #if a ["+","-","*","/","<","<=",">",">=","==","!=","="] was founded
    elif findOperators(tree,generator):
        pass

    #if other character is found children of the actual node are called
    elif tree.root not in compare_types:
        for node in tree.children:
            generateCode(node,generator)

#check operators
def findOperators(tree,generator):

    #if the actual character is in the character list
    if tree.root in compare_types:

        leftChild = tree.children[0]
        rightChild = tree.children[1]

        #when = operation
        if tree.root == "=":
            #When the rightChild is an integer
            if represents_int(rightChild.root):
                offset_local = str(generator.offset-generator.variables_directory[leftChild.root])
                generator.write("li $a0 "+str(rightChild.root))
                generator.write("sw $a0 "+str(offset_local)+"($sp)")
                
            #when the rightChild is a character
            elif rightChild.root in compare_types:
                findOperators(rightChild,generator)
                generator.write("addiu $sp $sp 4")
                generator.offset -= 4
                offset_local = str(generator.offset-generator.variables_directory[leftChild.root])
                generator.write("sw $a0 "+str(offset_local)+"($sp)")

            #when is equal to another variable
            else: 
                last_child = tree.children[len(tree.children)-1]

                #if the last child is a int
                if represents_int(last_child.root):
                    generator.write("li $a0 "+str(last_child.root))

                #if the last child is an arithmetic operator
                elif last_child.root in compare_types:
                    findOperators(last_child,generator)
                    generator.write("addiu $sp $sp 4")
                    generator.offset -= 4
                #if it is a variable
                else:
                    offset_local = str(generator.offset-generator.variables_directory[rightChild.root])
                    generator.write("lw $a0 "+str(offset_local)+"($sp)")
                
                #copy the child to all previus variables
                for i in range(len(tree.children)-1):
                    offset_local = str(generator.offset-generator.variables_directory[tree.children[i].root])
                    generator.write("sw $a0 "+str(offset_local)+"($sp)")

        #for arithmetic operators
        if tree.root == "+" or tree.root == "-" or tree.root == "*" or tree.root == "/":
            
            #to process the children
            process_arithmetic_operator(leftChild,generator)
            process_arithmetic_operator(rightChild,generator)
            
            #load the last two variables
            generator.write("lw $a1, 4($sp)")
            generator.write("lw $a0, 8($sp)")

            #make the operation
            choose_operation(tree.root,generator)

            #free the last 8 spaces of the stack
            generator.write("addiu $sp $sp 8")
            generator.offset -= 8

            #save the result in the stack
            generator.write("sw $a0, 0($sp)")
            generator.write("addiu $sp $sp -4")
            generator.offset += 4
        return True
    return False

#process child for arithmetic operators
def process_arithmetic_operator(child,generator):

    #if the child is a int
    if(represents_int(child.root)):
        generator.write("li $a0 "+str(child.root))
        generator.write("sw $a0, 0($sp)")
        generator.write("addiu $sp $sp -4")
        generator.offset += 4

    #if the child is an operator
    elif child.root in compare_types:
        findOperators(child,generator)

    #if the child is a variable
    else:
        offset_local = str(generator.offset-generator.variables_directory[child.root])
        generator.write("lw $a0 "+str(offset_local)+"($sp)")
        generator.write("sw $a0, 0($sp)")
        generator.write("addiu $sp $sp -4")
        generator.offset += 4

def choose_operation(operation,generator):
    if operation == "+":
        generator.write("add $a0 $a0 $a1")

    elif operation == "-":
        generator.write("sub $a0 $a0 $a1")
        
    elif operation == "*":
        generator.write("mul $a0 $a0 $a1")

    elif operation == "/":
        generator.write("div $a0 $a1")  
        generator.write("mflo $a0")  

#To print te value of a variable
def output_code(var,generator):
    offset_local = str(generator.offset-generator.variables_directory[var])
    generator.write("li $v0 1")
    generator.write("lw $a0 "+str(offset_local)+"($sp)")
    generator.write("syscall")
    generator.write("li $v0 4")
    generator.write("la $a0 newline")
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
        generator.write(".data")
        generator.write('newline: .asciiz "\n"')
        generator.write(".text")
        generator.write(".globl main")
        generator.write("main:")
        
        generateCode(tree,generator)

        generator.write("li $v0, 10")
        generator.write("syscall")

        generator.closeFile()


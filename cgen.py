#estos dos van en findOperators
#falta caso a = func()
#falta caso a = func()+1
#checar con funciones los =
#poner si se iguala a parte especifica del arreglo
#a = b[1]

compare_types = ["+","-","*","/","<","<=",">",">=","==","!=","="]
word_size = 4
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
        #to declare a array
        if len(tree.children)>=3 and tree.children[1].root == "arr_statement" and represents_int(tree.children[2].root):
            #to indicate the size of the array
            generator.variables_directory[tree.children[0].root+"_tam"] = int(tree.children[2].root)
            generator.write("li $a0 "+str(tree.children[2].root))
            generator.write("sw $a0 0($sp)")
            generator.write("addiu $sp $sp -4")
            generator.offset += 4

            #to initialize all the array with 0
            
            generator.variables_directory[tree.children[0].root] = generator.offset
            for i in range(int(tree.children[2].root)):
                generator.write("li $a0 0")
                generator.write("sw $a0 0($sp)")
                generator.write("addiu $sp $sp -4")
                generator.offset += 4

        #if a variable is declared
        else:
            generator.write("li $a0 0")
            generator.write("sw $a0 0($sp)")
            generator.write("addiu $sp $sp -4")
            generator.variables_directory[tree.children[0].root] = generator.offset
            generator.offset += 4

    #if output is founded
    elif tree.root == "output":
        output_code(tree.children[0].children[0].children[0],generator)

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
                if len(leftChild.children) == 1:
                    verify_array_index(leftChild,generator,"write",rightChild.root)

                else:
                    offset_local = str(generator.offset-generator.variables_directory[leftChild.root])
                    generator.write("li $a0 "+str(rightChild.root))
                    generator.write("sw $a0 "+str(offset_local)+"($sp)")
                
            #when the rightChild is a character
            elif rightChild.root in compare_types:
                findOperators(rightChild,generator)
                generator.write("addiu $sp $sp 4")
                generator.offset -= 4
                

                if len(leftChild.children) == 1:
                    verify_array_index(leftChild,generator,"save")
                else:
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
                    #if it is equal to a array 
                    if len(last_child.children) == 1:
                        verify_array_index(last_child,generator,"load")

                    else:
                        offset_local = str(generator.offset-generator.variables_directory[last_child.root])
                        generator.write("lw $a0 "+str(offset_local)+"($sp)")
            
                
                #checar multiples == 
                #copy the child to all previus variables
                for i in range(len(tree.children)-1):
                    if len(tree.children[i].children) == 1:
                        verify_array_index(tree.children[i],generator,"save")
                    else:
                        offset_local = str(generator.offset-generator.variables_directory[tree.children[i].root])
                        generator.write("sw $a0 "+str(offset_local)+"($sp)")

        #for arithmetic operators
        if tree.root == "+" or tree.root == "-" or tree.root == "*" or tree.root == "/":
            
            #to process the children
            process_arithmetic_operator(leftChild,generator)
            process_arithmetic_operator(rightChild,generator)
            
            #load the last two variables
            generator.write("lw $t1, 4($sp)")
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



#check the index of the array
def verify_array_index(child, generator, mode, value=0):


    #to get the size of the array
    offset_local = generator.offset - (generator.variables_directory[child.root]-word_size)
    generator.write("lw $t3 "+str(offset_local)+"($sp)")

    #to get the value of the index
    

    if represents_int(child.children[0].root):
        generator.write("li $t0 "+str(child.children[0].root))
    else:
        if len(child.children[0].children) == 1:
            verify_array_index(child.children[0], generator, "load")
            generator.write("move $t0 $a0")
        else:
            offset_local = generator.offset - generator.variables_directory[child.children[0].root]
            generator.write("lw $t0 "+str(offset_local)+"($sp)")



    #check for out of bounds
    generator.write("blt $t0 $zero Outbounds")
    generator.write("bge $t0 $t3 Outbounds") 

    generator.write("move $t1 $sp")                                       
    generator.write("addiu $t1 $t1 " + str(generator.offset - generator.variables_directory[child.root]))   
    generator.write("li $t2 4")                                            
    generator.write("mul $t0 $t0 $t2")                                    
    generator.write("sub $t1 $t1 $t0")                                    

    if mode == "write":
        if represents_int(value):
            generator.write("li $a0 "+str(value))
        else:
            offset_local = generator.offset - generator.variables_directory[value]
            generator.write("lw $a0 "+str(offset_local)+"($sp)")  
        generator.write("sw $a0 0($t1)")

    elif mode == "load": 
        generator.write("lw $a0 0($t1)")

    elif mode == "save":
        generator.write("sw $a0 0($t1)")
    

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
        if len(child.children) == 1:
            verify_array_index(child,generator,"load")
        else:
            offset_local = str(generator.offset-generator.variables_directory[child.root])
            generator.write("lw $a0 "+str(offset_local)+"($sp)")

        generator.write("sw $a0, 0($sp)")
        generator.write("addiu $sp $sp -4")
        generator.offset += 4

def choose_operation(operation,generator):
    if operation == "+":
        generator.write("add $a0 $a0 $t1")

    elif operation == "-":
        generator.write("sub $a0 $a0 $t1")
        
    elif operation == "*":
        generator.write("mul $a0 $a0 $t1")

    elif operation == "/":
        generator.write("div $a0 $t1")  
        generator.write("mflo $a0")  

#To print te value of a variable
def output_code(var,generator):
    
    if len(var.children) == 1:
        verify_array_index(var,generator,"load")
    else:
        offset_local = str(generator.offset-generator.variables_directory[var.root])
        generator.write("lw $a0 "+str(offset_local)+"($sp)")

    generator.write("li $v0 1")
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
        generator.write('outbounds: .asciiz "Variable fuera del indice: runtime error \n"')
        generator.write(".text")
        generator.write(".globl main")
        generator.write("main:")
        
        generateCode(tree,generator)


        generator.write("End:")
        generator.write("li $v0, 10")
        generator.write("syscall")

        generator.write("Outbounds:")
        generator.write("li $v0 4")
        generator.write("la $a0 outbounds")
        generator.write("syscall")
        generator.write("j End")

        generator.closeFile()


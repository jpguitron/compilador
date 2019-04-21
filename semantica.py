
error = False
reservadas = ["int","void","else","if","return","while"]
compare_types = ["+","-","*","/","<","<=",">",">=","==","!=","="]
class Table_Scope:
    #When a Tree_Node is created it should receive a root value and 
    def __init__(self, scope, parent):
        self.scope = scope 
        self.children = []
        self.scopes = []
        self.parent = parent

    #When a child is added a new Table_Scope is created
    def addChild(self,child):
        self.children.append(child)

    #Add a scope to the scope list
    def addScope(self, table_scope):
        self.scopes.append(table_scope)

    #print children
    def printTable(self,indentation):
        
        #print the name of the scope
        print("\t" * indentation, self.scope)

        #print the children of the scope
        for child in self.children:
            print("\t" * indentation,child)
        
        #call the others scopes
        for scope in self.scopes:
            scope.printTable(indentation+1)
    

def semantica(AST, imprime = True):
    if AST != None:
        tabl = tabla(AST,imprime)
        if tabl == None:
            exit(0)
        return tabl
    return None

#remove unncesary scopes
def clean_table(table):
    
    for scope in table.scopes:
        if not clean_table(scope):
            table.scopes.remove(scope)

    if len(table.children) == 0 and len(table.scopes) == 0:
        return False
        
    return table



def tabla(tree, imprime = True):
    
    table = Table_Scope("Scope: 0", None)
    table.children.append(['input','int','args_statement','void'])
    table.children.append(['output','void','args_statement','int'])
    tabla = generateTable(table,tree,0,False)

    clean_table(tabla)
    verify_return(tabla)
    verify_main_position(tabla)

    if imprime and not error:
        tabla.printTable(0)
    if error:
        return None

    return tabla

#Check if all int functions return an int
def verify_return(table):
    for child in table.children:
        if len(child) == 2:
            return

        if child [0] != "input" and child [0] != "output" and child [2] == "args_statement" and child[1] =="int" :
            exist = False
            for scope in table.scopes:
                if child [0] == scope.children[0][0]:
                    for chil in scope.children:
                        if chil[0] == "return":
                            exist = True
            if not exist:
                trigger_error("La función "+child [0]+" debe regresar un entero")

#Check that the last child of the scope 0 is a main function
def verify_main_position(table):
    if table.children[len(table.children)-1][0] != "main" or table.children[len(table.children)-1][2] != "args_statement":
        trigger_error("La función main debe ser la última declarada en el Scope 0")


    
                    
#For creating the table
def generateTable(table,tree,lvl,function_added):
    
    #create a new scope if a compount_stmt is found
    if tree.root == "compound_stmt" and not function_added:
        lvl+=1
        tab = Table_Scope("Scope: "+str(lvl), table)
        table.addScope(tab)
        table = tab

    #Don't add the first compount_stmt in a function
    if function_added:
        function_added = False

    #A variable could not be declared as void (Punto 2)
    if tree.root == "void" and len(tree.children) > 0:
        void_tuple= []
        void_tuple.append(tree.children[0].root)
        trigger_error("void no es válido para declarar una variable "+void_tuple[0])
        table.addChild(void_tuple)

    #If a integer declaration is found
    elif tree.root == "int" and len(tree.children) > 0:

        int_tuple = []
        int_tuple.append(tree.children[0].root)
        int_tuple.append(tree.root)

        for i in range(1,len(tree.children)):
            int_tuple.append(tree.children[i].root)

        #validate if it wasn't declared before
        if verifyDeclaration(table, int_tuple[0]):
            table.addChild(int_tuple)

    #If a function declaration is found
    elif tree.root == "fun_declaration":
        
        fun_tuple = []
        fun_tuple.append(tree.children[1].root)
        fun_tuple.append(tree.children[0].root)
        fun_tuple.append(tree.children[2].root)

        #get the values of the param list
        if tree.children[3].root == "param_list":
            for i in range(len(tree.children[3].children)):
                if len(tree.children[3].children[i].children)==2:
                    fun_tuple.append("arr_statement")
                else:
                    fun_tuple.append(tree.children[3].children[i].root)
        else:
            fun_tuple.append("void")
        
        #if return int check if exist
        if tree.children[0].root == "int":
             fun_tuple.append("return")

        #create a new scope
        if verifyDeclaration(table, fun_tuple[0]):

            table.addChild(fun_tuple)


            lvl+=1
            tab = Table_Scope("Scope: "+str(lvl), table)
            table.addScope(tab)
            table = tab
            
            function_added = True

            table.addChild(fun_tuple)
        #If it was already declared then create a scope without the function in scope
        else:
            function_added = True
            lvl+=1
            tab = Table_Scope("Scope: "+str(lvl), table)
            table.addScope(tab)
            table = tab

    for node in tree.children:
        generateTable(table,node,lvl,function_added)

    verify_types(tree,table)

    return table


#check if a variable was already decleared in the scope
def verifyDeclaration(scope, variable_name):
    for child in scope.children:
        if child[0] == variable_name:
            trigger_error(variable_name+ " ya había sido declarada en el scope "+scope.scope)
            return False

    return True

#get a specific child of the table
def getChild(scope, var):
    if scope != None:
        for child in scope.children:
            if child[0] == var:
                return child
        return getChild(scope.parent,var)

    return False

#Verify types of operations
def verify_types(node,table):

    #For verifying the characters
    if node.root in compare_types:
        verify_equals(node,table)
    
    #For verifying the functions
    elif len(node.children)> 0 and node.children[0].root == "args_statement":
        
        if check_in_table(table,table, node.root):
            #if len(node.children[0].children) == 1 and node.children[0].children[0].root == "arg_list":
            valid = True
            count = 0
            variable_types = []
            if len(node.children[0].children) == 1:
                for param in node.children[0].children[0].children:
                    if not represents_int(param.root):
                        valid = check_in_table_operators(table,table,param,False)
                        count += 1
                        actual_child = getChild(table,param.root)

                        if actual_child and len(actual_child) == 2:
                            variable_types.append("int")
                        else:
                            if len(param.children)>0:
                                variable_types.append("int")
                            else:
                                variable_types.append("arr_statement")
                    else:
                        count += 1
                        variable_types.append("int")
            if valid:
                params_on_function = get_function_n_params(table, node.root)
                actual_child = getChild(table,node.root)
                if len(actual_child)!= 2 and variable_types != params_on_function and actual_child[2] != "arr_statement":
                    trigger_error("Se esperaban los parámetros "+str(params_on_function)+" y se encontraron "+str(variable_types)+" al llamar la función " + node.root)

    #For verifying that a function void doesn't have a return
    elif node.root == "return":
        founded = False
        tab_actual = table
        while not founded and tab_actual.parent != None:
            for nod in tab_actual.children:
                if len(nod)>=3:
                    founded = True
                    if nod[1]=="void":
                        trigger_error("No debe haber un return en una función void ("+nod[0]+")")
                    else:
                        if len(node.children) == 0:
                            trigger_error("falta parametro en return")
                            break
                        elif  check_in_table(table,table,node.children[0].root):
                            c = getChild(table,node.children[0].root)
                            if len(c)>=3 and c[2]=='arr_statement' and len(node.children[0].children) !=1:
                                trigger_error("Indice requerido para el arreglo "+c[0]+" en el return de la función")
                            table.addChild([node.root,node.children[0].root])
                            break

                        elif represents_int(node.children[0].root) or node.children[0].root in compare_types:
                            table.addChild([node.root,node.children[0].root])
                            break                            
            if not founded:
                tab_actual = tab_actual.parent
    
    elif "while" == node.root or "if" == node.root:
        if node.children[0].root not in compare_types:
            check_in_table_operators(table, table, node.children[0])
            

    elif not '_' in str(node.root):
        if node.root not in reservadas and node.root not in compare_types:
            if not represents_int(node.root):
                if not check_in_table(table,table, node.root,node.children):
                    trigger_error(node.root+" no ha sido declarado en el scope "+table.scope)



#Get function n_params
def get_function_n_params(table, func):
    params_array = []
    for child in table.children:
        if child[0] == func:
            if len(child) == 2:
                trigger_error(child[0]+" no es una función")
                return None
            if child[3] != "void":
                if child[len(child)-1]=="return":
                    for i in range(3,len(child)-1):
                        params_array.append(child[i]) 
                    return params_array
                for i in range(3,len(child)):
                    params_array.append(child[i]) 
                return params_array
            else:
                return []

    if table.parent != None:
        params = get_function_n_params(table.parent, func)
        if params != 0:
            return params
        else:
            return 0
    else:
        trigger_error("La función "+str(func)+ " no ha sido declarada")
        return 0
    return 0

#Check all children of ["+","-","*","/","<","<=",">",">=","==","!=","="]
def verify_equals(tree,table):

    valid2 = False
    for node in tree.children:
        
        valid = True
        valid2 = False

        if node.root in compare_types:
            for child in node.children:
                valid = verify_equals(child,table)
            if valid:
                continue
            valid = False    
            
        
        elif represents_int(node.root):
            valid2 = True
            continue
        
        elif check_in_table_operators(table, table, node):
            valid2 =  True
            continue

    return True

#Check if string can be cast to int
def represents_int(num):
    try: 
        int(num)
        return True
    except ValueError:
        return False

#check if a function was declared in the table in the current or higher scope
def check_in_table(root_table,table, func, child=None):
    
    if child:
        for chil in table.children:
            if chil[0] == func and len(chil)>=3 and chil[2]=="arr_statement" and not represents_int(child[0].root) and len(child[0].children)!=1:
                c = getChild(table, child[0].root)
                if c and len(c)>=3 and c[2]=="arr_statement":
                    trigger_error("Indice requerido para el arreglo "+str(child[0].root))

    ch=child
    if child:
        for child in table.children:
            if child[0] == func and len(child)>=3:
                return True
    else:
        for child in table.children:
            if child[0] == func:
                return True

    if table.parent != None:
        if check_in_table(root_table,table.parent, func):
            return True
        else:
            return False
    else:
        #trigger_error(str(func)+ " no ha sido declarado")
        return False
    return True

#check if a variable was declared in the table in the current or higher scope
def check_in_table_operators(root_table,table, var,access=True):

    #if not table:
    #    return False
    
    for child in table.children:
        #is child 0 because of the structure of the table, all names are on de space 0
        
        if child[0] == var.root:
            
            if child[1] != "int":
                trigger_error("La función "+child[0]+" no regresa ningún parámetro")
                return False
            elif len(var.children) == 0 and len(child)>=3 and child[2]!="arr_statement":
                trigger_error("Una función "+child[0]+" no puede ser llamada como variable")
                return False
            elif len(getChild(table,var.root))>=3 and getChild(table,var.root)[2]== "arr_statement" and len(var.children) == 0 and access:
                trigger_error("Indice requerido para el arreglo "+getChild(table,var.root)[0] )
            
            else:
                
                if len(var.children) != 0:
                    if len(var.children) == 1:
                        #for examples a = b() ven b is not declared as function
                        if len(child) == 2 and var.children[0].root == "args_statement":
                            trigger_error(var.root+" no es una función")
                            return False
                        else:
                            if represents_int(var.children[0].root):
                                if len(child) == 2:
                                    trigger_error(child[0]+" No es un arreglo")
                                    return True
                                if len(child)>3 and child[3] == "void":
                                    trigger_error(child[0]+" no es un arreglo")
                                    return True
                                if len(child)>3:
                                    if  int(child[3]) > int(var.children[0].root):
                                        return True
                                    else:
                                        trigger_error("Índice fuera de rango para la variable "+var.root)
                                        return True
                            elif var.children[0].root == "args_statement":
                                actual_child = getChild(table,var.root)
                                if actual_child and actual_child[2] == "args_statement":
                                    return True
                                else:
                                    trigger_error(var.root+" no es una función")

                            elif var.children[0].root == "arr_statement":
                                actual_child = getChild(table,var.root)
                                if actual_child and actual_child[2] == "arr_statement":
                                    return True
                                else:
                                    trigger_error(var.root+" no es un arreglo")


                    elif child[2] == var.children[0].root:
                        
                        return True
                        
                        if check_in_table_operators(root_table,root_table,var.children[0]):
                            return True
                        

                        trigger_error("Se esperaba recibir argumentos para "+child[0]+" en el scope "+table.scope)
                        return False    
            
            return True

        

    if table.parent != None:
        #print(var.root)
        if check_in_table_operators(root_table,table.parent, var,False):
            return True
        else:
            
            return False
    #else:
    #    trigger_error(str(var.root)+ " no ha sido declarado")

    return False

def trigger_error(err):
    global error
    error = True
    print("Semantic error:")
    print(err)
    
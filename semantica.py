
error = False
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
    table.children.append(['input','int','args','void'])
    table.children.append(['output','void','args','int'])
    tabla = generateTable(table,tree,0,False)

    clean_table(tabla)

    if imprime and not error:
        tabla.printTable(0)
    if error:
        return None

    return tabla

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
        trigger_error("void no es valido para declarar una variable "+void_tuple[0])
        table.addChild(void_tuple)

    #If a integer declaration is found
    if tree.root == "int" and len(tree.children) > 0:

        int_tuple = []
        int_tuple.append(tree.children[0].root)
        int_tuple.append(tree.root)

        for i in range(1,len(tree.children)):
            int_tuple.append(tree.children[i].root)

        #validate if it wasn't declared before
        if verifyDeclaration(table, int_tuple[0]):
            table.addChild(int_tuple)

    #If a function declaration is found
    if tree.root == "fun_declaration":
        
        fun_tuple = []
        fun_tuple.append(tree.children[1].root)
        fun_tuple.append(tree.children[0].root)
        fun_tuple.append(tree.children[2].root)

        #get the values of the param list
        if tree.children[3].root == "param_list":
            for i in range(len(tree.children[3].children)):
                fun_tuple.append(tree.children[3].children[i].root)
        else:
            fun_tuple.append("void")
        
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
            trigger_error(variable_name+ " ya habia sido declarada en el scope "+scope.scope)
            return False

    return True

#Verify types of operations
compare_types = ["+","-","*","/","<","<=",">",">=","==","!=","="]
def verify_types(node,table):

    #For verifying the characters
    if node.root in compare_types:
        verify_equals(node,table)
    
    #For verifying the functions
    elif len(node.children)> 0 and node.children[0].root == "args":
        if check_in_table(table,table, node.root):
            if len(node.children[0].children) == 1 and node.children[0].children[0].root == "arg_list":
                valid = True
                count = 0
                for param in node.children[0].children[0].children:
                    if not represents_int(param.root):
                        valid = check_in_table_operators(table,table,param)
                        count += 1
                    else:
                        count += 1
                if valid:
                    params_on_function = get_function_n_params(table, node.root)
                    if params_on_function != count:
                        trigger_error("Se otubieron "+str(count)+" de "+str(params_on_function)+" parametros al llamar la función " + node.root)
    #For verifying that a function void doesn't have a return
    elif node.root == "return":
        for nod in table.children:
            if len(nod)>=3:
                if nod[1]=="void":
                    trigger_error("No debe haber un return en una función void ("+nod[0]+")")
                else:
                    check_in_table(table,table,node.children[0].root)

        #falta verificar que exista el return



    #if tree.root in compare_types:
    #    print(tree.root+" encontrado")

    #for node in node.children:
    #    verify_types(node,table)

#Get function n_params
def get_function_n_params(table, func):
    for child in table.children:
        if child[0] == func:
            if child[3] != "void":
                return len(child)-3
            else:
                return 0

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
def check_in_table(root_table,table, func):
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
def check_in_table_operators(root_table,table, var):

    #if not table:
    #    return False
    for child in table.children:
        #is child 0 because of the structure of the table, al names are on de space 0
        if child[0] == var.root:
            if len(var.children) != 0:
                if child[2] == var.children[0].root:
                    return True
                else:
                    if represents_int(var.children[0].root):
                        if int(child[3]) > int(var.children[0].root):
                            return True
                        else:
                            trigger_error("Index out of bounds ")
                            return True
                    
                    if check_in_table_operators(root_table,root_table,var.children[0]):
                        return True
                    

                    trigger_error("Se esparaba recibir argumentos para "+child[0]+" en el scope "+table.scope)
                    return False

            return True

    if table.parent != None:
        if check_in_table_operators(root_table,table.parent, var):
            return True
        else:
            return False
    else:
        trigger_error(str(var.root)+ " no ha sido declarado")

    return False

def trigger_error(err):
    global error
    error = True
    print("ERROR:")
    print("\t"+err)
    
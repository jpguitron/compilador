from Parser_tree_node import Tree_Node
from globalTypes import *
from lexer import *
import lexer as lex


def parser(imprime = True):

    #global programa,posicion, progLong, lexer, nline, tokens, tokenTypes, posiciones, lenE, pos

    #Obtiene las va
    programa = lex.programa
    posicion = lex.posicion
    progLong = lex.progLong
    lexer = lex.lexer
    nline = lex.nline
    linesSizes = lex.linesSizes

    #Obtener todos los tokens del archivo
    tokens = []
    tokenTypes = []
    posiciones = []
    lineas = []

    token, tokenString = lex.getToken(False)

    tokenTypes.append(token)
    tokens.append(tokenString)
    posiciones.append(lex.posicion)
    lineas.append(lex.aline)

    while (token != TokenType.ENDFILE):
        token, tokenString = lex.getToken(False)
        tokenTypes.append(token)
        tokens.append(tokenString)
        posiciones.append(lex.posicion)
        lineas.append(lex.aline)

    parse = Paserser_class(tokens, tokenTypes, posiciones,imprime,linesSizes, lineas)
    AST = parse.ejecutar()
    return AST



class Paserser_class:

    def __init__(self, tokens, tokenTypes, posiciones, imprime,linesSizes, lineas):
        self.tokens = tokens
        self.tokenTypes = tokenTypes
        self.posiciones = posiciones
        self.pos = 0
        self.lenE = len(tokens)-1
        self.imprime = imprime
        self.linesSizes = linesSizes 
        self.lineas = lineas
        self.err = 0


    
    def ejecutar(self):
        AST = self.program()
        if self.imprime and self.err == 0:
            AST.Tree_Node_Print(0)
        if self.err == 0:
            return AST
        return None

    #1.	program --> declaration-list 
    def program(self):
        return self.declaration_list()

    #2.	declaration-list --> declaration {declaration} 
    def declaration_list(self):
        AST = Tree_Node("declaration_list")
        child = self.declaration()
        if child is not None:
            AST.addChild(child)
        else:
            self.error()
        
        while self.pos < self.lenE-1:
            child = self.declaration()
            if child is not None:
                AST.addChild(child)
            else:
                self.error()

        return AST
        
    #3.	declaration --> var-declaration | fun-declaration
    def declaration(self):
        posA = self.pos
        child = self.var_declaration()

        if child is not None:
            return child
        
        posMayor = self.pos

        self.pos = posA

        child = self.fun_declaration()
        if child is not None:
            return child

        if posMayor < self.pos:
            posMayor = self.pos
        
        self.pos = posMayor
        
        return None

    #4.	var-declaration --> type-specifier ID [ [ NUM ] ] ;
    def var_declaration(self):
        AST = self.type_specifier()
        if AST is not None:
            tok = self.match(TokenType.ID)
            if tok is not None:
                AST.addChild(tok)
                tok = self.match(TokenType.SEMICOLON)
                if tok is not None:
                    return AST
                tok = self.match(TokenType.LBRACKET)
                if tok is not None:
                    AST.addChild(Tree_Node("arr_statement"))
                    tok = self.match(TokenType.NUM)
                    if tok is not None:
                        AST.addChild(tok)
                        tok = self.match(TokenType.RBRACKET)
                        if tok is not None:
                            tok = self.match(TokenType.SEMICOLON)
                            if tok is not None:
                                return AST
                            else:
                                self.error(False)
                                return AST
        return None

    #5.	type-specifier --> int | void
    def type_specifier(self):

        tok = self.match(TokenType.INT)
        if tok is not None:
            return tok
        tok = self.match(TokenType.VOID) 
        if tok is not None:
            return tok

        return None

    #6.	fun-declaration --> type-specifier ID ( params ) compound-stmt
    def fun_declaration(self):
        AST = Tree_Node("fun_declaration")
        child = self.type_specifier()
        if child is not None:
            AST.addChild(child)
            tok = self.match(TokenType.ID)
            if tok is not None:
                AST.addChild(tok)
                AST.addChild(Tree_Node("args_statement"))
                tok = self.match(TokenType.LPAREN)
                if tok is not None:
                    child = self.params()
                    if child is not None:
                        AST.addChild(child)
                        tok = self.match(TokenType.RPAREN)
                        if tok is not None:
                            child = self.compound_stmt()
                            if child is not None:
                                AST.addChild(child)
                                return AST
    
        self.error(False)
        if self.tokenTypes[self.pos] == TokenType.LKEY:
            child = self.compound_stmt()
            if child is not None:
                AST.addChild(child)
                return AST
        return None

    #7.	params --> param-list | void
    def params(self):
        posA = self.pos
        child = self.param_list()
        if child is not None:
            return child
        posMayor = self.pos
        self.pos = posA
        tok = self.match(TokenType.VOID)
        if tok is not None:
            return tok

        self.pos = posMayor
        return None

    #8.	param-list --> param { , param}
    def param_list(self):
        AST = Tree_Node("param_list")
        child = self.param()
        if child is not None:
            AST.addChild(child)
        else:
            return None
        
        while self.pos < self.lenE-1:
            tok = self.match(TokenType.COMA)
            if tok is not None:
                child = self.param()
                if child is not None:
                    AST.addChild(child)
                else:
                    return None
            else:
                break
        return AST

    #9.	param --> type-specifier ID [ [ ] ]
    def param(self):
        child = self.type_specifier()
        AST = child
        if child is not None:
            tok = self.match(TokenType.ID)
            if tok is not None: 
                AST.addChild(tok)
                tok = self.match(TokenType.LBRACKET)
                if tok is None:
                    return AST
                else:
                    #AST.addChild(tok)
                    tok = self.match(TokenType.RBRACKET)
                    if tok is not None:
                        AST.addChild(Tree_Node("arr_statement"))
                        return AST

        return None

    #10. compound-stmt --> { local-declarations statement-list }
    def compound_stmt(self):
        AST = Tree_Node("compound_stmt")
        tok = self.match(TokenType.LKEY)
        if tok is not None: 
            child = self.local_declarations()
            if child is not None:
                AST.addChild(child)
                child = self.statement_list()
                if child is not None:
                    AST.addChild(child)
                    tok = self.match(TokenType.RKEY)
                    if tok is not None: 
                        return AST
        return None
    #11. local-declarations --> { var-declaration }
    def local_declarations(self):
        AST = Tree_Node("local_declarations")
        while self.pos < self.lenE-1:
            posA = self.pos
            child = self.var_declaration()
            if child is not None:
                AST.addChild(child)
            else:
                save = self.pos
                self.pos = posA
                
                tok = self.match(TokenType.RKEY)
                if tok is not None:
                    self.pos = posA
                    return AST

                if self.tokenTypes[self.pos] == TokenType.ID or self.tokenTypes[self.pos] == TokenType.LPAREN  or self.tokenTypes[self.pos] == TokenType.NUM or self.tokenTypes[self.pos] == TokenType.LKEY or self.tokenTypes[self.pos] == TokenType.IF or self.tokenTypes[self.pos] == TokenType.WHILE or self.tokenTypes[self.pos] == TokenType.RETURN:
                    self.pos = posA
                    return AST
                else:
                    self.pos = save
                    self.error(True)
        
        return AST

    #12. statement-list --> { statement }
    def statement_list(self):
        AST = Tree_Node("statement_list")
        while self.pos < self.lenE-1:
            posA = self.pos
            child = self.statement()
            if child is not None:
                AST.addChild(child)
            else:
                if self.tokenTypes[posA] == TokenType.RKEY:
                    return AST
                self.error(True)   
           
                
        return AST
    
    #13. statement --> expression-stmt | compound-stmt | selection-stmt | iteration-stmt | return-stmt
    def statement(self):
        posA = self.pos
        child = self.expression_stmt()
        if child is not None:
            return child
        
        posMayor = self.pos
        self.pos = posA

        child = self.compound_stmt()
        if child is not None:
            return child

        if posMayor < self.pos:
            posMayor = self.pos

        self.pos = posA
        child = self.selection_stmt()
        if child is not None:
            return child

        if posMayor < self.pos:
            posMayor = self.pos

        self.pos = posA
        child = self.iteration_stmt()
        if child is not None:
            return child

        if posMayor < self.pos:
            posMayor = self.pos

        self.pos = posA
        child = self.return_stmt()
        if child is not None:
            return child

        if posMayor < self.pos:
            posMayor = self.pos
        
        self.pos = posMayor
        
        return None
    #14. expression-stmt --> [expression] ; 
    def expression_stmt(self):
        child = self.expression()
        AST = child
        if child is not None: 
            tok = self.match(TokenType.SEMICOLON)
            if tok is not None: 
                return AST
        
        return None
    
    #15. selection-stmt --> if ( expression ) statement [else statement]
    def selection_stmt(self):
        
        tok = self.match(TokenType.IF)
        AST = tok
        if tok is not None: 
            tok = self.match(TokenType.LPAREN)
            if tok is not None: 
                child = self.expression()
                if child is not None: 
                    AST.addChild(child)
                    tok = self.match(TokenType.RPAREN)
                    if tok is not None: 
                        child = self.statement()
                        if child is not None:
                            AST.addChild(child)
                            tok = self.match(TokenType.ELSE)
                            if tok is not None:
                                AST.addChild(tok)
                                child = self.statement()
                                if child is not None:
                                    AST.addChild(child)
                                    return AST
                            else:
                                return AST
        return None

    #16. iteration-stmt --> while ( expression ) statement
    def iteration_stmt(self):
        AST = Tree_Node("iteration_stmt")
        tok = self.match(TokenType.WHILE)
        if tok is not None: 
            AST.addChild(tok)
            tok = self.match(TokenType.LPAREN)
            if tok is not None: 
                child = self.expression()
                if child is not None: 
                    AST.addChild(child)
                    tok = self.match(TokenType.RPAREN)
                    if tok is not None: 
                        child = self.statement()
                        if child is not None:
                            AST.addChild(child)
                            return AST
        return None
    
    #17. return-stmt --> return [ expression ];  
    def return_stmt (self):

        tok = self.match(TokenType.RETURN)
        AST = tok
        if tok is None:
            return None


        posA = self.pos
        child = self.expression()
        if child is not None: 
            AST.addChild(child)
            
            tok = self.match(TokenType.SEMICOLON)
            if tok is not None: 
                return AST
        
        posMayor = self.pos
        self.pos = posA

        tok = self.match(TokenType.SEMICOLON)
        if tok is not None: 
            return AST

        if posMayor < self.pos:
            posMayor = self.pos
        
        self.pos = posMayor
        
        return None   


    #18. expression --> { var =} simple-expression 
    def expression(self):
        AST = None

        while self.pos < self.lenE-1:
            posA = self.pos

            child = self.var()
            if child is not None:
                tok = self.match(TokenType.EQUALS)
                if tok is not None: 

                    if AST is None:
                        AST = tok
                    AST.addChild(child)
                else:
                    self.pos = posA
                    break
            else:
                self.pos = posA
                break

    
        child = self.simple_expression()
        if AST is None:
            return child    
        if child is not None:
            AST.addChild(child)
            return AST

        return None

    #19. var --> ID [ [ expression ] ]
    def var(self):
        tok = self.match(TokenType.ID)
        AST = tok
        if tok is not None: 
            posA = self.pos
            tok = self.match(TokenType.LBRACKET)
            if tok is not None:
                child = self.expression()
                if child is not None:
                    AST.addChild(child)
                    tok = self.match(TokenType.RBRACKET)
                    if tok is not None: 
                        return AST
            else:
                self.pos = posA
                return AST
        
        return None

    #20. simple-expression --> additive-expression [ relop additive-expression ]
    def simple_expression(self):
        child = self.additive_expression()
        AST = child
        if child is not None: 
            posA = self.pos
            operator = self.relop()
            if operator is not None:
                operator.addChild(AST)
                child = self.additive_expression()
                if child is not None:
                    operator.addChild(child)
                    return operator
            else:
                self.pos = posA
                return AST
        return None
    
    #21. relop --> <= | < | > | >= | == | !=
    def relop(self):
        tok = self.match(TokenType.SETHAN)
        if tok is not None: 
            return tok
        
        tok = self.match(TokenType.STHAN)
        if tok is not None: 
            return tok

        tok = self.match(TokenType.BTHAN)
        if tok is not None: 
            return tok

        tok = self.match(TokenType.BETHAN)
        if tok is not None: 
            return tok

        tok = self.match(TokenType.COMPAREEQUALS)
        if tok is not None: 
            return tok
        
        tok = self.match(TokenType.NOTEQUALS)
        if tok is not None: 
            return tok

        return None

    #22. additive-expression --> term { addop term }
    def additive_expression(self):
        AST = None

        child = self.term()
        if child is None:
            return None
        
        while self.pos < self.lenE-1:
            operator = self.addop()

            if operator is not None:
                if AST is None:
                    AST = operator
                    AST.addChild(child)
                else:
                    AST_Child = AST
                    AST = operator
                    AST.addChild(AST_Child)

                child = self.term()
                if child is not None:
                    AST.addChild(child)
                else:
                    return None
            else:
                break
        
        if AST is None:
            return child

        return AST 
    #23. addop --> + | -
    def addop(self):
        tok = self.match(TokenType.PLUS)
        if tok is not None: 
            return tok
        tok = self.match(TokenType.MINUS)
        if tok is not None: 
            return tok
        return None

    #24. term --> factor { mulop factor }
    def term(self):
        AST = None
        child = self.factor()
        if child is None:
            return None
        
        while self.pos < self.lenE-1:
            operator = self.mulop()
            if operator is not None:
                if AST is None:
                    AST = operator
                    AST.addChild(child)
                else:
                    AST_Child = AST
                    AST = operator
                    AST.addChild(AST_Child)

                child = self.factor()
                if child is not None:
                    AST.addChild(child)
                else:
                    return None
            else:
                break

        if AST is None:
            AST = child
            
        return AST 
    #25. mulop --> * | /
    def mulop(self):
        tok = self.match(TokenType.TIMES)
        if tok is not None: 
            return tok
        tok = self.match(TokenType.DIVIDE)
        if tok is not None: 
            return tok
        return None

    #26. factor --> ( expression ) | var | call | NUM
    def factor(self):
        posA = self.pos
        tok = self.match(TokenType.LPAREN)
        if tok is not None:
            child = self.expression()
            if child is not None:
                tok = self.match(TokenType.RPAREN)
                if tok is not None:
                    return child
        posMayor = self.pos

        self.pos = posA
        child = self.call()
        if child is not None:
            return child

        if posMayor < self.pos:
            posMayor = self.pos

        self.pos = posA
        child = self.var()
        if child is not None:
            return child

        if posMayor < self.pos:
            posMayor = self.pos
        

        self.pos = posA
        tok = self.match(TokenType.NUM)   
        if tok is not None:
            return tok

        if posMayor < self.pos:
            posMayor = self.pos
        self.pos = posMayor
        
        return None

    #27. call --> ID ( args )
    def call(self):
        tok = self.match(TokenType.ID)
        AST = tok
        if tok is not None:
            tok = self.match(TokenType.LPAREN)
            if tok is not None:
                child = self.args()
                if child is not None:
                    AST.addChild(child)
                    tok = self.match(TokenType.RPAREN)
                    if tok is not None:
                        return AST

    #28. args --> arg-list | empty
    def args(self):
        AST = Tree_Node("args_statement")
        posA = self.pos
        tok = self.match(TokenType.RPAREN)
        if tok is not None:
            self.pos -= 1
            return AST

        child = self.arg_list()
        if child is not None:
            AST.addChild(child)
            return AST
        else:
            self.error(False, False)

        return AST

    #29. arg-list --> expression { , expression }
    def arg_list(self):
        AST = Tree_Node("arg_list")
        child = self.expression()
        if child is not None:
            AST.addChild(child)
        else:
            return None
        
        while self.pos < self.lenE-1:
            tok = self.match(TokenType.COMA)
            if tok is not None:
                child = self.expression()
                if child is not None:
                    AST.addChild(child)
                else:
                    return None
            else:
                break
        return AST


    def match(self,car):
        if self.lenE>self.pos and self.tokenTypes[self.pos] == car:
            self.pos += 1
            return Tree_Node(self.tokens[self.pos-1])
        return None

    def error(self, move = True, pr = True):
        self.err = 1

        if pr:
            errorLine = self.getErrorLine()
            print("Sintax error in line",errorLine,":")
            posicion = self.posiciones[self.pos]

            print(self.linesSizes[errorLine-1][0])
            offset = posicion-self.linesSizes[errorLine-1][1]-errorLine+1
            print(' ' * offset +"^")

        for i in range(self.pos, len(self.tokens)):
            if self.tokenTypes[i] == TokenType.SEMICOLON or self.tokenTypes[i] == TokenType.ENDFILE or self.tokenTypes[i] == TokenType.LKEY or self.tokenTypes[i] == TokenType.RKEY:
                if move:
                    self.pos = i+1
                else:
                    self.pos = i
                break

    def getErrorLine(self):
        return self.lineas[self.pos-1]
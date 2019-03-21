from globalTypes import *
import lex as lex
linesSizes = []

#Palabras reservadas utilizadas por lex
reserved = {
    'else' : 'ELSE',
    'if' : 'IF',
    'int' : 'INT',
    'return' : 'RETURN',
    'void' : 'VOID',
    'while' : 'WHILE',
}

#tokens de lex
tokens = [
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'STHAN',
    'SETHAN',
    'BTHAN',
    'BETHAN',
    'COMPAREEQUALS',
    'NOTEQUALS',
    'EQUALS',
    'SEMICOLON',
    'COMA',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LKEY',
    'RKEY',
    'ID',
    'NUM',
    'COMMENT',
    'ENDFILE'
    ]+ list(reserved.values())

# ER de los tokens de lex
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_STHAN  = r'<'
t_SETHAN  = r'<='
t_BTHAN  = r'>'
t_BETHAN  = r'>='
t_COMPAREEQUALS  = r'=='
t_NOTEQUALS = r'!='
t_EQUALS  = r'='
t_SEMICOLON  = r';'
t_COMA  = r','
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACKET  = r'\['
t_RBRACKET  = r'\]'
t_LKEY  = r'\{'
t_RKEY  = r'\}'
t_ENDFILE = r"\$"

#Para poder detectar los IDs
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    #r'[a-zA-Z][a-zA-Z]*(?![0-9])'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

#Para poder detectar los comentarios
def t_COMMENT(t):
    r'/\*/*([^*/]/*|\*)*\*/'
    t.lexer.lineno += t.value.count("\n")

#Para poder detectar los numeros
def t_NUM(t):
    r'\d+'
    #r'\d+(?![0-9a-zA-Z])'
    t.value = int(t.value)
    return t
    
# Caracteres que se ignoran
t_ignore = " \t"

#Cuando encuentra una nueva linea 
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

#Si ocurre un error al detectar el token se imprime el caracter de error y se ubica en que linea se encuentra   
def t_error(t):
    print("Ilegal character in line",t.lineno,":")
    print(linesSizes[t.lineno-1][0])
    offset = t.lexpos-linesSizes[t.lineno-1][1]-t.lineno+1
    print(' ' * offset +"^")

    """movimientos = 0
    for i in range(len(t.value)):
        if t.value[i] is ' ' or t.value[i] is '\n' or t.value[i] is '$':
            movimientos = i
            break"""
    
    t.lexer.skip(1)
    t.type = "ERROR"
    t.value = t.value[0]

#Inicializar las variables globales
def globales(prog, pos, long):
    global programa
    global posicion
    global progLong
    global lexer
    global nline
    global linesSizes
    global aline


    programa = prog
    posicion = pos
    progLong = long
    lexer = lex.lex()
    lexer.input(prog)
    aline = 1

    #utilizado para ubicar los errores en una linea especifica
    #prog2 = prog[:-1]
    lines = prog.split("\n")
    
    nline = 0
    for line in lines:
        linesSizes.append((line,nline))
        nline += len(line)

#Detecta los tokens y los regresa
def getToken(imprime = True):
    global posicion
    global aline
    tok = lexer.token()
    posicion = tok.lexpos
    aline = tok.lineno
    token = TokenType[tok.type]
    if imprime:
        print('('+token.name+', "'+str(tok.value)+'")')
    return token,tok.value
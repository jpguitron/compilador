from globalTypes import *
from lexer import *

f = open('sample.c‐', 'r')
programa = f.read()    
progLong = len(programa)   
programa = programa + '$'   
posicion = 0   

globales(programa, posicion, progLong)
token, tokenString = getToken(False)
print(token, tokenString)

while (token != TokenType.ENDFILE):
    print(token, tokenString)
    token, tokenString = getToken(False)


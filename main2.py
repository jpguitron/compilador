

posA = 0
pos = 0
lenE = 0


def E(p):
    a =[]
    boolean = T(a)
    if lenE>pos and match("opsuma"):
        p.append("opsuma")
        p.append(boolean)
        boolean = E(a)
        p.append(boolean)
    else:
        return boolean
    return p

def T(p):
    global pos
    global posA
    posA = pos
    a = []
    boolean = T1(a)

    if not boolean:
        pos = posA 
        boolean2 = T2(a)
        return boolean2
    else:
        return boolean    


def T1(p):
    if lenE>pos and match("num"):
        boolean = "num"
    else:
        return False

    if lenE>pos and match("opmult"):
        a = []
        p.append("opmult")
        p.append("num")
        boolean = E(a)
        p.append(boolean)    
    else:
        return boolean
    return p

def T2(p):
    a = []
    if match("lParen"):
        boolean = E(a)
        if match("rParen"):
            return boolean
    return False

def match(car):
    global pos
    global entrada
    global tokens
    if lenE>pos and entrada[pos] == car:
        pos += 1
        return True
    return False


tokens = ["lParen","rParen","num","opmult","opsuma"]
#entrada = ["num","opmult","num","opsuma","num"]
#entrada = ["num","opmult"]
entrada = ["num","opmult","lParen","lParen","num","opsuma","num","rParen","opsuma","num","rParen"]
p=[]
lenE = len(entrada)
tokenA = entrada[pos]
print(E(p))


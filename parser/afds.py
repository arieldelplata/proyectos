def afd_id(cadena):
    estados_sin_trampa = [0, 1]
    estado_final = [1]
    estado_no_aceptado = [0]
    estado_trampa = 't'
    estado = 0
    caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3',
                '4', '5', '6', '7', '8', '9']
    delta = {
    0: {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1,
        'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1,
        'A': 't', 'B': 't', 'C': 't', 'D': 't', 'E': 't', 'F': 't', 'G': 't', 'H': 't', 'I': 't', 'J': 't', 'K': 't',
        'L': 't', 'M': 't', 'N': 't', 'O': 't', 'P': 't', 'Q': 't', 'R': 't', 'S': 't', 'T': 't', 'U': 't', 'V': 't',
        'W': 't', 'X': 't', 'Y': 't', 'Z': 't', '0': 't', '1': 't', '2': 't', '3': 't', '4': 't', '5': 't', '6': 't',
        '7': 't', '8': 't', '9': 't'},
    1: {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1,
        'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1,
        'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1, 'H': 1, 'I': 1, 'J': 1, 'K': 1, 'L': 1, 'M': 1,
        'N': 1, 'O': 1, 'P': 1, 'Q': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 1, 'W': 1, 'X': 1, 'Y': 1, 'Z': 1,
        '0': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1},
    't': {'a': 't', 'b': 't', 'c': 't', 'd': 't', 'e': 't', 'f': 't', 'g': 't', 'h': 't', 'i': 't', 'j': 't', 'k': 't',
        'l': 't', 'm': 't', 'n': 't', 'o': 't', 'p': 't', 'q': 't', 'r': 't', 's': 't', 't': 't', 'u': 't', 'v': 't',
        'w': 't', 'x': 't', 'y': 't', 'z': 't', 'A': 't', 'B': 't', 'C': 't', 'D': 't', 'E': 't', 'F': 't', 'G': 't',
        'H': 't', 'I': 't', 'J': 't', 'K': 't', 'L': 't', 'M': 't', 'N': 't', 'O': 't', 'P': 't', 'Q': 't', 'R': 't',
        'S': 't', 'T': 't', 'U': 't', 'V': 't', 'W': 't', 'X': 't', 'Y': 't', 'Z': 't', '0': 't', '1': 't', '2': 't',
        '3': 't', '4': 't', '5': 't', '6': 't', '7': 't', '8': 't', '9': 't'}
    }

    for caracter in cadena:
        if (estado in estados_sin_trampa) and (caracter in caracteres):
            estado = delta[estado][caracter]
        elif (estado == 't') or not(caracter in caracteres):
            estado = 't'
            break
    if estado in estado_final:
            #estado_final=estado_final
        estado_final='aceptado'
    elif estado == estado_trampa:
            #estado_final=estado_trampa
        estado_final='trampa'
    elif estado in estado_no_aceptado: 
        #estado_final=estado_no_final
        estado_final='no aceptado'
    return estado_final
def afd_num(cadena):
    estados_sin_trampa = [0, 1]
    estado_final = [1]
    estados_no_aceptados = [0]
    estado_trampa = 't'
    estado = 0
    caracteres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    delta = {
    0: {'0': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1},
    1: {'0': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1},
    't': {'0': 't', '1': 't', '2': 't', '3': 't', '4': 't', '5': 't', '6': 't', '7': 't', '8': 't', '9': 't'}
    }

    for caracter in cadena:
        if (estado in estados_sin_trampa) and (caracter in caracteres):
            estado = delta[estado][caracter]
        elif (estado == 't') or not(caracter in caracteres):
            estado = 't'
            break
    if estado in estado_final:
            #estado_final=estado_final
        estado_final='aceptado'
    elif estado == estado_trampa:
            #estado_final=estado_trampa
        estado_final='trampa'
    elif estado in estados_no_aceptados: 
        #estado_final=estado_no_final
        estado_final='no aceptado'
    return estado_final

        
def afd_finalprograma (cadena):
    estado_no_final=[0]
    estado_final=[1]
    estado_trampa='t' 
    estado=0
    delta={
        0:{'#':1},
        1:{'#':'t'},
        't':{'#':'t'}
        
    }
    for caracter in cadena:
        if caracter in delta[estado]:
            estado = delta[estado][caracter]
        else:
            estado = estado_trampa
            break
    if estado in estado_final:
            #estado_final=estado_final
        estado_final='aceptado'
    elif estado == estado_trampa:
            #estado_final=estado_trampa
        estado_final='trampa'
    elif estado in estado_no_final: 
        #estado_final=estado_no_final
        estado_final='no aceptado'
    return estado_final
         
def afd_const(cadena):
    estado_no_final=[0,1,2,3,4]
    estado_final=[5]
    estado_trampa='t' 
    estado=0
    delta={
        0: {chr(c): 1 if ('c'== chr(c) ) else estado_trampa for c in range(128)},
        1: {chr(c): 2 if ('o'== chr(c) ) else estado_trampa for c in range(128)},
        2: {chr(c): 3 if ('n'==chr(c) ) else estado_trampa for c in range(128)},
        3: {chr(c): 4 if ('s'== chr(c) ) else estado_trampa for c in range(128)},
        4: {chr(c): 5 if ('t'== chr(c) ) else estado_trampa for c in range(128)},
    }
    for caracter in cadena:
        if estado in delta and caracter in delta[estado]:
            estado = delta[estado][caracter]
        else:
            estado = estado_trampa
            break
    if estado in estado_final:
            #estado_final=estado_final
        estado_final='aceptado'
    elif estado == estado_trampa:
            #estado_final=estado_trampa
        estado_final='trampa'
    elif estado in estado_no_final: 
        #estado_final=estado_no_final
        estado_final='no aceptado'
    return estado_final
        
def afd_var(cadena):
    estado_trampa='t' 
    estado=0
    estado_no_final=[0,1,2]
    estado_final=[3]
    delta={
        0: {chr(c): 1 if ('v'== chr(c) ) else estado_trampa for c in range(128)},
        1: {chr(c): 2 if ('a'== chr(c) ) else estado_trampa for c in range(128)},
        2: {chr(c): 3 if ('r'==chr(c) ) else estado_trampa for c in range(128)},
    }
    for caracter in cadena:
        if estado in delta and caracter in delta[estado]:
            estado = delta[estado][caracter]
        else:
            estado = estado_trampa
            break
    if estado in estado_final:
            #estado_final=estado_final
        estado_final='aceptado'
    elif estado == estado_trampa:
            #estado_final=estado_trampa
        estado_final='trampa'
    elif estado in estado_no_final: 
        #estado_final=estado_no_final
        estado_final='no aceptado'
    return estado_final
    
def afd_coma(cadena):
    estado_trampa='t' 
    estado=0
    estado_no_final=[0]
    estado_final=[1]
    delta={
        0: {chr(c): 1 if (','== chr(c) ) else estado_trampa for c in range(128)},
    }
    for caracter in cadena:
        if estado in delta and caracter in delta[estado]:
            estado = delta[estado][caracter]
        else:
            estado = estado_trampa
            break
    if estado in estado_final:
            #estado_final=estado_final
        estado_final='aceptado'
    elif estado == estado_trampa:
            #estado_final=estado_trampa
        estado_final='trampa'
    elif estado in estado_no_final: 
        #estado_final=estado_no_final
        estado_final='no aceptado'
    return estado_final
       
def afd_puntocoma (cadena):
    estado_trampa='t' 
    estado=0
    estado_no_final=[0]
    estado_final=[1]
    delta={
        0: {chr(c): 1 if (';'== chr(c) ) else estado_trampa for c in range(128)},
    }
    for caracter in cadena:
        if estado in delta and caracter in delta[estado]:
            estado = delta[estado][caracter]
        else:
            estado = estado_trampa
            break
    if estado in estado_final:
            #estado_final=estado_final
        estado_final='aceptado'
    elif estado == estado_trampa:
            #estado_final=estado_trampa
        estado_final='trampa'
    elif estado in estado_no_final: 
        #estado_final=estado_no_final
        estado_final='no aceptado'
    return estado_final
def afd_assign(cadena):
    estado_trampa='t' 
    estado=0
    estado_no_final=[0,1]
    estado_final=[2]
    delta={
        0: {chr(c): 1 if (':'== chr(c) ) else estado_trampa for c in range(128)},
        1: {chr(c): 2 if ('='== chr(c) ) else estado_trampa for c in range(128)},
    }
    for caracter in cadena:
        if estado in delta and caracter in delta[estado]:
            estado = delta[estado][caracter]
        else:
            estado = estado_trampa
            break
    if estado in estado_final:
            #estado_final=estado_final
        estado_final='aceptado'
    elif estado == estado_trampa:
            #estado_final=estado_trampa
        estado_final='trampa'
    elif estado in estado_no_final: 
        #estado_final=estado_no_final
        estado_final='no aceptado'
    return estado_final
        
def afd_call (cadena):
    estado_no_final=[0,1,2,3]
    estado_final=[4]
    estado_trampa='t' 
    estado=0
    delta={
        0: {chr(c): 1 if ('c'== chr(c) ) else estado_trampa for c in range(128)},
        1: {chr(c): 2 if ('a'== chr(c) ) else estado_trampa for c in range(128)},
        2: {chr(c): 3 if ('l'==chr(c) ) else estado_trampa for c in range(128)},
        3: {chr(c): 4 if ('l'== chr(c) ) else estado_trampa for c in range(128)},
        
    }
    for caracter in cadena:
        if estado in delta and caracter in delta[estado]:
            estado = delta[estado][caracter]
        else:
            estado = estado_trampa
            break
    if estado in estado_final:
            #estado_final=estado_final
        estado_final='aceptado'
    elif estado == estado_trampa:
            #estado_final=estado_trampa
        estado_final='trampa'
    elif estado in estado_no_final: 
        #estado_final=estado_no_final
        estado_final='no aceptado'
    return estado_final
        
def afd_begin(cadena):
    estado_no_final=[0,1,2,3,4]
    estado_final=[5]
    estado_trampa='t' 
    estado=0
    delta={
        0: {chr(c): 1 if ('b'== chr(c) ) else estado_trampa for c in range(128)},
        1: {chr(c): 2 if ('e'== chr(c) ) else estado_trampa for c in range(128)},
        2: {chr(c): 3 if ('g'==chr(c) ) else estado_trampa for c in range(128)},
        3: {chr(c): 4 if ('i'== chr(c) ) else estado_trampa for c in range(128)},
        4: {chr(c): 5 if ('n'== chr(c) ) else estado_trampa for c in range(128)},
    }
    for caracter in cadena:
        if estado in delta and caracter in delta[estado]:
            estado = delta[estado][caracter]
        else:
            estado = estado_trampa
            break
    if estado in estado_final:
            #estado_final=estado_final
        estado_final='aceptado'
    elif estado == estado_trampa:
            #estado_final=estado_trampa
        estado_final='trampa'
    elif estado in estado_no_final: 
        #estado_final=estado_no_final
        estado_final='no aceptado'
    return estado_final
        
def afd_end (cadena):
    estado_no_final=[0,1,2]
    estado_final=[3]
    estado_trampa='t' 
    estado=0
    delta={
        0: {chr(c): 1 if ('e'== chr(c) ) else estado_trampa for c in range(128)},
        1: {chr(c): 2 if ('n'== chr(c) ) else estado_trampa for c in range(128)},
        2: {chr(c): 3 if ('d'==chr(c) ) else estado_trampa for c in range(128)},
        
    }
    for caracter in cadena:
        if estado in delta and caracter in delta[estado]:
            estado = delta[estado][caracter]
        else:
            estado = estado_trampa
            break
    if estado in estado_final:
            #estado_final=estado_final
        estado_final='aceptado'
    elif estado == estado_trampa:
            #estado_final=estado_trampa
        estado_final='trampa'
    elif estado in estado_no_final: 
        #estado_final=estado_no_final
        estado_final='no aceptado'
    return estado_final
        
def afd_if (cadena):
    estado_no_final=[0,1]
    estado_final=[2]
    estado_trampa='t' 
    estado=0
    delta={
        0: {chr(c): 1 if ('i'== chr(c) ) else estado_trampa for c in range(128)},
        1: {chr(c): 2 if ('f'== chr(c) ) else estado_trampa for c in range(128)},
        
    }
    for caracter in cadena:
        if estado in delta and caracter in delta[estado]:
            estado = delta[estado][caracter]
        else:
            estado = estado_trampa
            break
    if estado in estado_final:
            #estado_final=estado_final
        estado_final='aceptado'
    elif estado == estado_trampa:
            #estado_final=estado_trampa
        estado_final='trampa'
    elif estado in estado_no_final: 
        #estado_final=estado_no_final
        estado_final='no aceptado'
    return estado_final
        
def afd_then (cadena):
    estado_no_final=[0,1,2,3]
    estado_final=[4]
    estado_trampa='t' 
    estado=0
    delta={
        0: {chr(c): 1 if ('t'== chr(c) ) else estado_trampa for c in range(128)},
        1: {chr(c): 2 if ('h'== chr(c) ) else estado_trampa for c in range(128)},
        2: {chr(c): 3 if ('e'==chr(c) ) else estado_trampa for c in range(128)},
        3: {chr(c): 4 if ('n'== chr(c) ) else estado_trampa for c in range(128)},
       
    }
    for caracter in cadena:
        if estado in delta and caracter in delta[estado]:
            estado = delta[estado][caracter]
        else:
            estado = estado_trampa
            break
    if estado in estado_final:
            #estado_final=estado_final
        estado_final='aceptado'
    elif estado == estado_trampa:
            #estado_final=estado_trampa
        estado_final='trampa'
    elif estado in estado_no_final: 
        #estado_final=estado_no_final
        estado_final='no aceptado'
    return estado_final
def afd_while (cadena):
    estado_no_final=[0,1,2,3,4]
    estado_final=[5]
    estado_trampa='t' 
    estado=0
    delta={
        0: {chr(c): 1 if ('w'== chr(c) ) else estado_trampa for c in range(128)},
        1: {chr(c): 2 if ('h'== chr(c) ) else estado_trampa for c in range(128)},
        2: {chr(c): 3 if ('i'==chr(c) ) else estado_trampa for c in range(128)},
        3: {chr(c): 4 if ('l'== chr(c) ) else estado_trampa for c in range(128)},
        4: {chr(c): 5 if ('e'== chr(c) ) else estado_trampa for c in range(128)},
    }
    for caracter in cadena:
        if estado in delta and caracter in delta[estado]:
            estado = delta[estado][caracter]
        else:
            estado = estado_trampa
            break
    if estado in estado_final:
            #estado_final=estado_final
        estado_final='aceptado'
    elif estado == estado_trampa:
            #estado_final=estado_trampa
        estado_final='trampa'
    elif estado in estado_no_final: 
        #estado_final=estado_no_final
        estado_final='no aceptado'
    return estado_final
        
def afd_do (cadena):
    estado_no_final=[0,1]
    estado_final=[2]
    estado_trampa='t' 
    estado=0
    delta={
        0: {chr(c): 1 if ('d'== chr(c) ) else estado_trampa for c in range(128)},
        1: {chr(c): 2 if ('o'== chr(c) ) else estado_trampa for c in range(128)},
        
    }
    for caracter in cadena:
        if estado in delta and caracter in delta[estado]:
            estado = delta[estado][caracter]
        else:
            estado = estado_trampa
            break
    if estado in estado_final:
            #estado_final=estado_final
        estado_final='aceptado'
    elif estado == estado_trampa:
            #estado_final=estado_trampa
        estado_final='trampa'
    elif estado in estado_no_final: 
        #estado_final=estado_no_final
        estado_final='no aceptado'
    return estado_final
        
def afd_odd (cadena):
    estado_no_final=[0,1,2]
    estado_final=[3]
    estado_trampa='t' 
    estado=0
    delta={
        0: {chr(c): 1 if ('o'== chr(c) ) else estado_trampa for c in range(128)},
        1: {chr(c): 2 if ('d'== chr(c) ) else estado_trampa for c in range(128)},
        2: {chr(c): 3 if ('d'==chr(c) ) else estado_trampa for c in range(128)},
       
    }
    for caracter in cadena:
        if estado in delta and caracter in delta[estado]:
            estado = delta[estado][caracter]
        else:
            estado = estado_trampa
            break
    if estado in estado_final:
            #estado_final=estado_final
        estado_final='aceptado'
    elif estado == estado_trampa:
            #estado_final=estado_trampa
        estado_final='trampa'
    elif estado in estado_no_final: 
        #estado_final=estado_no_final
        estado_final='no aceptado'
    return estado_final
        
def afd_comparison(cadena):
    estados_sin_trampa = [0, 1, 2, 3]
    estado_final = [1, 2, 3]
    estado_no_final = [0]
    estado_trampa = 't'
    estado = 0
    caracteres = ['<', '>', '=']
    delta = {
    0: {'<': 1, '>': 2, '=': 3},
    1: {'<': 't', '>': 3, '=': 3},
    2: {'<': 't', '>': 't', '=': 3},
    3: {'<': 't', '>': 't', '=': 't'},
    't': {'<': 't', '>': 't', '=': 't'}
    }

    for caracter in cadena:
        if (estado in estados_sin_trampa) and (caracter in caracteres):
            estado = delta[estado][caracter]
        elif (estado == 't') or not(caracter in caracteres):
            estado = 't'
            break
    if estado in estado_final:
            #estado_final=estado_final
        estado_final='aceptado'
    elif estado == estado_trampa:
            #estado_final=estado_trampa
        estado_final='trampa'
    elif estado in estado_no_final: 
        #estado_final=estado_no_final
        estado_final='no aceptado'
    return estado_final
        
def afd_operation(cadena):
    estados_sin_trampa = [0, 1]
    estados_aceptados = [1]
    estados_no_aceptados = [0]
    estado_trampa = 't'
    estado = 0
    caracteres = ['+', '-']
    delta = {
    0: {'+': 1, '-': 1},
    1: {'+': 't', '-': 't'},
    't': {'+': 't', '-': 't'}
    } 

    for caracter in cadena:
        if (estado in estados_sin_trampa) and (caracter in caracteres):
            estado = delta[estado][caracter]
        elif (estado == 't') or not(caracter in caracteres):
            estado = 't'
            break

    if estado in estados_aceptados:
        estado_final = 'aceptado'
    elif estado in estados_no_aceptados:
        estado_final = 'no aceptado'
    elif estado == estado_trampa:
        estado_final = 'trampa'

    return estado_final
        
def afd_division(cadena):
    estado_no_final=[0]
    estado_final=[1]
    estado_trampa='t' 
    estado=0
    delta={
        0: {chr(c): 1 if ('/'== chr(c) ) else estado_trampa for c in range(128)},
       
       
    }
    for caracter in cadena:
        if estado in delta and caracter in delta[estado]:
            estado = delta[estado][caracter]
        else:
            estado = estado_trampa
            break
    if estado in estado_final:
            #estado_final=estado_final
        estado_final='aceptado'
    elif estado == estado_trampa:
            #estado_final=estado_trampa
        estado_final='trampa'
    elif estado in estado_no_final: 
        #estado_final=estado_no_final
        estado_final='no aceptado'
    return estado_final
def afd_multiplicacion(cadena):
    estado_no_final=[0]
    estado_final=[1]
    estado_trampa='t' 
    estado=0
    delta={
        0: {chr(c): 1 if ('*'== chr(c) ) else estado_trampa for c in range(128)},
    }
    for caracter in cadena:
        if estado in delta and caracter in delta[estado]:
            estado = delta[estado][caracter]
        else:
            estado = estado_trampa
            break
    if estado in estado_final:
            #estado_final=estado_final
        estado_final='aceptado'
    elif estado == estado_trampa:
            #estado_final=estado_trampa
        estado_final='trampa'
    elif estado in estado_no_final: 
        #estado_final=estado_no_final
        estado_final='no aceptado'
    return estado_final
def afd_parentesisini (cadena):
    estado_no_final=[0]
    estado_final=[1]
    estado_trampa='t' 
    estado=0
    delta={
        0: {chr(c): 1 if ('('== chr(c) ) else estado_trampa for c in range(128)},
    }
    for caracter in cadena:
        if estado in delta and caracter in delta[estado]:
            estado = delta[estado][caracter]
        else:
            estado = estado_trampa
            break
    if estado in estado_final:
            #estado_final=estado_final
        estado_final='aceptado'
    elif estado == estado_trampa:
            #estado_final=estado_trampa
        estado_final='trampa'
    elif estado in estado_no_final: 
        #estado_final=estado_no_final
        estado_final='no aceptado'
    return estado_final
def afd_parentesisfin (cadena):
    estado_no_final=[0]
    estado_final=[1]
    estado_trampa='t' 
    estado=0
    delta={
        0: {chr(c): 1 if ( ')'== chr(c) ) else estado_trampa for c in range(128)},
    }
    for caracter in cadena:
        if estado in delta and caracter in delta[estado]:
            estado = delta[estado][caracter]
        else:
            estado = estado_trampa
            break
    if estado in estado_final:
            #estado_final=estado_final
        estado_final='aceptado'
    elif estado == estado_trampa:
            #estado_final=estado_trampa
        estado_final='trampa'
    elif estado in estado_no_final: 
        #estado_final=estado_no_final
        estado_final='no aceptado'
    return estado_final
def afd_procedure (cadena):
    estado_no_final=[0,1,2,3,4,5,6,7,8]
    estado_final=[9]
    estado_trampa='t' 
    estado=0
    delta={
        0: {chr(c): 1 if ('p'== chr(c) ) else estado_trampa for c in range(128)},
        1: {chr(c): 2 if ('r'== chr(c) ) else estado_trampa for c in range(128)},
        2: {chr(c): 3 if ('o'== chr(c) ) else estado_trampa for c in range(128)},
        3: {chr(c): 4 if ('c'== chr(c) ) else estado_trampa for c in range(128)},
        4: {chr(c): 5 if ('e'== chr(c) ) else estado_trampa for c in range(128)},
        5: {chr(c): 6 if ('d'== chr(c) ) else estado_trampa for c in range(128)},
        6: {chr(c): 7 if ('u'== chr(c) ) else estado_trampa for c in range(128)},
        7: {chr(c): 8 if ('r'== chr(c) ) else estado_trampa for c in range(128)},
        8: {chr(c): 9 if ('e'== chr(c) ) else estado_trampa for c in range(128)},
    }
    for caracter in cadena:
        if estado in delta and caracter in delta[estado]:
            estado = delta[estado][caracter]
        else:
            estado = estado_trampa
            break
    if estado in estado_final:
            #estado_final=estado_final
        estado_final='aceptado'
    elif estado == estado_trampa:
            #estado_final=estado_trampa
        estado_final='trampa'
    elif estado in estado_no_final: 
        #estado_final=estado_no_final
        estado_final='no aceptado'
    return estado_final
def afd_espacio(cadena):
    estados_sin_cerrar = [0, 1]
    estado_final = [1]
    estado_no_final = [0]
    estado_trampa = 't'
    estado = 0
    caracteres = [' ', '\n', '\t']
    delta = {
    0: {' ': 1, '\n': 1, '\t': 1},
    1: {' ': 1, '\n': 1, '\t': 1},
    't': {' ': 't', '\n': 't', '\t': 't'}
    }

    for caracter in cadena:
        if (estado in estados_sin_cerrar) and (caracter in caracteres):
            estado = delta[estado][caracter]
        elif (estado == 't') or not(caracter in caracteres):
            estado = 't'
            break
    if estado in estado_final:
            #estado_final=estado_final
        estado_final='aceptado'
    elif estado == estado_trampa:
            #estado_final=estado_trampa
        estado_final='trampa'
    elif estado in estado_no_final: 
        #estado_final=estado_no_final
        estado_final='no aceptado'
    return estado_final

    
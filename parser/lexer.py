from afds import*
TOKENS_POSIBLES = [  
    ("const", afd_const),
    ("var", afd_var),
    ("call", afd_call),
    ("begin", afd_begin),
    ("end", afd_end),
    ("if", afd_if),
    ("then", afd_then),
    ("while", afd_while),
    ("do", afd_do),
    ("odd", afd_odd),
    ("procedure", afd_procedure),
    ("fin programa", afd_finalprograma),
    ("puntoycoma", afd_puntocoma),
    ("coma", afd_coma),
    ("assign", afd_assign),
    ("comparison", afd_comparison),
    ("operation", afd_operation),
    ("multiplicacion", afd_multiplicacion),
    ("division", afd_division),
    ("parentesis inincial", afd_parentesisini),
    ("parentesis final", afd_parentesisfin),
    ("id", afd_id),
    ("num", afd_num),
    ("espacio_blanco", afd_espacio)
]
def lexer(codigoFuente):
    contador = 1
    inicio_del_lexema = 0
    fin_del_lexema = 0
    lexema = ''
    posibles_tokens = []
    posibles_tokens_anterior = []
    tokens = []
    analizar_lexema_mas_grande = False   
    while contador <= len(codigoFuente):
        fin_del_lexema = contador
        lexema = codigoFuente[inicio_del_lexema:fin_del_lexema]                
        for tipo_de_token, afd_token in TOKENS_POSIBLES:        
            simulacion_afd = afd_token(lexema)           
            if simulacion_afd == 'aceptado':
                posibles_tokens.append(tipo_de_token)          
            elif simulacion_afd == 'no aceptado':
                analizar_lexema_mas_grande = True
        if analizar_lexema_mas_grande == True:
            analizar_lexema_mas_grande = False
            posibles_tokens_anterior = posibles_tokens
            posibles_tokens = []
            contador += 1        
        elif len(posibles_tokens) >= 1:
            posibles_tokens_anterior = posibles_tokens
            posibles_tokens = []
            contador += 1        
        elif len(posibles_tokens) == 0 and len(posibles_tokens_anterior) >= 1:
            token = lexema[:-1]
            tipo_de_token_definitivo = posibles_tokens_anterior[0]
            if tipo_de_token_definitivo != 'espacio_blanco':
                tokens.append((tipo_de_token_definitivo, token))            
            inicio_del_lexema = fin_del_lexema - 1          
            posibles_tokens = []
            posibles_tokens_anterior = []
        elif len(posibles_tokens) == 0 and len(posibles_tokens_anterior) == 0:
            print('Error: caracter o expresion invalidos')
            break 
    if len(posibles_tokens_anterior) >= 1:
       token = lexema
       tipo_de_token_definitivo = posibles_tokens_anterior[0]  
       if tipo_de_token_definitivo != 'espacio_blanco': 
            tokens.append((tipo_de_token_definitivo, token))
    
    return tokens
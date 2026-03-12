from lexer import lexer
#tabla de analisis sintactico
tabla = {
    'Program':{
        'const': ['Block','#'], 
        'var' : ['Block', '#'],
        'procedure': ['Block', '#'],
        'begin': ['Block', '#'],
        '#': ['Block', '#'],
        'id': ['Block', '#'],
        'if': ['Block', '#'],
        'while': ['Block', '#'],
        'call':['Block','#'],



    
        
    },
    'Block':{
        'const': ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
        'var' : ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
        'procedure': ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
        'begin': ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
        'id': ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
        'if': ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
        'while': ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
        'call':['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],
        ';' : ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'],                        
        '#': ['ConstDecl', 'VarDecl', 'ProcDecl', 'Statement'] 
    },
    'ConstDecl':{
        'const':   ['const','ConstAssigList'], 
        'var':     [],
        ';':       [],
        'procedure': [],
        'begin': [],
        'id': [],
        'if': [],
        'while': [],
        'call':[],
        '#': [],
    },
    'ConstAssigList':{
        'id':       ['id','=','num','ConstAssigList`'], 
    },
    'ConstAssigList`':{
        ',':       [',','id','=', 'num','ConstAssigList`'], 
    },
    'VarDecl ':{
        'var':      ['var', 'IdList'], 
        'procedure':[], 
        ';':        [],
        '#':        [],
        'begin': [],
        'id': [],
        'if': [],
        'while': [],
        'call':[],
        '#': [],
    },
    'IdList':{
        'id':       ['id', 'IdList`']
    },
    'IdList`':{
        ',':        [',','id', 'IdList`'],
        ';':        []   
    },
    'ProcDecl':{
        'procedure':['procedure', 'Id', 'Block', 'ProcDecl'],
        '#':[],
        ';':[],
        'id':[],
        'call':[],
        'begin':[],
        'if':[],
        'while':[]
    },
    'Statement':{
        'id': ['id',':','=','Expression'],
        'call': ['call','id'],
        'begin': ['begin','StatementList','end'],
        'if': ['if','Condition','then','Statement',','],
        'while': ['while','Condition','do','Statement'],
        '#': [],
        ';': [],
        'end': []
    },
    'StatementList':{
        'id':['Statement', 'StatementList`'],
        'call':['Statement', 'StatementList`'],
        'begin':['Statement', 'StatementList`'],
        'while':['Statement', 'StatementList`'],
        'if':['Statement', 'StatementList`'],
        'end': [],
        ';': ['Statement', 'StatementList`'],
        },

  
    'Condition':{
        '+':['Expression','Relation','Expression'],
        '-':['Expression','Relation','Expression'],
        '(':['Expression','Relation','Expression'],
        'id':['Expression','Relation','Expression'],
        'num':['Expression','Relation','Expression'],
        'odd':['odd','Expression']
    },
    'Expression':{
        '+':['SumOperator','Term','Expression`'],
        '-':['SumOperator','Term','Expression`'],
        '(':['Term','Expression`'],
        'id':['Term','Expression`'],
        'num':['Term','Expression`'],     
    },
    'Expression`':{
        '+':['SumOperator','Term','Expression`'],
        '-':['SumOperator','Term','Expression`'],
        ')':[],
        'then':[],
        'do':[],
        '#':[],
        ';':[],
        '=':[],
        '<>':[],
        '<':[],
        '>':[],
        '<=':[],
        '>=':[],
        'end': [],
    },
    'Term':{
        '(':['Factor', 'Term`'],
        'id':['Factor', 'Term`'],
        'num':['Factor', 'Term`']     
    },
    'Term`':{
        '*':['MultOperator', 'Factor', 'Term`'],
        '/':['MultOperator', 'Factor', 'Term`'],
        '+':[],
        '-':[],
        ';': [],
        '<': [],
        '>': [],
        '<=': [],
        '>=': [],
        '<>': [],
        '=': [],
        '#': [],
        'do': [],
        'then': [],
        'end': [],
        '(': [],
        ')': [],
    },
    'Relation':{
        '=':['='],
        '<>':['<>'],
        '<':['<'],
        '>':['>'],
        '<=':['<='],
        '>=':['>=']         
    },
    'SumOperator':{
        '+':['+'],
        '-':['-']
    },
    'MultOperator':{
        '':['*'], 
        '/':['/']
        },
    'Factor':{
    '(':['(','I',')'],
    'id': ['id'],
    'num': ['num']
    },
}


def parse(tokens):

    pila = ['#','Program'] #pila que contiene simbolos de la gramatica, indice inicializado en primer token
   
    indicador = 0    

    tokens.append(('#', '#'))

    while pila: #cicla solo si hay elementos en la pila, toma el simbolo que se encuentra en el tope y obtiene el token actual. si el token se encuentra en la tabla, brinda la produccion que le corresponde.
        tope = pila.pop()

        token_actual= tokens[indicador][0]

        if (tope, token_actual) in tabla:
            produccion = tabla[(tope, token_actual)]

            if produccion != ['λ']:
                pila.extend(reversed(produccion))

        elif tope == token_actual:
            indicador +=1

        else:
            print(f'Error! No hay produccion correspondiente a {tope} con {token_actual}') #si hay un error de coincidencia entre el tope y el token actual, no se obtiene la produccion y se imprime un error
            return False

    if indicador == len(tokens):
        print('Parseo completo')
        return True

    else:
        print('Error! No llegó al símbolo #')
        return False
    
#ejemplo
codigo_fuente = """
const x = 4, y = 3; 
var resultado; 
procedure multiplicar; 
begin 
    resultado := x * y 
end; 
begin 
    call multiplicar; 
    if resultado > 10 then 
        resultado := resultado * 2 
    else 
        resultado := resultado * 3 
end;
#"""

tokens = lexer(codigo_fuente)
print("Tokens generados:", tokens)
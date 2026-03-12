from lexer import *

print('test I')
cadena='2123 4' 
print (lexer(cadena))
print('PRUEBA FINALIZADA')

print('test II')
cadena='jamon, pan, 234, alan, 232#'
print(lexer(cadena))
print('PRUEBA FINALIZADA')

print ('test III')
cadena='1234#'
print(lexer(cadena))
print('PRUEBA FINALIZADA')

print ('test IV')
cadena=':= ; <> ; > ; < ( )#'
print(lexer(cadena))
print('PRUEBA FINALIZADA')

print ('test V')
cadena='procedure while,do#'
print(lexer(cadena))
print('PRUEBA FINALIZADA')

print ('test VI')
cadena='Error #'
print(lexer(cadena))
print('PRUEBA FINALIZADA')

print ('test VII')
cadena='call ; begin #'
print(lexer(cadena))
print('PRUEBA FINALIZADA')

print ('test VIII')
cadena='end , const;var #'
print(lexer(cadena))
print('PRUEBA FINALIZADA')

print ('test IX')
cadena='call , if then w #'
print(lexer(cadena))
print('PRUEBA FINALIZADA')

print ('test X')
cadena='hernan ponenos un 10 #'
print(lexer(cadena))
print('PRUEBA FINALIZADA')
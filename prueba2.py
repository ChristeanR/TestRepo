numero = input ('Ingresar número:')
try:
    num = int (numero)
    suma = str (num + 5)
    print ('Tu número más 5 es: ' + suma)
except:
    print ('Ingresar valor numérico')

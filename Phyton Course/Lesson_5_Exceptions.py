'''
Created on Mar 28, 2017

@author: Administrator
'''
from platform import _release_filename

def main():
    
# Two ways of handling exceptions
    try:
        fh=open('filename')
    except IOError as e:
        print(e)
    else:
        print("file opened")
        
    try:
        fh=open('filename')
    except: # Este error es generico, no sabemos si el fichero no existe o no tenemos permisos, etc.
        print("file doesn't exist")

# How to extend exceptions
    try:
        fh=open('filename')
    except IOError: # Extendemos el tipo de excepcion
        print("could no open file")
    else:
        for line in fh: print(line.strip())

    try:
        fh=open('filename')
    except IOError as e: # Extendemos el tipo de excepcion
        print(e," : could no open file")
    else:
        for line in fh: print(line.strip())

    try: # Ahora controlamos tambien posibles errores en la salida al meter la output dentro del bloque del try
        fh=open('filename')
        for line in fh: print(line.strip())
    except IOError as e: # Extendemos el tipo de excepcion
        print(e," : could no open file")
  
# How to raise exceptions, create you own exceptions an handle them
def readline(filename): # Definimos una funcion para abrir el fichero y devolver el numero de lineas
    fh=open(filename)
    return fh.readlines()
try:
    for line in readline('filename.txt'): print(line.strip())
except IOError as e:
    print("can't read the file: ",e)


# En la funcion readline1 se incluye que se lance un excepcion definida por el usuario en el caso que el fichero no tenga la ext requerida
def readline1(filename):
    if filename.endswith('.txt'):
        fh=open(filename)
        return fh.readlines()
    else: raise ValueError('Filename must end with .txt')
try:
    for line in readline1('filename'): print(line.strip())
except IOError as e:
    print("can't read the file: ",e)
except ValueError as e:
    print("wrong file extension: ",e)

# Como manejar excepciones multiples y excepciones genericas con un except bloque al final
try:
        fh=open('filename.doc')
        x=1/0
except FileNotFoundError as e:
    print("problem is ",e)
except ZeroDivisionError as e:
        print("ZeroDivision problem ",e)
except:
        print("Generic exception")

# Gestionar excepciones e ignorarlas
try:
    fh=open('filename.bmp')
    print("file has been opened") # no se ejecuta esta linea, porque el fichero no existe, atrapa la excepciones y sale del bloque en el except
except:
    pass

# Como usar el bloque Finally
counter=0
try:
    fh=open('filename.bmp')
    print("file has been opened") # no se ejecuta esta linea, porque el fichero no existe, atrapa la excepciones y sale del bloque en el except
except:
    counter+=1
    print("there was a problem")
    pass
finally: # Se ejecuta siempre, haya o no excepcion; se puede utilizar para gestionar variables como contadores de errores, que luego pueden alterar el flujo de ejecucion
    print("Numero de erroes = ",counter)
    print("all work was done")
    
main()
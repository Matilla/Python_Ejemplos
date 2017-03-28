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

# Dentro de la funcion para abrir el fichero, añadimos que se lance una excepcion nuestra en caso de que el fichero no tenga la extension requerida
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

main()
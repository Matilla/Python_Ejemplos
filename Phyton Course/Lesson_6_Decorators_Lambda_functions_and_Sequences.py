'''
Created on Mar 29, 2017

@author: Administrator
'''

# How to use decorators

import  operator # Es necesario importar operator para usar itemgetter

# This class is required for the example of decorators
class Files:
    def __init__(self,**kwargs):
        self.properties = kwargs
        
    def copy(self):
        print("copying...")
    def move(self):
        print("moving...")
    def remove(self):
        print("removing...")
    
    def get_properties(self):
        return self.properties
    def get_property(self,key):
        return self.properties.get(key,None)
    
    # decorator definition
    @property
    def privacy(self):
        return self.properties.get('privacy')
    
    # decorator definition
    @privacy.setter
    def privacy(self,c):
        self.properties['privacy']=c
    
    # decorator definition
    @privacy.deleter
    def privacy(self):
        del self.properties['privacy']

# This class in required for the example of generators with classes
class inclusive_range:
    def __init__(self,*args):
        numargs=len(args)
        if numargs < 1: raise TypeError('requires at least 1 param')
        elif numargs==1:
            self.stop=args[0]
            self.step=1
            self.start=0
        elif  numargs==2:
            (self.start,self.stop)=args
            self.step=1
        elif numargs==3:
            (self.start,self.stop,self.step)=args
        else: raise TypeError('Expected at most 3 params received {}'.format(numargs))
        
    def __iter__(self):
        i=self.start
        while i<=self.stop:
            yield i
            i += self.step
        pass
    
# How to define lambda function -> Sirven para crear funciones  en una linea
def calc(x):
    return x*2

t = lambda x: x*2 # Funcion lambda que realiza la misma funcionalidad que la funcion calc definida anteriormente, pero no tiene nombre, solo se asigna a una variable en este caso t, tampoco tiene return 

# Lambda functios with multi args
def add(x,y):
    return x+y
def minus(x,y):
    return x-y

result=lambda x,y: (x+y,x-y)

def main():
    # Create a class instance setting a property value for privacy porperty
    imageDoc=Files(privacy="secret")
    print(imageDoc.get_property("privacy"))
    
    # How to use decotaror for basicaly do the same that the code above does
    newImageDoc=Files()
    newImageDoc.privacy="archive"
    print(newImageDoc.privacy)
    
    # How to use lambda functions
    print(calc(3)) # Esta funcion se puede definir como una funcion lambda de la siguiente manera
    # Funcion lambda que realiza la misma funcionalidad que la funcion calc definida anteriormente
    # la funcion lambda se puede definir dentro del def main() o fuera como se realiza en este caso
    print(t(3))
    
    # How to use multi args lambda functions
    print(add(5, 6))
    print(minus(6, 5))
    
    print(result(6,5))
    print(result(6,5)[0]) # se puede incluir el indexador con valor 0 y nos da el primer resultado
    print(result(6,5)[1]) # se puede incluir el indexador con valor 0 y nos da el segundo resultado
    
    #  Operadores y keywords en sequences
    tupla=tuple(range(10)) # esto crea un tupla
    arrayList=list(range(10)) #esto crea una lista, es decir un array, 
    
    print("Como usar funciones y operadores sobre tuplas y listas creadas con range")
    print(tupla," esto es una tupla")
    print(arrayList," esto es un array")
    
    print("En una tupla no se puede cambiar un valor, en un array si, append puede usarse en un array pero no en una tupla")
    print("En una tupla y en un array se puede usan funciones len, is in o is not in")
    
    # How to use ittengetter, es necesario importar operador
    # itemgetter fecht una lista por el numero de elemento y lo devuelve
    lista = ['a','b','c','d','e']
    getseconditem = operator.itemgetter(1)
    print(getseconditem(lista))
    print(operator.itemgetter(1,2,5)('abcdefg')) # En este caso indico los elementos que quiero recuperar de la tupla creada en esta misma linea
    
    #  How to use enumerate
    seasons=['winter','spring','summer','autumn']
    seasons_arrau_of_tuplas=list(enumerate(seasons))
    print(seasons)
    print(seasons_arrau_of_tuplas)
    
    #  How to use eval
    v=10
    print(v)
    print(eval('v+1')) # El argunmento debe ser un string
    
    # How to use iterators
    try:
        with open('file.txt') as fh:
            for line in iter(fh.readline(),'') :
                print(line)
    except IOError as e:
        print(e)
    
    # How to use nested sequences
    seasons2=["winter",("spring","summer"),["autumn","fall"]] # Esto es una secuencia anidada
    print(seasons2)
    print(type(seasons2))
    print(seasons2[0]) # Devuelve la primera palabra de la lista
    print(seasons2[0][1]) # Devuelve la segunda letra de la palabra winter
    
    # How to use:  Implementar generator function
    def inclusive_range_function(start,stop,step):
        i = start
        while i <= stop:
            yield i
            i+=step
    print("This is a sample generator function")
    for i in inclusive_range_function(0,20,5): # se usa la generator function "inclusive_range"
        print('Ejemplo de uso de la funcion inclusive_range_function : ',i,end=' ')

    # How to use:generators function using range
    print("")
    o = range(5,25,2)
    for j in o: print(j,end=' ')
    
    # How to use:generators function in a class
    print("")
    p=inclusive_range(10,20,3) # el uso de la clase se puede iniciarlizar con 1,2 o 3 argumentos, ver la clase; y se controla el error en caso de que se pasen mas de 3 parametros
    for k in p: print('Ejemplo uso gen func in a class :',k,end=' ')
    
main()
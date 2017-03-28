'''
Created on Mar 28, 2017

@author: Administrator
'''
# Third lesson how to use:
#  Sequences
#  A sequences can be strings, lists o  tuplas support the same types of operations, for example slicing or indexing or built in functions
from builtins import print
from time import _STRUCT_TM_ITEMS

def main():
    
    print('This is how working with sequences and len,amx and min built in function')
    print(len("pizza")) #len on a string
    print(len([1,2,3,4,5])) #len on an array
    print(len(['a','b','c'])) #array of letters
    print(max([1,2,3,4,5])) #max funcion on an int array
    print(min([1,2,3,4,5])) #max funcion on an int array
    
    print('This is how working with sequences and range built in function')
    mynums=range(10) # me dice el rango que hay de  0 a 10
    print(mynums)
    mynums1=list(range(10)) # me da los numeros de 0 a 9
    print(mynums1)
    mynums2=list(range(10,20)) # me dalos numero de 10 a 19 
    print(mynums2)
    mynums3=list(range(10,20,2)) # me da los numeros pares entre 10 y 20 
    print(mynums3)
    
    print('This is how working with sequences and sorted built in function')
    print(sorted([1,5,2,7,3,9]))
    print(sorted(['a','h','b','z','f']))
    items=['pan','agua','vino','queso']
    print(sorted(items))
    
    print('This is how working with sequences and sorting functions')
    nums=[5,4,3,2,1]
    nums.sort()
    print(nums)
    # Si en vez de usar un array uso un diccionario, estos no tienen la funcion .sort() y dara un error.
    # pero si en vez de eso uso un array de tuplas si puedo usar sorting, por ejemplo
    books = [('book1','a',10),('book2','z',9),('book3','g',5)]
    print('Imprime books antes de ordenar = ',books)
    #sorted(books,key=lambda books: books[2])
    books.sort(key=lambda books: books[2]) # se ordena siguiendo el tercer valor de cada tupla
    print('Imprime books despues de ordenar = ',books)
    
    print('This is how working with sequences and operator functions to sort')
    books = [('book1','a',10),('book2','z',9),('book3','g',5)]
    from operator import itemgetter,attrgetter
    books.sort(key=itemgetter(2))
    print(books)
    books.sort(key=itemgetter(1))
    print(books)
    
    print('This is how working with sequences and slicing')
    letters="abcdefgh"
    slice1=letters[1:3] # Nos da bc
    print(slice1)
    slice1=letters[:3] # Nos da abc
    print(slice1)
    slice1=letters[:] # Nos da todo
    print(slice1)
    items=['cheese','milk','wine']
    slice2=items[0:2]
    print(slice2) # Nos da milk y wine
    
    print('This is how working with sequences and indexing')
    print(items)
    items[2]='juice' # se cambia el valor del tercer elemento
    print(items) 
    
    print('This is how working with sequences and sorting in place')
    grocery=['milk','fruits','cheese','eggs','corn']
    print(grocery)
    grocery.sort() # Ordena la lista en orden alfanumerico
    print(grocery)
    newlist=sorted(grocery, key=lambda x: x, reverse=True) # crea una nueva lista copia de grocery ordenada en  alfanumerico e inverso
    print(newlist)
    grocery.sort(key=lambda x: x, reverse=True) # ordena la lista original en orden alfanumerico inverso
    print(grocery)
    
main()
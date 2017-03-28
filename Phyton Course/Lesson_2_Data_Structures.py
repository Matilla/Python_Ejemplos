'''
Created on Mar 28, 2017

@author: Administrator
'''
# Second lesson how to use:
#  List and  Dictionary
#  Organizing data using dictionaries, update and delete elements within a dictionary 

def main():
    
    print('This is how working with list')
    
    words="En un lugar de la mancha "
    print(words) # Writes the sentence
    words2="de cuyo nombre no quiero acordarme".split() # it returns an array
    print(words2) # prints the array form by each word in the sentence
    print(words2[1]) # prints the second position in the array 
    
    info=[[w.upper(),w.lower(),len(w)] for w in words2] # creo un array compuesto por la palabra en mayusculas, minusculas y su longitud por cada palabra en el array words2
    print(info)
    for data in info:
        print(data)
    
    print('This is how working with dictionary in memory')
    
    students={'name1':'alex','age1':'12','grade1':'A'} # creo un diccionario en memoria
    print('Name = ',students['name1']) # imprime el nombre del estudiante
    print(type(students)) # indica el tipo de la estructura de datos, en este caso dictionary pero in memory
    
    students2=dict(
        name="jane",
        age="13",
        grade="C"
        )
    print(type(students2)) # indica el tipo de la estructura de datos, en este caso dictionary 
    
    students3=dict(
        nombre="john",
        edad="14",
        notas="D",
        **students,
        **students2
        )
    print(type(students3)) # indica el tipo de la estructura de datos, en este caso dictionary con la concatenacion de los dictionaries students, students2, students3
    
    # Importante, los diccionarios no son un array de tuplas con la clave con mismo nombre, las claves tienen que ser distintas entre si
    
    # Se puede comprobar que una clave determinada pertenece a un diccioario
    if "name1" in students3: 
        print("name1 is in students3")
    else:
        print("name1 is not in students3")

    # como acceder a las claves y valores en un diccionario
    for i,j in students3.items():print(i,j)
    
    # se puede acceder a los valores con el metodo get de los diccionarios y obtener el valor o un mensaje en caso de que no exista esa clave.
    print(students3.get('name1','not found'))
    print(students3.get('name2','not found'))
    
    # se puede eliminar tuplas de un diccionario con el metodo pop
    print(students3)
    students3.pop('name1')
    print(students3)
    
    # se pueden eliminar elementos de un diccionario con del
    print('Name = ',students3['name'])
    del students3['name']
    if 'name' in students3:
        print('Name = ',students3['name'])
    else:
        print("Not found \'name\' in students3")
    
    # se pueden actualizar los valores de una clave
    print('Nombre = ', students3['nombre']) 
    students3['nombre']='john whitman'
    print('Nombre = ', students3['nombre'])
    
    #  se puede limpiar el contenido de un diccionario
    students3.clear()
    
    # se puede eliminar todo el diccionario
    del students2
    
main()
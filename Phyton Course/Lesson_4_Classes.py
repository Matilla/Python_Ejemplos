'''
Created on Mar 28, 2017

@author: Administrator
'''
from locale import windows_locale

# definincion de una clase simple
class data:
    def create(self):
        print("Creating data")
    def update(self):
        print("Updating data")
    def delete(self):
        print("Remove data")

# definincion de una clase con constructor parametrizado y atributo de clase
class mailData:
    def __init__(self,value): # Esta es la manera de definir el constructor de la clase
        self._v=value   # de esta manear paso un valor al constructor y lo asigno a un atributo de la clase
        print("constructor")

    def sendMail(self):
        print("Sending mail data ",self._v)
    def fwdMail(self):
        print("Forwarding mail data ",self._v)
    def ccMail(self):
        print("cc mail data ",self._v)

# definicion de clase con constructor inicializado por defecto y como crear y usar get y set funciones para atributos
class files:
    def __init__(self, ftype="text"):
        self._ftype='text'
    def move(self):
        print("file is moving")
    def copy(self):
        print("file is being copied")
    def delete(self):
        print("file is being deleted")
        
    def set_ftype(self,ftype):
        self._ftype=ftype
    def get_ftype(self):
        return self._ftype

# definicion de clase y como usar herencia
class fileSystem():
    def convertTo(self):
        print("I am converting to this filesystem")
    def dynamicPartition(self):
        print("I am changing to a dynamic partition")
    def status(self):
        print("I'm currently displaying the status of my system")
    def virtual(self):
        print("I am now a virtual filesystem")

class NTFS(fileSystem): # Hereda de la clase fileSystem de arriba
    def convertTo(self): # overwritten method
        super().convertTo() # Acceso al metodo de la clase padre
        print("I have converted to NTFS filesystem")

# definicion de clase y como usar polimorfismo
class network:
    def cable(self): print("I'm the cable")
    def router(self): print("I'm the router")
    def wifi(self): print("I'm WIFI")
    
class tokenRing(network):
    def cable(self): print("I'm a token ring network")
    def router(self): print("I'm a router token ring network")

class ethernet(network):
    def cable(self): print("I'm a ethernet network")
    def router(self): print("I'm a router ethernet")
    def wifi(self): print("I'm a WIFI for mac")


def main():
    customerdata=data()
    customerdata.create()
    customerdata.update()
    customerdata.delete()

    myMail=mailData(99)
    myMail.sendMail()
    myMail.fwdMail()
    myMail.ccMail()
    
    myFile=files()
    myFile.move()
    myFile.copy()
    print(myFile.get_ftype())
    myFile.set_ftype('bmp')
    print(myFile.get_ftype())
    
    myFS=fileSystem()
    myFS.convertTo()
    
    myFS2=NTFS()
    myFS2.convertTo()
    myFS2.status()
    myFS2.dynamicPartition()
    
    windows=tokenRing()
    mac=ethernet()
    windows.cable()
    mac.cable()
    
    print("Loop through the class instances windows and mac")
    for obj in (windows,mac):
        obj.cable()
        obj.router()
        obj.wifi()
    
main()
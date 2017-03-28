'''
Created on Mar 27, 2017

@author: Administrator
'''

# First lesson how to use:
# Multiple choices - List, Array and Dictionary
# Flow control - For loop
# Conditional sentences


def main():
    
    print('This is how a Dictionary is use it')
    choices=dict(
        alex="A",
        jane="B",
        john="C"
        )
    print(choices["alex"])
    
    print('This is how flow control is use it for FOR sentences')
    
    data="This is where I want to break"
    for char in data:
        if char=='b': break
        print(char,end='')
    
    print("") # Write a blank line
    print('This is how conditional sentences is use it for ')
    
    x,y=10,1000
    if (x==10):
        msg="x is equal to 10"
    elif (x<y):
        msg="x is less than y"
    elif (x==y):
        msg="x is equal to y"
    else:
        msg="x is greater than y"
    print(msg)
      
main()
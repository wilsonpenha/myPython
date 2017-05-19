'''
Created on 1 de mai de 2017

if expression1:
   statement(s)
elif expression2:
   statement(s)
elif expression3:
   statement(s)
else:
   statement(s)
   
@author: wpjunior
'''

if __name__ == '__main__':
    n = int(input())
    
    mod = n % 2
    
    if (mod == 1):
        print("Weird")
    elif (n>=2 and n<5):
        print("Not Weird")
    elif (n>=6 and n<=20):
        print("Weird")
    else:
        print("Not Weird") 
    
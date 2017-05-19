'''
Created on 1 de mai de 2017

@author: wpjunior
'''

def is_leap(year):
    
    #print(year%100)
    
    if (year%4==0 and year%100>0):
        return True
    elif (year%100==0 and year%400==0):
        return True
    else:
        return False


if __name__ == '__main__':
    year=int(input())
    print(is_leap(year))
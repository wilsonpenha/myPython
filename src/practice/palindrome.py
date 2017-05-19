'''
Created on 5 de mai de 2017

@author: wpjunior
'''

import string

def isAlmostPalindrome():
    s = input('Enter a string: ')
    l=len(s)
    list_s=list(s)
    last_i = l-1
    just_one=0
    for i in range(0,l):                                            
        if(list_s[i] !=list_s[l-i-1]):
            just_one+=1
            if (just_one>1): # means only the last member is different and it could be turn to palindrome by change it
                return False
    else:
        return True
    return True
    
if __name__ == '__main__':
    print(isAlmostPalindrome())
'''
Created on 1 de mai de 2017

better solution code:

def read_in():
   return [x.strip() for x in sys.stdin.readlines() ]
   
@author: wpjunior
'''

import sys

def readLine():
    s = input()
    #for i in range(len(s)):
    #    s[i] = s[i].replace('\n','')
    #print lines
    return s

if __name__ == '__main__':
    s = readLine()
    print (s)
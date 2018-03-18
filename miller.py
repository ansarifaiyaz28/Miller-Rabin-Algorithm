'''
Created on Mar 17, 2018

@author: MJYao
'''
from math import pow, fmod 
import random
def miller(n):
    tmpN, rString = n-1, "inconclusive"     #initialize tmpN=n-1 and rString="inconclusive"
    k, q = 0, 0     #initialize k and q to zero
    while n-1!=pow(2,k)*q:      #find integers k, q, with k>0, q is odd, so that n-1 = (2^k)*q 
        if tmpN%2==0:
            tmpN, q  = divmod(tmpN, 2)      #divmod(x,y) return two value quotient and remainder
            k+=1
        else:
            q = tmpN        #this confirms that q is odd
    if rString == inconclusive(n, k, q):
        return("inconclusive")
    else:
        return("composite")

def inconclusive(n,k,q):  
    a = random.choice(list(range(1,n-1)))
    if int(fmod(pow(a,q),n))==1:
        return("inconclusive")
    else:
        for j in range(k):
            if int(fmod(pow(a, pow(2, j)*q), n)) == n-1:
                return("inconclusive")

print(miller(int(input("enter integer greater than 2: "))))


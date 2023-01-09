from math import floor
import random


#function for finding gcd of two numbers using euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#uses extened euclidean algorithm to get the d value
def get_d(e, z):
    a = z #prime #z 
    b = e #e 
    c = (1,0) #c is initally (1,0) for the algorithm (see example (z=60=(1,0), but we j switch out z  
    d = (0,1) #d is initally (0,1) for the algorith 
    
    #Stop when e =1 (Euclid(#,1)
    while(b != 1):
        l = floor(a/b) #l = z/e 
        a, b = b, a % b #new (a,b) becomes (b, a mod b)
        c, d = d , (c[0]-l*d[0],c[1]-l*d[1]) #c2 becomes d1, d2 becomes ->Calculate c-d (<1,0>-<0,1>) for each iteration (recursive call)
    
    if(d[1] < 0): #if d is negative 
        return z + d[1] #add z to d[1] to make it positive 
    return d[1] #return d 
    
def is_prime (num):
    if num > 1: 
      
        # Iterate from 2 to n / 2  
       for i in range(2, num//2): 
         
           # If num is divisible by any number between  
           # 2 and n / 2, it is not prime  
           if (num % i) == 0: 
               return False 
               break
           else: 
               return True 
    else: 
        return False


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    z = (p-1)*(q-1)
    n = p*q
    e=random.randint(1,z)
    while(gcd(e,z) != 1):
        e = (e + 1)%z
    d=get_d(e,z)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    #plaintext is a single character
    #cipher is a decimal number which is the encrypted version of plaintext
    #the pow function is much faster in calculating power compared to the ** symbol !!! 
    m = ord(plaintext)  
    return pow(m,pk[0],pk[1])

def decrypt(pk, ciphertext):
    #ciphertext is a single decimal number
    #the returned value is a character that is the decryption of ciphertext
    sum = pow(ciphertext,pk[0],pk[1])
    return chr(sum)

if(__name__ == '__main__'):
    print(generate_keypair(13,17))
    print("cyphertext = ", encrypt((11,221),'a'))
    
    print("plaintext  = ", decrypt((35,221),193))

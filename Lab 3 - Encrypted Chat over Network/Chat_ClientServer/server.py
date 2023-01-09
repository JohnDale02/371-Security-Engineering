from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
import re
from RSA import decrypt
PORT_NUMBER = 5000
SIZE = 1024

#hostName = '10.0.0.1'
hostName = gethostbyname( 'DE1_SoC' )

mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )

print ("Test server listening on port {0}\n".format(PORT_NUMBER))
client_public_key=''
while True:
        (data,addr) = mySocket.recvfrom(SIZE)
        data=data.decode()
        if data.find('public_key')!=-1: #client has sent their public key
            #retrieve public key and private key from the received message (message is a string!)
            temp = data.split(" ")
            #split public key (e,n) received from client 
            public_key_e=int(temp[1])
            public_key_n=int(temp[2])
            #server prints the public key to the screen 
            print ('public key is : %d, %d'%(public_key_e,public_key_n))
        else:
            #the ecipher (encrypted text/message)
            cipher=int(data)
            print (str(cipher)+':')
            #data_decoded is the decoded character based on the received cipher, calculate it using functions in RSA.py
            
            #decrypted message (public key decrypts the ciphertext/message) 
            data_decoded=decrypt((public_key_e, public_key_n),cipher)
            print (data_decoded)
sys.ext()

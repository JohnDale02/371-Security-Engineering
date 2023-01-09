from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
import re
import struct
from RSA import decrypt
import DES


PORT_NUMBER = 5000
SIZE = 8192

#hostName = '10.0.0.1'#gethostbyname( '192.168.1.3' )
hostName = gethostbyname( 'DE1_SoC' )

mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )

print ("Test server listening on port {0}\n".format(PORT_NUMBER))
client_public_key=''
des_key=''
while True:
        (data,addr) = mySocket.recvfrom(SIZE)
        data=data.decode()
        print(data)
        if data.find('public_key')!=-1: #client has sent their public key\
            #retrieve public key and private key from the received message (message is a string!)

            #data is the message (the public key) 
            #split the public key for indexing 
            temp = data.split(" ")
            
            public_key_e= int(temp[1])
            public_key_n= int(temp[2])
            print ('public key is : %d, %d'%(public_key_e,public_key_n))
        elif data.find('des_key')!=-1: #client has sent their DES key
            #read the next 8 bytes for the DES key by running (data,addr) = mySocket.recvfrom(SIZE) 8 times and then decrypting with RSA
            print("data" +data)
            print(data)
	    

            des_key=''#des key string 
            
            #decrpt the key 
            #8 bytes 
            for i in range(8):
                (data,addr) = mySocket.recvfrom(SIZE)
                #append to des_key string 
                print(data)
                cipher = int(data)
                des_key+=decrypt((public_key_e, public_key_n),cipher)

            print ('DES key is :' + des_key)

            #now we will receive the image from the client
            (data,addr) = mySocket.recvfrom(SIZE)
            #decrypt the image
            #the received encoded image is in data
            #perform des decryption using des.py
            coder=des.des()
            #the final output should be saved in a byte array called rr_byte
            rr_byte=bytearray()
            #decrypted image 
            r = coder.decrypt(des_key, data)
            
            for x in r: 

                rr_byte+= bytes([ord(x)]) #ord converts character (x) to ASCII. bytes takes in 8 bits and makes a byt

            #rr_byte holds decrypted image 

            #write to file to make sure it is okay
            file2=open(r'penguin_decrypted.jpg',"wb") 
            file2.write(bytes(rr_byte))
            file2.close()
            print ('decypting image completed')
            break
        else:
            continue

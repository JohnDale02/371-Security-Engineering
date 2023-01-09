
from pickle import FALSE
import des
import sys
from socket import socket, AF_INET, SOCK_DGRAM, gethostbyname
from RSA import generate_keypair,encrypt,decrypt
import struct


#SERVER_IP = '10.0.0.2' 
SERVER_IP = gethostbyname( 'DE1_SoC' )
PORT_NUMBER = 5000
SIZE = 1024
des_key='ece371!!'
print ("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))

mySocket = socket( AF_INET, SOCK_DGRAM )
message='hello'

#first generate the keypair
#get these two numbers from the excel file
p=1297273
q=1297651
###################################your code goes here#####################################
#generate public and private key from the p and q values
public=[0,0]
private=[0,0]

#generate RSA public and private keys 
public, private = generate_keypair(p,q)
#send public key over the network (to image server) 
message=('public_key: %d %d' % (public[0], public[1]))
mySocket.sendto(message.encode(),(SERVER_IP,PORT_NUMBER))

#encode converts string to a form sent over the socket 
message=('des_key')
mySocket.sendto(message.encode(),(SERVER_IP,PORT_NUMBER))
###################################your code goes here#####################################
#encode the DES key with RSA and save in DES_encoded, the value below is just an example

des_encoded=[0]*8

for i in range(len(des_key)):
    #client encrypts each letter in the de_key with the private key and puts it in the des_encoded array 
    des_encoded[i] = str(encrypt(private,des_key[i]))

#send the encrypted symmetric DES Key over the network to the client sercver 
[mySocket.sendto(code.encode(),(SERVER_IP,PORT_NUMBER)) for code in des_encoded]
#read image, encode, send the encoded image binary file
file=open(r'penguin.jpg',"rb") 
data=file.read()
file.close()

###################################your code goes here#####################################
#the image is saved in the data parameter, you should encrypt it using des.py
#set cbc to False when performing encryption, you should use the des class
#coder=des.des(), use bytearray to send the encryped image through network
#r_byte is the final value you will send through socket
r_byte=bytearray()

#encrypt image using DES 
coder = des.des() #coder is an object of des class 

r = coder.encrypt(des_key, data) #encrypted penguin image (string of characters)

#for each character in the encrypted image file (filled with chars )
for x in r: 
    #Put into bytes (8-bit items)
    r_byte+= bytes([ord(x)]) #ord converts character (x) to ASCII. bytes takes in 8 bits and makes a byte 

#r_byte is the encrypted image in ASCII
#send image through socket
mySocket.sendto(bytes(r_byte),(SERVER_IP,PORT_NUMBER))
print('encrypted image sent!')


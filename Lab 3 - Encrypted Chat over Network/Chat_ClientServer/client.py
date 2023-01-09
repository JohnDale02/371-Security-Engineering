import sys
from socket import socket, AF_INET, SOCK_DGRAM, gethostbyname
from RSA import generate_keypair,encrypt,decrypt

#SERVER_IP = '10.0.0.2' 
SERVER_IP = gethostbyname( 'DE1_SoC' )
PORT_NUMBER = 5000
SIZE = 1024
print ("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))

mySocket = socket( AF_INET, SOCK_DGRAM )
message='hello'

#first generate the keypair
#get these two numbers from the excel file
p=1297459
q=1297993

#generate public and private key from the p and q values
#hint: use generate_keypair() function from RSA.py
public, private = generate_keypair(p,q)

#THis is the public key (e,n) that the client sends to the chat_server (not encrypted)
message=('public_key: %d %d' % (public[0], public[1]))
print(message)
mySocket.sendto(message.encode(),(SERVER_IP,PORT_NUMBER))
while True:
        message=input()
        message.join('\n')
        #message is a string input received from the user, encrypt it with RSA character by character and save in message_encoded
        #message encoded is a list of integer ciphertext values in string format e.g. ['23131','352135','54213513']
        #hint: encrypt each character in message using RSA and store in message_encoded
        
        #encoded message to send to chat_server
        message_encoded=[]
        for c in message:
                #encrypt the character with private key and append to encrypted message array 
                message_encoded.append(str(encrypt(private,c)))
        
        #Socket sends encrypted message/txt  to chat_server
        [mySocket.sendto(code.encode(),(SERVER_IP,PORT_NUMBER)) for code in message_encoded] # do not change [sends message through socket]
sys.exit()

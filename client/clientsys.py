from calendar import c
from multiprocessing.connection import Client
import socket
import os

from cryptex import decrypt_file,encrypt_file
# ?rom tcp.server.cryptex import decrypt_file
IP = socket.gethostbyname(socket.gethostname())
PORT = 44256
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 4096


def send_cmd(cmd,mode):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   
    """ Connecting to the server. """
    client.connect(ADDR)
    """ Opening and reading the file data. """


    # file = open("data.txt", "r")
    # data = file.read()
    
   
    
    message=mode+cmd
    client.send(message.encode(FORMAT))
        #client.send(cmd.encode(FORMAT))

        
    cmd=decrypt_file(cmd,mode)
    # cmd=cmd.split()[0]
    # path
    if(len(cmd.split())==1):

        if(cmd=="CWD"):
            msg=client.recv(SIZE).decode(FORMAT)
                # print("msg before dec",msg)
            msg=decrypt_file(msg,mode)
            print("output:",msg)
        
        elif(cmd=="LS") :
            
            msg=client.recv(SIZE).decode(FORMAT) 
            msg=decrypt_file(msg,mode) 
            print("output",msg)
    else:
        cmd1=cmd.split()[0]
        path=cmd.split()[1]

        if(cmd1=="CD"):
            msg=client.recv(SIZE).decode(FORMAT) 
            msg=decrypt_file(msg,mode) 
            print("output",msg)
        elif(cmd1=="UPD"):
            file =open(path,'r')

            data = file.read()
            data=encrypt_file(data,mode)
            client.send(data.encode(FORMAT))
            msg=client.recv(SIZE).decode(FORMAT)
            msg=decrypt_file(msg,mode) 
            print("Successful::",msg)
        
        elif(cmd1=="DWD"):

            filename=os.path.basename(path)
            
            data=client.recv(4096).decode()

            data=decrypt_file(data,mode)
            if(data=="NOK"):
                print("output:",data)
                
            else:    
                file = open(filename, "w")
                file.write(data)
                file.close()


                



        



# if __name__ == "__main__":
    
    

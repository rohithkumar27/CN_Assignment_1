import py_compile
import sys
import os
from clientsys import send_cmd
from cryptex import encrypt_file,decrypt_file

if __name__ == '__main__':

    command=input("Please type the Command: ")
    encryptionmode=input("Select the encryption mode: ")
    com_enpy=encrypt_file(command,encryptionmode)
    send_cmd(com_enpy,encryptionmode)
        
        # path = os.getcwd()
        # print("Current directory is:,",path)

    

    #elif(command.split()[0]=="UPD"):
        #encryptionmode=input("Select the encryption mode: ")
        #com_enpy=encrypt_file(command.split()[0],encryptionmode)
        #send_cmd(com_enpy,encryptionmode)
        #filename=command.split()[1]

        #data=open(filename,"r")
        #data = data.read().replace('\n', ' ')
        #data_enc=encrypt_file(data,encryptionmode)
        #uploadfile(filename,data)
        






    
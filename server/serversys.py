import socket
import os

from cryptex import encrypt_file,decrypt_file
# from cryptex import 
IP = socket.gethostbyname(socket.gethostname())
PORT = 44256
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
def getcomd():
    print("[STARTING] Server is starting.")
    """ Staring a TCP socket. """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    """ Bind the IP and PORT to the server. """
    server.bind(ADDR)
    """ Server is listening, i.e., server is now waiting for the client to connected. """
    server.listen()
    print("[LISTENING] Server is listening.")


    
    while True:
    
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")
        """ Receiving the filename from the client. """
        
        message=conn.recv(SIZE).decode(FORMAT)
        
        # print("where is the bug")
        mode=message[0]
        
        

       
        
        msg=message[1:]
        # print("message is:",msg)

        com=decrypt_file(msg,mode)
        
        if(len(com.split())==1):

        #print(com)
            if(com=="CWD"):
                path = os.getcwd()
                path=encrypt_file(path,mode)
                conn.send(path.encode(FORMAT))
                
                # reply(path)print("Current directory is:,",path)
            elif(com=="LS"):
                path = os.getcwd()
                string=""
                ans=os.listdir(path)
                for i in ans:
                    string+=i
                    string+=","
                new=string[:len(string)-1]
                new_str=encrypt_file(new,mode)
                conn.send(new_str.encode(FORMAT))
        else:
            com1=com.split()[0]
            path=com.split()[1]
            if(com1=="CD"):
                try:
                    curr=os.chdir(path)
                    end_dir=encrypt_file(curr,mode)
                    conn.send(end_dir.encode())
                    stat="OK"
                    stat=encrypt_file(stat,mode)
                    conn.send(stat.encode())

                except:
                    stat="NOK"
                    stat=encrypt_file(stat,mode)
                    conn.send(stat.encode())


            elif(com1=="UPD"):
                try:
                    filename=os.path.basename(path)

                    data=conn.recv(1024).decode()

                    data=decrypt_file(data,mode)
                    file = open(filename, "w")
                    file.write(data)
                    file.close()

                    conn.send(encrypt_file("Finally,uploaded the file!",mode).encode(FORMAT))  
                except:
                    stat="NOK"
                    stat=encrypt_file(stat,mode)
                    conn.send(stat.encode())   
                
            elif(com1=="DWD"):    
                
                try:
                    #filename=os.path.basename(path)
                    file = open(path, "r")
                    data=file.read()
                    data=encrypt_file(data,mode)
                    conn.send(data.encode(FORMAT))
                    file.close()
                    
                    conn.send(encrypt_file("Succesfully downloaded",mode).encode(FORMAT)) 
                except: 
                    stat="NOK"
                    stat=encrypt_file(stat,mode)
                    conn.send(stat.encode())    
                
                
            
                
   







                    # reply(path)print("list of files in the directory:",os.listdir(path)) 
            
        
            
            elif(com=="close"):
                conn.close()
    #upload(mode,server)
     

    
        # print(f"[DISCONNECTED] {addr} disconnected.")


# if __name__ == "__main__":

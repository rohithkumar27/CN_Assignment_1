

#from pyexpat import model
import sys

def encrypt_file( text,mode):
    if (mode=="1"):
        
        return text
    elif(mode=="2"):
        s=2
        result = ""
  
    # traverse text
        for i in range(len(text)):
            char=text[i]
            if(char.isalnum()):
    
            # Encrypt uppercase characters
                if (char.isupper()):
                    result += chr((ord(char) + s-65) % 26 + 65)
        
                # Encrypt lowercase characters
                elif(char.islower()):

                    result += chr((ord(char) + s - 97) % 26 + 97)
                else:
                    result+=chr((ord(char)+s-48) % 10 + 48)   
                    

            else:
                result+=char
        
        return result
        
    elif(mode=="3"):
        res=[]
        for word in text.split(" "):
            res.append(word[::-1])
        
        result=" ".join(res)

        return result


def decrypt_file( text,mode):
    if (mode=="1"):
        
        return text
    elif(mode=="2"):
        s=26-2
        s1=10-2
        result = ""
  
    # traverse text
        for i in range(len(text)):
            char=text[i]
            if(char.isalnum()):
    
            # Encrypt uppercase characters
                # Encrypt uppercase characters
                if (char.isupper()):
                    result += chr((ord(char) + s-65) % 26 + 65)
        
                # Encrypt lowercase characters
                elif(char.islower()):

                    result += chr((ord(char) + s - 97) % 26 + 97)
                else:
                    result+=chr((ord(char)+s1-48) % 10 + 48)   
                    
            else:
                result+=char
        
        return result
        
    elif(mode=="3"):
        res=[]
        for word in text.split(" "):
            res.append(word[::-1])
        
        result=" ".join(res)
        # print(result)
        return result












# text="AR%^TZ"
# mode1='PlAIN_TEXT'
# mode2="SUBSTITUTE"
# mode3="TRANSPOSE"
# print(decrypt_file(text,mode1))
# print(decrypt_file(text,mode2))
# print(decrypt_file(text,mode3))
    

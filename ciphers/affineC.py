def encryption(plainText, a, b):
    
    plainText = plainText.rstrip()
    
    cipherText = ""

    for i in plainText:
        if(i==" "):
            cipherText += " "
        elif(i.isupper()):
            cipherText += chr((a*(ord(i)-65) + b)%26 + 65)
        else:
            cipherText += chr((a*(ord(i)-97) + b)%26 + 97)
        print(cipherText)
    
    return cipherText

def mod_Inv(x,y):
    for i in range(y):
        if (x*i)%y==1:
            return i

def decryption(cipherText, a, b):
    
    cipherText = cipherText.rstrip()
    
    a = mod_Inv(a,26)
    
    plainText = ""

    for i in cipherText:
        if(i==" "):
            plainText += " "
        elif(i.isupper()):
            plainText += chr(a*(ord(i)-65 - b)%26 + 65)
        else:
            plainText += chr(a*(ord(i)-97 - b)%26 + 97)
        
    return plainText
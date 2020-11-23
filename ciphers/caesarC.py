def encryption(plainText, key):
    
    plainText = plainText.rstrip()
    
    cipherText = ""

    for i in plainText:
        if(i==" "):
            cipherText += " "
        elif(i.isupper()):
            cipherText += chr((ord(i)-65+key)%26 + 65)
        else:
            cipherText += chr((ord(i)-97+key)%26 + 97)
    
    return cipherText

def decryption(cipherText, key):
    
    cipherText = cipherText.rstrip()
    
    plainText = ""

    for i in cipherText:
        if(i==" "):
            plainText += " "
        elif(i.isupper()):
            plainText += chr((ord(i)-65-key)%26 + 65)
        else:
            plainText += chr((ord(i)-97-key)%26 + 97)
        
    return plainText

def hacking(cipherText):
    
    solutions = []
    
    for i in range(1,26):
        solutions.append(decryption(cipherText,i))
        
    return solutions
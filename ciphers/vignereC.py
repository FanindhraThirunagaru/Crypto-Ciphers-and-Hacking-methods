def encrypt(plainText, Key):
    
    plainText = plainText.rstrip().lower()
    Key = Key.rstrip().lower()
    
    k,keyLength = 0,len(Key)

    cipherText = ""

    for i in plainText:
        if(i==" "):
            cipherText += " "
        else:
            cipherText += chr((ord(i)+ord(Key[k])-194)%26 + 97)
            k = (k+1)%keyLength
            
    return cipherText
    
def decrypt(cipherText, Key):
    
    cipherText = cipherText.rstrip().lower()
    Key = Key.rstrip().lower()
    
    k,keyLength = 0,len(Key)

    plainText = ""

    for i in cipherText:
        if(i==" "):
            plainText += " "
        else:
            plainText += chr((ord(i)-ord(Key[k]))%26 + 97)
            k = (k+1)%keyLength
            
    return plainText



def encryption(plainText, key, input_type):
    method = [26,2,10]
    subract = [97,48,48]
    
    plainText,key = plainText.lower().split(),key.lower().split()
    cipherText = []

    for i in range(len(plainText)):
        partial_cipherText = ""
        for j in range(len(plainText[i])):
            c = (ord(plainText[i][j])+ord(key[i][j])-2*subract[input_type-1])%method[input_type-1]
            partial_cipherText+=chr(c+subract[input_type-1])
        cipherText.append(partial_cipherText)

    cipherText = " ".join(cipherText)
    
    return cipherText

def decryption(cipherText, key, inputType):
    method = [26,2,10]
    subract = [97,48,48]
    
    cipherText,key = cipherText.lower().split(),key.lower().split()
    plainText = []

    for i in range(len(cipherText)):
        partial_plainText = ""
        for j in range(len(cipherText[i])):
            p = (ord(cipherText[i][j])-ord(key[i][j]))%method[input_type-1]
            partial_plainText+=chr(p+subract[input_type-1])
        plainText.append(partial_plainText)

    plainText = " ".join(plainText)

        
    return plainText
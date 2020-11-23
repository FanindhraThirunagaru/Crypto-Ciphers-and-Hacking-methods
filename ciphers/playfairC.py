import numpy as np

def encrypt(plainText,key):
    
    keyTable = []
    
    data = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    plainText = plainText.rstrip().lower().replace("j","i")
    Key = key.rstrip().lower()

    cipherText = ""

    for i in Key:
        if(data and i in data):
            keyTable.append(i)
            data.remove(i)

    keyTable.extend(data)
    keyTable =  np.array(keyTable).reshape(5,5)

    if(len(plainText)%2==1):
        plainText+="z"

    for i in range(0,len(plainText),2):
        first_element = np.where(keyTable == plainText[i])
        second_element = np.where(keyTable == plainText[i+1])
        first_element_row,first_element_column = first_element[0][0],first_element[1][0]
        second_element_row,second_element_column = second_element[0][0],second_element[1][0]

        if(first_element_column==second_element_column):
            cipherText+=keyTable[(first_element_row+1)%5][first_element_column]
            cipherText+=keyTable[(second_element_row+1)%5][second_element_column]
        elif(first_element_row==second_element_row):
            cipherText+=keyTable[first_element_row][(first_element_column+1)%5]
            cipherText+=keyTable[second_element_row][(second_element_column+1)%5]
        else:
            cipherText+=keyTable[first_element_row][second_element_column]
            cipherText+=keyTable[second_element_row][first_element_column]
            
    return cipherText

def decrypt(cipherText,key):
    
    keyTable = []
    
    data = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    cipherText = cipherText.rstrip().lower()
    Key = key.rstrip().lower()

    plainText = ""

    for i in Key:
        if(data and i in data):
            keyTable.append(i)
            data.remove(i)

    keyTable.extend(data)
    keyTable =  np.array(keyTable).reshape(5,5)

    for i in range(0,len(cipherText),2):
        first_element = np.where(keyTable == cipherText[i])
        second_element = np.where(keyTable == cipherText[i+1])
        first_element_row,first_element_column = first_element[0][0],first_element[1][0]
        second_element_row,second_element_column = second_element[0][0],second_element[1][0]

        if(first_element_column==second_element_column):
            plainText+=keyTable[(first_element_row-1)%5][first_element_column]
            plainText+=keyTable[(second_element_row-1)%5][second_element_column]
        elif(first_element_row==second_element_row):
            plainText+=keyTable[first_element_row][(first_element_column-1)%5]
            plainText+=keyTable[second_element_row][(second_element_column-1)%5]
        else:
            plainText+=keyTable[first_element_row][second_element_column]
            plainText+=keyTable[second_element_row][first_element_column]
            
    return plainText
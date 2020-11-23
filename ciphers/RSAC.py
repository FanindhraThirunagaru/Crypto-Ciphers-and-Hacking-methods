def encrypt(pub_key,n_text):
    
    n_text = n_text.rstrip().upper()
    e,n=pub_key
    x=[]
    m=0
    for i in n_text:
        if(i.isupper()):
            m = ord(i)-65
            c=(m**e)%n
            temp1 = chr(c+65)
            x.append(temp1)
        elif(i.islower()):               
            m= ord(i)-97
            c=(m**e)%n
            temp2=chr(c+97)
            x.append(temp2)
        elif(i.isspace()):
            x.append(' ')
    code = ''
    
    return (code.join(x))

def decrypt(priv_key,c_text):
    
    c_text = c_text.rstrip().upper()
    d,n=priv_key
    x=''
    m=0
    for i in c_text:
        if(i== ' '):
            x+=' '
        elif(x.islower()):
            temp = ord(i)-97
            m=(temp**d)%n
            m+=97
            c=chr(m)
            x+=c
        else:
            temp = ord(i) - 65
            m = (temp**d)%n
            m+=65
            c=chr(m)
            x+=c
    
    return x

def prime(N):
    
    for i in range(2,int(N**0.5)+1):
        if((N%i)==0):
            return False
    return True

from math import gcd

def hacking(publicKey,cipherText):
    
    cipherText = cipherText.rstrip().upper()
    e,n = publicKey
    
    p,q = 0,0
    for p in range(2,int(n**2)+1):
        if((n%p)==0 and prime(p) and prime(int(n/p))):
            q = int(n/p)
            break
            
    phi = (p-1)*(q-1)
    plainTexts = ""
    
    d = 0
    
    for d in range(1,n+1):
        if((e*d)%phi==1):
            plainTexts = decrypt((d,n),cipherText)
            
    return plainTexts
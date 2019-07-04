import sys,math,numpy

def main():

    print(" ******______hello______******")
    mode=input(" enter your mode : (e) for encrypt (d) for decrypt\t")
    message=input(" enter your message please \t")
    branch=int(input(" enter thr branch of showing message you want "))

    print(" enter key:\n")

    key=numpy.zeros((2,2))

    for i in range(2):
        for j in range(2):
            print(" enter key(%s,%s)"%(i,j))
            key[i][j]=input()

    if mode=="e":
        print(encryptmessage(message,branch,key))
    if mode=="d":
        print(decryptmessage(message,branch,key))




#########################################
#########################################
#########################################
#########################################

def encryptmessage(message,branch,key):
    LETTERS="abcdefghijklmnopqrstuvwxyz"
    translated=[]
    n=2

    det=numpy.linalg.det(key)# WE SEE THE DETERMINANT OF MATRIX
    d=round(det,9)
    d=int(d)


    if d%2==0 or d%13==0:
        print(" please enter valuble keys \n your matrix determinant is even : %s"%d)
        sys.exit()

    for i in message:# WE DELETE SPACES
        if i==" ":
            message=list(message)
            message.remove(i)
            message="".join(message)

    if len(message)%n!=0:# WE ADD X
        p=len(message)%n
        for h in range(p,n):
            message=list(message)
            message.append("x")
            message="".join(message)

    for i in range(len(message)):# ENCRYPTING PROCOSS
        if i%n==0:
            j=i
            ls=[]
            for j in range(j,j+n):
                num=LETTERS.find(message[j])
                ls.append(num+1)

            for k in range(n):
                y=0
                for z in range(n):
                    x=int(int(key[k][z])*int(ls[z]))
                    y+=x
                y=(y-1)%26
                translated.append(LETTERS[y])

    if len(message)>=branch:
        for i in range(len(message)*2):# WE ADD BRANCH OF SPACES
            if i%(branch+1)==0:
                translated.insert(i," ")

    translated="".join(translated)
    return "".join(translated)



#########################################
#########################################
#########################################
#########################################


def decryptmessage(message,branch,key):

    length=input(" your original message is odd or even? : (o) for odd and (e) for even\t")

    LETTERS="abcdefghijklmnopqrstuvwxyz"
    translated=[]


    n=2

    for i in message:# WE DELETE SPACES
        if i==" ":
            message=list(message)
            message.remove(i)
            message="".join(message)

    det=numpy.linalg.det(key)
    d=round(det,9)
    d=int(d)


    inverse=int

    if d%13==0 or d%2==0:
        print(" enter the valuable key ")
        sys.exit()

    elif d%26==1:
        inverse=1
    elif d%26==3:
        inverse=9
    elif d%26==5:
        inverse=21
    elif d%26==7:
        inverse=15
    elif d%26==9:
        inverse=3
    elif d%26==11:
        inverse=19
    elif d%26==15:
        inverse=7
    elif d%26==17:
        inverse=23
    elif d%26==19:
        inverse=11
    elif d%26==21:
        inverse=5
    elif d%26==23:
        inverse=17
    elif d%26==25:
        inverse=25
    else:
        sys.exit(" social error \t\t")


    t=key[0][0]
    key[0][0]=key[1][1]
    key[1][1]=t

    key[0][1]=-key[0][1]
    key[1][0]=-key[1][0]

    for i in range(n):
        for j in range(n):
            key[i][j]%=26

    for i in range(n):
        for j in range(n):
            key[i][j]*=inverse

    for i in range(n):
        for j in range(n):
            key[i][j]%=26


    for i in range(len(message)):# ENCRYPTING PROCOSS
        if i%n==0:
            j=i
            ls=[]
            for j in range(j,j+n):
                num=LETTERS.find(message[j])
                ls.append(num+1)

            for k in range(n):
                y=0
                for z in range(n):
                    x=int(int(key[k][z])*int(ls[z]))
                    y+=x
                y=(y-1)%26
                translated.append(LETTERS[y])


    if len(message)>=branch:
        for i in range(len(message)*2):# WE ADD BRANCH OF SPACES
            if i%(branch+1)==0:
                translated.insert(i," ")

    if length=='o':
        translated.pop()

    translated="".join(translated)
    return "".join(translated)




main()

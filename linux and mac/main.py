import pickle
import os


def encode():
    os.system('clear')
    print(r'''    ______   _   __   ______   ____     ____     ______
   / ____/  / | / /  / ____/  / __ \   / __ \   / ____/
  / __/    /  |/ /  / /      / / / /  / / / /  / __/   
 / /___   / /|  /  / /___   / /_/ /  / /_/ /  / /___   
/_____/  /_/ |_/   \____/   \____/  /_____/  /_____/   
                                                       ''')

    x=input("Enter text to be encoded: ")
    print('')
    asc1=''
    val=''

    for i in range(0,len(x)):
        n=ord(x[i])
        b=str(bin(n)[2:])
        if len(b)<8:
            w=8-len(b)
            b=('0'*w)+b
        asc1+=b

    print(asc1)
    if len(asc1)%6!=0:
        asc=asc1+'0'*(6-len(asc1)%6)
        print(asc)
    else:
        asc=asc1
    
    for i in range(0,len(asc),6):
        bas=asc[i:i+6]
        f=open("binary.dat",'rb')
        try:
            while True:
                r=pickle.load(f)
                y=r[1]
                if len(y)<6:
                    y='0'*(6-len(y))+y    
                if y==bas:
                    val+=r[0]

        except EOFError:
            f.close()

    if len(asc1)%6==4:
        val=val+'='
    if len(asc1)%6==2:
        val=val+'=='
    
    os.system('clear')
    print("The encoded text is:")
    print('')
    print(val)
    print('')
    input('Press Enter to continue.')
    os.system('clear')



def decode():
    os.system('clear')
    print(r'''    ____     ______   ______   ____     ____     ______
   / __ \   / ____/  / ____/  / __ \   / __ \   / ____/
  / / / /  / __/    / /      / / / /  / / / /  / __/   
 / /_/ /  / /___   / /___   / /_/ /  / /_/ /  / /___   
/_____/  /_____/   \____/   \____/  /_____/  /_____/   
                                                       ''')

    x=input("Paste the Base64 code here: ")
    print('')
    l=[]
    bas=''
    val=''

    for i in range(len(x)):
        if x[i]=='=':
            continue
        else:
            l.append(x[i])
    
    for i in l:
        f=open("binary.dat",'rb')
        try:
            while True:
                r=pickle.load(f)
                if i==r[0]:
                    b=r[1]
                    bas=bas+b
                    break
                else:
                    continue
    
        except EOFError:
            f.close()

    if len(bas)%8!=0:       
        bas=bas.rstrip('0')

    for i in range(0,len(bas),8):
        asc=bas[i:i+8]
        asc1=int(asc,2)
        val+=chr(asc1)

    os.system('clear')
    print("The decoded text is:")
    print('')
    print(val)
    print('')
    input('Press Enter to continue.')
    os.system('clear')



def change():
    os.system('clear')
    while True:
        k=input("Enter Key: ")
        if len(k)!=64:
            os.system('clear')
            print("Invalid Key!")
            continue
        else:
            os.system('clear')
            break
    
    l=list(k)

    f=open("binary.dat",'rb+')
    try:
        while True:
            for i in l:
                r=pickle.load(f)
                r[0]=i
                f1=open("temp.dat",'ab')
                pickle.dump(r,f1)
                f1.close()
    
    except EOFError:
        f.close()
        os.remove("binary.dat")
        os.rename("temp.dat","binary.dat")

    print("Key changed Successfully!")
    print('')
    input('Press Enter to continue.')
    os.system('clear')



### MAIN ###
while True:
    print(r'''   ________  _________________  __  ___   _______   ____________  ____  __________ 
  / ____/ / / / ___/_  __/ __ \/  |/  /  / ____/ | / / ____/ __ \/ __ \/ ____/ __ \
 / /   / / / /\__ \ / / / / / / /|_/ /  / __/ /  |/ / /   / / / / / / / __/ / /_/ /
/ /___/ /_/ /___/ // / / /_/ / /  / /  / /___/ /|  / /___/ /_/ / /_/ / /___/ _, _/ 
\____/\____//____//_/  \____/_/  /_/  /_____/_/ |_/\____/\____/_____/_____/_/ |_|  
 ''')
    print("Welcome!")
    print("What would you like to do?")
    print('1. Encode')
    print('2. Decode')
    print('3. Change Key')
    print('4. Exit')
    a=input('(1/2/3/4): ')

    if a=='1':
        encode()
    elif a=='2':
        decode()
    elif a=='3':
        change()
    elif a=='4':
        os.system('clear')        
        print('Exiting...')
        break
    else:
        print("Invalid option!")
        input('Press Enter to continue.')
        os.system('clear')

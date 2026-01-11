from Emp import Employee
from datastore import Datastore
from Admin import Admin

def main():
    ch=0 
    while(ch !="2"):
        print('''SELECT OPTION FROM BELOW
        1.LOGIN
        2.EXIT
        ''')
        ch= input("Enter Ch:")
        if(ch=="1"):
            uname=input("Enter UserName: ")
            passw= input("Enter Password: ")
            unaam="admin" 
            passd="123a"
            if(uname==unaam and passw==passd):
                print("LOgin Successfull..........")
                ad1= Admin()
            else:
                print("INVALID CREDENTAILS.....")
        elif(ch=="2"):
            print("THANK YOU!!!!!!!")
        else:
            print("INvalid CHoice")

if(__name__ == "__main__"):
    main()
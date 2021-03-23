import re

regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
def check(email):
    if(re.search(regex, email)):
        print("valid email")
    else:
        print("invalid email")

if __name__ =='__main__':
    email = input("Enter your email id : ")
    check(email)


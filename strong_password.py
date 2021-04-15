import random
import string

def password(length):
    pc = string.ascii_letters + string.digits + string.punctuation
    pa = ''.join(random.choice(pc) for i in range(length))

    print("your password : ", pa)


l = int(input("Enter the length of password : "))
password(l)



# !JF]0Ff'
import random
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
length=len(letters)
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','$','%','^','&','*']
print("Welcome to the password generator !\n")
a = int(input("How Many Letters would you like to have in your Password ?\n"))
b = int(input("How Many numbers would you like to have in your Password ?\n"))
c = int(input("How Many symbols would you like to have in your Password ?\n"))
password = []
for i in range(1,a+1):
    password += random.choice(letters)
    
for i in range(1,b+1):
    password += random.choice(numbers)
       
for i in range(1,c+1):
    password += random.choice(symbols)
    
pas = password
random.shuffle(pas)
for i in pas:
    print(i,end="")
    

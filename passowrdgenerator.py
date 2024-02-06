import random
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','$','%','^','&','*']
print("welcome to the password generator")
a=int(input("how many letters you want in your password ?\n"))
b=int(input("how many symbols you want to have: \n"))
c=int(input("how many numbers you want: \n"))
password=[]
for i in range (0,a+1):
    password +=random.choice(letters)
   

for i in range(0,b+1):
    password +=random.choice(symbols)
    
    
for i in range(0,c+1):
    password +=random.choice(numbers)
    
pas=password
random.shuffle(pas)

for i in pas:
    print(i,end="")
    

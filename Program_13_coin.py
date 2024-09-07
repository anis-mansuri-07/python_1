#Program 13
https://www.useblackbox.io/editor?id=c53eda73-4e70-43f7-acdf-5c725cfd949a
#Excat change: Given a price identify if you have exact change summing up to that price?
value = int(input("Enter price  "))
price = value
c1 = c2 = c5 = c10 = c20 = c50 = c100 = c200 = c500 = c2000 = num =  0

while(price!=0):
    if(price>=2000):
        num = num+2000
        c2000 = c2000 + 1
        price = price - 2000
        continue
    if(price>=500):
        num = num+500
        c500 = c500 + 1
        price = price - 500
        continue
    if(price>=200):
        num = num+200
        c200 = c200 + 1
        price = price - 200
        continue
    if(price>=100):
        num = num+100
        c100 = c100 + 1
        price = price - 100
        continue
    if(price>=50):
        num = num+50
        c50 = c50 + 1
        price = price - 50
        continue
    if(price>=20):
        num = num+20
        c20 = c20 + 1
        price = price - 20
        continue
    if(price>=10):
        num = num+10
        c10 = c10 + 1
        price = price - 10
        continue
    if(price>=5):
        num = num+5
        c5 = c5 + 1
        price = price - 5
        continue
    if(price>=2):
        num = num+2
        c2 = c2 + 1
        price = price - 2
        continue
    if(price>=1):
        num = num+1
        c1 = c1 + 1
        price = price - 1
        continue
print("change of {} is".format(value))
print("2000: {}\n500:{}\n200:{}\n100:{}\n50:{}\n20:{}\n10:{}\n5:{}\n2:{}\n1:{}\n".format(c2000,c500,c200,c100,c50,c20,c10,c5,c2,c1))








amt = float(input("Enter amount:: "))
amt = int(amt)
coin1 = int(input("Enter coin no 1: "))
coin2 = int(input("Enter coin no 2: "))
coin3 = int(input("Enter coin no 3: "))
count = 0


for i in range(0,1+amt//coin1):
    for j in range(0,1+amt//coin2):
        for k in range(0,1+amt//coin3):
            if i * coin1 + j * coin2 + k * coin3 == amt :
              print(i,j,k,)
              count += 1

print("Total combination is:: {}".format(count))

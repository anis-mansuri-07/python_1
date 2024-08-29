#Program 11
#Check the given positive integer number if number is prime or not

num = int(input("Enter the positive integer::"))
if(num>1):
    for i in range(2,(num//2)+1):
        if(num%i) == 0:
            print("not Prime...")
            break
        
    else:
        print("Prime...")
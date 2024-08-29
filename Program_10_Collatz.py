#Program 10
#Collatz sequence  

Collatz_num = int(input("Enter the number::"))
while(Collatz_num!=1):
    if Collatz_num%2 == 0:
        Collatz_num/=2
        print(int(Collatz_num))
    else:
        Collatz_num = 3*Collatz_num + 1
        print(int(Collatz_num))
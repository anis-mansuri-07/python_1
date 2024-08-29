#Program 9
#Print Fibbonacci sequence
n1 , n2 =  0 , 1
Fib_Seq = int(input("How Many Fibonacci Sequence You want.."))
for i in range(0,Fib_Seq):
    temp = n1 + n2
    print(n1)
    n1 = n2
    n2 = temp
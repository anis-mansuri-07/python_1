#Program 2
#sum of the first N natural number

num  = float(input("Enter the number::"))
num = int(num)
if(num>=0):
    Sum = int(num*(num+1)/2)  #Formula to find sum
else:
    print("You Entered Wrong Type Of Data...")
    

print("The sum of the first {} number is:{} ".format(num,Sum))

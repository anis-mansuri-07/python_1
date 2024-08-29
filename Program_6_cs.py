#Program 6
#Find that student is from cs department or not

D_name = input("Enter Department Name::")
Stu_Cour = D_name[0:2].upper()
if(Stu_Cour=='CS'):
    print(D_name," is from cs department::")
else:
    print(D_name," is not from cs department::")
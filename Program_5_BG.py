#Program 5
#Write a program to find out if the blood groups match.
Blood_Grps = ('A+','B+','A-','B-','AB+','AB-','O+','O-')
BG_1 = input("Enter Blood Group Of Person 1:: ").upper()

for i in Blood_Grps:
    if BG_1 == i:
        print(BG_1,"Is Matched")
        break  
else:
    print(BG_1,"Not Matched")  
       


    

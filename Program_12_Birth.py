#Program 12
#Birthday month 
Birthday = {"Ayan" : '18/11/2003' ,
            "Aman" : '16/12/2000' ,
            "Jenul" : '25/07/2002' ,
            "Mahir" : '29/05/1996' }
month = input("Enter month:: ")
for dost , bd in Birthday.items():
    if bd[3:5] == month :
        print(dost)
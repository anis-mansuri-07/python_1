#Program 8
#Find out pass-percentage of a class a teacher is entering the marks of student. A student passes a course if the marks are at least 40 out of 100.
#The teacher wants to know the percentage of students passed.


std = int(input("Enter no of student in class:: "))
count = 0
print("Enter marks out of 100")

for i in range(1,std+1):
    print("Student",i,"Marks is")
    x = int(input())
    if(x>=40):
        count+=1

Pr = (count/std)*100  #Pr find formula

print("{:.2f}% Student passe the exam".format(Pr))
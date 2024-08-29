#Program 3
#Extracting fields of a roll number using string indexing and slicing.
#we take some fields and also number with fields so that every number is unique

print("Note:\nFirst 2 digit branch + 3 digit course name + 4 digit year of addm.. + Your  number..\n")
Field = input("Enter field:: ")    #First 2 digit branch + 3 digit course name + 4 digit year of addm.. + Your  number
Dep = Field[:2]
Course_name = Field[2:5] #Extracting from the field
Add_year = Field[5:9]
Roll_no = Field[9:]

print("Student's Department is::",Dep)
print("Student's Course Name is::",Course_name)
print("Student's Admission Year is::",Add_year)
print("Student's Roll Number is::",Roll_no)
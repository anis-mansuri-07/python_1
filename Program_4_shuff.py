#Program 4
#Word shuffling using string manipulation.
import random

S = input("Enter string:")
Spli = S.split()  
x = int(len(Spli)/2)
i  = 0
while(i<x):
    random.shuffle(Spli) #shuffling the words x times
    i+=1

for i in Spli:
  print(i,end=" ")
  
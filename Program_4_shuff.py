#Program 4
#Word shuffling using string manipulation.
s = input("Enter String : ")
lista = list(s)
for i in range(0,len(s)-2):
    if(i%2==0):
         temp = lista[i]
         lista[i] = lista[i+1]
         lista[i+1] = temp
s = ''.join(lista)
print(s)
  

import math

Rnum = int(input("Enter any integer number:  "))
Snumber = int(math.sqrt(Rnum)) + 1
print(Snumber)
flag = 0
for i in range(1, Snumber, 1):
      if ((Rnum%i)==0):
            flag += 1
            print("Hello", i)
print(flag)     
if(flag ==1):
      print("\t", Rnum , "is prime number")
else:
      print("\t", Rnum , "is not a prime number")


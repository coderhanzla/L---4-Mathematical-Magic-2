print("Check Whether the given number is prime or not ")
n= int(input("Enter the Number : "))

for i in range(2 , n):
    if n%i == 0:
     print("Prime")
     break
else:
    print("Not Prime")
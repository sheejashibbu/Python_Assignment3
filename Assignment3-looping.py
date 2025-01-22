a= int(input("enter a number first Number"))
b= int(input("enter a number second Number"))
c= int(input("enter a number Third6 Number"))
if a>b:
    if a>c:
        large=a
    else:
        large=c

else:
    if b>c:
        large=b
    else:
        large=c

print ("Biggest  Numbers is",large)
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
   print("factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


num = int(input("Enter a number: "))
reversed_num=0
while num != 0:
     digit = num % 10
     reversed_num = reversed_num * 10 + digit
     num //= 10
     print(reversed_num)

num = int(input("Enter a number: "))
print("The multiple are:")
for i in range(1,11):
 print(num*i,  end=" ")

for i in range(10):
     if i == 5:
         print("hello")
         print("fished: done")
         break
     print(i)

for i in range(11):
    if (i%3==0) :
         print("Fizz")
    elif (i%5==0):
        print("Buzz")
    elif(i%3==0) and (i%5==0):
        print ("FizzBuzz")
    else:
     print(i)
n=int(input())
for i in range(5,0,-1):
 for j in range(i,0,-1):
   print(j,end="")
print()

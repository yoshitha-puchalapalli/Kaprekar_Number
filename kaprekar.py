n=int(input())
a=n*n
total=0
while a>0:
    dig=a%10
    total=total+dig
    a=a//10
if(total==n):
    print("Kaprekar Number")
else:
    print("Not A Kaprekar Number")

a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
if(a>=b)and(b>=c):
    print(a,"a is greater")
elif(b>=a)and(b>=c):
    print(c,"is greater")
else:
    print(c,"is greater")
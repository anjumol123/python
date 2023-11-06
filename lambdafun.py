print("Area of rectangle")
l=int(input("length"))
b=int(input("breadth"))
c=lambda x,y:x*y
print("Area of rectangle:"+str(c(l,b)))
print("Area of square")
s=int(input("side of square"))
c=lambda x:x*x
print("Area of square:"+str(c(s)))
print("Area of triangle")
b=int(input("base"))
h=int(input("height"))
c=lambda x,y:1/2*x*y
print("Area of triangle:"+str(c(b,h)))
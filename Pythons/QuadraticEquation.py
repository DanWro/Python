import math


a=int(input("wartosc a: "))
b=int(input("wartosc b: "))
c=int(input("wartosc c: "))

Delta = (b**2)-(4*a*c)
p1=((-b)+math.sqrt(Delta))/2*a
p2=((-b)-math.sqrt(Delta))/2*a
print(p1,p2)


    
    


import math


a = float(input("a = "))
b = float(input('b = ' ))
c = float(input("c = "))
p = 1/2*(a+b+c)
pole = math.sqrt(p*(p-a)*(p-b)*(p-c))
print("pole trojkata = " , pole)

       
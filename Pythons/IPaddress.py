import random
def ip(a,b):
    return random.randint(a,b)
a=0
b=255
print(ip(a,b),".",ip(a,b),".",ip(a,b),".",ip(a,b))
i=0
while i<20:
    i=i+1
    print(ip(a,b),".",ip(a,b),".",ip(a,b),".",ip(a,b))

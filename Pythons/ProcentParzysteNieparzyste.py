from random import randint
lp=[]
ln=[]
lista = []
for x in range(1000):
    lista.append(randint(1,50))

for p in lista:
    if p%2==0:
        lp.append(p)
    if p%2!=0:
        ln.append(p)
print("Dla 1000 losowych liczb z przedziału: <1,50>")

print("Liczby parzyste : ", len(lp)/10 , " % ")
print("Liczby nie parzyste : " , len(ln)/10 , " % ")
  


lp=int(input("Podaj liczbe produktow : "))
i=0
koszyk=[]
portfel=[]
while i < lp :
    i=i+1
    print("Cena Produktu :  ", i)
    cena=int(input("podaj cene produktu : "))
    koszyk.append(cena)
suma=sum(koszyk)
print("koszt całkowity : " ,suma, "zl ")
b=int(input("wprowadz liczbe banknotow : "))
j=0
while j<b:
    j=j+1
    wb=int(input("podaj wartosc banknotow : "))
    assert wb==10 or wb==20 or wb==50, "Zly banknot"
    portfel.append(wb)
m=int(input("wprowadz liczbe monet : "))
if m<0:
   print("zero monet")
k=0
while k<m:
    k=k+1
    wm=int(input("podaj wartosc monet : "))
    assert wm==1 or wm==2 or wm==5, "Zla moneta"
    portfel.append(wm)
kwota=sum(portfel)
if kwota<suma:
    print("za malo kasy dales gosciu")
    
print("klient zapłacił : " ,kwota, "zl")
reszta=kwota-suma
print("reszta wynosi : ", reszta, "zl")

    
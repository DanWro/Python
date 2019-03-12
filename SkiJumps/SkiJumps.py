from random import randint
nr1="Daniel Wrona"
nr2="Adam Malysz"
nr3="Kozak"
def punkty_metr(a):
    k=80
    if a>k:
        s=2*(a-k)
        return s
def skoki():
    b=(randint(90,130))
    return b
def noty():
    wynik=[]
    while len(wynik) < 5:
        wynik.append(randint(15,20))
        a=sorted(wynik)
        result=a[1:4]
        suma=sum(result)
    return suma
def suma():
    a=punkty_metr(skoki())
    b=noty()
    return a+b

print("skoczek 1 : " ,nr1,"pkt za odleglosc :",punkty_metr(skoki()),"punkty za noty :",noty(),"suma :",suma(),"pkt")
print("skoczek 2 : " ,nr2,"pkt za odleglosc :",punkty_metr(skoki()),"suma :",suma(),"pkt")
print("skoczek 3 : " ,nr3,"pkt za odleglosc :",punkty_metr(skoki()),"suma :",suma(),"pkt")  
    
    
    


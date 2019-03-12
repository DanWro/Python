a=17
s=0
while a>0:      #dopóki zostały jakieś cyfry
    s=s+(a%10)     #dodaj ostatnią cyfrę (jedności)
    a=a//10       #podziel liczbę przez 10 
print( "suma: "+ str(s)) #wypisz sumę
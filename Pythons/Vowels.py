reduta = 'Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi.'
spolgloski = ['a','ą','e','ę','i','o','u','y']
ilosc = [0,0,0,0,0,0,0,0]
n = 0

while(True):
    for litera in reduta:
        #print(litera)
        if litera == spolgloski[n]:
            ilosc[n] = ilosc[n] + 1
        
    n = n + 1
    if n == 8:
        break
    
for x in range(0, 8, 1):
    print(spolgloski[x],'=',ilosc[x])


PIN="0805"
i=0
while True:
    i=i+1
    pin=str(input("podaj pin : "))
    if PIN == pin :
        print("super")
    if PIN != pin:
        print("kod niepoprawny")
    if i == 3:
       break
print("po ptakach")
        

        
        
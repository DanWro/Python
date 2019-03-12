x=int(input("wprowadz liczbe od 1 do 10 : "))
i=0
while True:
   i=i+1
   if i < 2:
       print(x , " x " , i , " = " , x*(i))
       continue
   if i < 10:
       print(x , " x " , i+1 , " = " , x*(i+1))
    
    
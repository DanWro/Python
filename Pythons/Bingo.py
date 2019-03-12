
i=0
while True:
 while i < 50:
    i=i+1
    if i%3==0: 
        print("BIM")
        continue
    if i%5==0:
        print("BAM")
        continue
    if i%3==0 and i%5==0:
        print("BINGO")
        continue
    print(i)
   

     
def BMI(x,y):
    return (y/(x**2)*10000)
x=int(input("Podaj swój wzrost : " ))
y=int(input("Podaj swoją wage : " ))
def ok(w):
    if w in range(m,M):
        return "jest poprawne"
    else:
        return "jest złe"
w=int(input("podaj BMI : "))
m=18
M=25
print("Twoje BMI wynosi : ", round(BMI(x,y),2), ok(w))     
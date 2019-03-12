def BMI(x,y):
    w=(y/(x**2)*10000)
    return w
print(round(BMI(180,77),2))

def ok(func,m,M):
    for func in range(m,M):
        return True
    else:
        return False
    
print(ok(BMI,18,25))
    
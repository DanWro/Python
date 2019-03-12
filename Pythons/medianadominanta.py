tab=[5,6,4,7]
t=sorted(tab)
if len(t)%2!=0:
    print((len(t)+1)/2)
else:
    print((len(t)/2+len(tab)/2+1)/2)
print(tab)
print(t)
tab=[2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4,3]
tab.sort()
if len(tab)%2!=0:
    print((len(tab)+1)/2)
else:
    print((len(tab)/2+len(tab)/2+1)/2)
print(tab)
n = int(input("Podaj wymiar macierzy: "))
x = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(i+1, n):
        s = int(input("Podaj element (" + str(i) + "," + str(j) + "): "))
        x[i][j] = s
        x[j][i] = s

print("Wczytana macierz:")
for i in range(n):
    print(" ".join(map(str, x[i])))
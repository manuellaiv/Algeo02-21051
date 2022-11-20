# Ambil matriks M
x = int(input("baris matriks A: "))
y = int(input("kolom matriks A: "))
M = [[0 for j in range (y)] for i in range (x)]
for i in range (x):
    for j in range (y):
       M[i][j] = int(input("Masukkan nilai A" + f"[{str(i + 1)}]" + f"[{str(j + 1)}]" + ": "))
print("\nMatriks A: ")
for i in range(x):
    for j in range(y):
        print(M[i][j], end=" ")
    print()

# Ubah baris
def switchrow(M, i, j):
    M[i],M[j] = M[j],M[i]
    return M

# Kali baris dengan skalar
def multrow(M, s, i):
    a = len(M[0])
    for k in range(a):
        M[i][k] = s * M[i][k]
    return M   

# Tambahkan suatu baris dengan baris lainnya
def addrow(M, s, i, j):
    a = len(M[0])
    for k in range(a):
        M[i][k] += s * M[j][k]
    return M

# matriks segitiga atas
def toUpper(M):
    for i in range(len(M)):
        for ii in range(i+1, len(M)):
            r = M[ii][i]/M[i][i]
            for j in range(len(M[0])):
                M[ii][j] = M[ii][j] - r*M[i][j]
    return M

M = toUpper(M)
for i in range(len(M)):
    for j in range(len(M[0])):
        print(M[i][j], end=" ")
    print()
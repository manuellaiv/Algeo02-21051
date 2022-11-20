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

# Mencari lambda*I

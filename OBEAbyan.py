import numpy as np
from tabulate import tabulate

# n = ukuran matriks persegi
n = 2
A = [[3, 0],
    [8, -1]]
# print("A=")
# print(tabulate(A))

def eigens(A, ulang=100000):
    M = np.copy(A)
    n = M.shape[0]
    V = np.eye(n)
    for k in range(ulang):
        s = M.item(n-1, n-1)
        smult = s * np.eye(n)
        Q, R = np.linalg.qr(np.subtract(M, smult))
        M = np.add(R @ Q, smult)
        V = V @ Q
        # if k % 10000 == 0:
            # print("A",k,"=")
            # print(tabulate(Ak))
            # print("\n")
    return M, V

M, V = eigens(A)

# print("Eigenvektor: ")
# print(QQ)
# r = np.diag(Ak)
# print("Eigenvalue: ")
# print(r)


[V1,M1] = np.linalg.eig(A)
print(M1)
print(M)
print()
print(V)
print(V1) 


# import numpy as np

# # Ambil matriks M
# x = int(input("baris matriks A: "))
# y = int(input("kolom matriks A: "))
# M = [[0 for j in range (y)] for i in range (x)]
# for i in range (x):
#     for j in range (y):
#         M[i][j] = int(input("Masukkan nilai A" + f"[{str(i + 1)}]" + f"[{str(j + 1)}]" + ": "))
# print("\nMatriks A: ")
# for i in range(x):
#     for j in range(y):
#         print(M[i][j], end=" ")
#     print()

# # Ubah baris
# def switchrow(M, i, j):
#     M[i],M[j] = M[j],M[i]
#     return M

# # Kali baris dengan skalar
# def multrow(M, s, i):
#     a = len(M[0])
#     for k in range(a):
#         M[i][k] = s * M[i][k]
#     return M   

# # Tambahkan suatu baris dengan baris lainnya
# def addrow(M, s, i, j):
#     a = len(M[0])
#     for k in range(a):
#         M[i][k] += s * M[j][k]
#     return M

# # matriks segitiga atas
# def toUpper(Mn):
#     M = Mn
#     for i in range(len(M)):
#         for ii in range(i+1, len(M)):
#             r = float(M[ii][i]/M[i][i])
#             for j in range(len(M[0])):
#                 M[ii][j] = M[ii][j] - r*M[i][j]
#     return M

# # determinan
# def det(M):
#     d = 1
#     Mn = toUpper(M)

#     for i in range(len(Mn)):
#         d = d*Mn[i][i]
#     return d

# # Matriks identitas
# def identity():
#     dimensi = x
#     M[i][j] = np.identity(dimensi, dtype="float")
#     return(M[i][j])


# A = np.asmatrix(M)
# print(A)
# B = np.asmatrix(identity())
# print(B)

# # Matriks lambda*I
# def identity(M):
#     s = "T"
#     dimensi = x
#     M[i][j] = np.identity(dimensi, dtype="float")
#     M[i][j] = s * M[i][j]
#     return M
# print(identity(M))
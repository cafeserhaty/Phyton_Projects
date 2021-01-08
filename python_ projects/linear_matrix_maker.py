import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as lai
b=0
l=0
a = int(input("Denklem sayısını giriniz: "))
Matrix = np.zeros((a,a))
while  a > b :
 c=0
 while a > c :
  e = float(input("Değişkeni giriniz "))
  Matrix[b][c] = e
  c = c + 1
 b= b+1

Matrix2 = np.zeros((a,1))
while a > l:
 d = float(input("Cevapları giriniz "))
 Matrix2[l][0] = d
 l = l + 1
xirtam = np.linalg.inv(Matrix)
sonuc = np.dot(xirtam,Matrix2)
print(sonuc)





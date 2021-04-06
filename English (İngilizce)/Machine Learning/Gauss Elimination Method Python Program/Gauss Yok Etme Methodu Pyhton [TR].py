# -*- coding: utf-8 -*-

# Gerekli kütüphanelerin iport edilmesi.
import numpy as np
import sys

# Bilinmeyen sayısının okunması
n = int(input('Bilinmeyen Sayısını Giriniz: '))

# Matrisi yerleştirmek için n e n+1 olacak şekilde
# 2 boyutlu bir nunpy dizisi oluşturup 0 ile dolduruyoruz.
a = np.zeros((n,n+1))

# Çözümleri tutmak için n boyutunda tek boyutlu bir
# nunpy dizisi oluşturuyoruz ve 0 ile dolduruyoruz.
x = np.zeros(n)

# Arttırılmış Katsayılar Matrisinin Okunması.
print('Arttırılmış Katsayılar Matrisinin Katsayılarını Girin [Agumented Matrix]:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input( 'M['+str(i)+']['+ str(j)+']='))

# Girilen matrisi ekrana yazdırma.
print("\n")
print(a)

# Gauss Yok Etme Metodu Uygulaması
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('Sıfıra Bölme Algılandı!')
        
    for j in range(i+1, n):
        ratio = a[j][i]/a[i][i]
        
        for k in range(n+1):
            a[j][k] = a[j][k] - ratio * a[i][k]


# Yerine koyma
x[n-1] = a[n-1][n]/a[n-1][n-1]

for i in range(n-2,-1,-1):
    x[i] = a[i][n]
    
    for j in range(i+1,n):
        x[i] = x[i] - a[i][j]*x[j]
    
    x[i] = x[i]/a[i][i]

# Sonuçları ekrana yazdırma
print('\nRequired solution is: ')
for i in range(n):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')
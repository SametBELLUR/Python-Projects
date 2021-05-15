# -*- coding: utf-8 -*-

# Gerekli Kütüphanelerin İmport Edilmesi
import numpy as np
import sys
from sklearn.metrics import r2_score

# Manuel Çoklu Doğrusal Regresyon
def coklu_dogrusal_regresyon (x1,x2,y):
    n= len(x1)
    y_toplam= sum(y)
    x1_toplam= sum(x1)
    x2_toplam= sum(x2)
    x1_kareler_toplami = 0
    x2_kareler_toplami = 0
    x1_x2_carpimlar_toplami= 0
    x1_y_carpimlar_toplami= 0
    x2_y_carpimlar_toplami= 0
    
    for i in range(n):
        x1_kareler_toplami += x1[i]*x1[i]
    
    for i in range(n):
        x2_kareler_toplami += x2[i]*x2[i]
    
    for i in range(n):
        x1_x2_carpimlar_toplami += x1[i]*x2[i]
        
    for i in range (n):
        x1_y_carpimlar_toplami += x1[i]*y[i]
        
    for i in range (n):
        x2_y_carpimlar_toplami += x2[i]*y[i]
    
    print("n ------> ",n)
    print("∑y -----> ",y_toplam)
    print("∑x1 ----> ",x1_toplam)
    print("∑x2 ----> ",x2_toplam)
    print("∑x1^2 --> ",x1_kareler_toplami)
    print("∑x2^2 --> ",x2_kareler_toplami)
    print("∑x1*x2 -> ",x1_x2_carpimlar_toplami)
    print("∑x1*y --> ",x1_y_carpimlar_toplami)
    print("∑x2*y --> ",x2_y_carpimlar_toplami)
    print("\nDenklem Sistemi:")
    print(f"\n{n}*β0 + {x1_toplam}*β1 + {x2_toplam}*β2 = {y_toplam}")
    print(f"{x1_toplam}*β0 + {x1_kareler_toplami}*β1 + {x1_x2_carpimlar_toplami}*β2 = {x1_y_carpimlar_toplami}")
    print(f"{x2_toplam}*β0 + {x1_x2_carpimlar_toplami}*β1 + {x2_kareler_toplami}*β2 = {x2_y_carpimlar_toplami}")
    
# Gauss Yok Etme Metodu ile Denklem Sisteminin Çözümü // Algoritmanın detayları için :
# https://github.com/SametBELLUR/Python-Projects/tree/main/T%C3%BCrk%C3%A7e%20(Turkish)/Lineer%20Cebir
    
    print("\nArttırılmış Katsayılar Matrisi:")
    
    a = np.zeros((3,4))
    x = np.zeros(3)

# Arttırılmış Katsayılar Matrisinin Atanması.
    a[0][0] = n
    a[0][1] = x1_toplam
    a[0][2] = x2_toplam
    a[0][3] = y_toplam
    
    a[1][0] = x1_toplam
    a[1][1] = x1_kareler_toplami
    a[1][2] = x1_x2_carpimlar_toplami
    a[1][3] = x1_y_carpimlar_toplami
    
    a[2][0] = x2_toplam
    a[2][1] = x1_x2_carpimlar_toplami
    a[2][2] = x2_kareler_toplami
    a[2][3] = x2_y_carpimlar_toplami
    
    print("\n",a)
    
# Gauss Yok Etme Metodu Uygulaması
    for i in range(3):
        if a[i][i] == 0.0:
            sys.exit('Sıfıra Bölme Algılandı!')
        
        for j in range(i+1, 3):
            oran = a[j][i]/a[i][i]
        
            for k in range(4):
                a[j][k] = a[j][k] - oran * a[i][k]

# Yerine koyma
    x[2] = a[2][3]/a[2][2]

    for i in range(1,-1,-1):
        x[i] = a[i][3]
    
        for j in range(i+1,3):
            x[i] = x[i] - a[i][j]*x[j]
    
        x[i] = x[i]/a[i][i]

# Sonuçları ekrana yazdırma
    print('\nBulunan Değişkenler: [Gauss Eleme Metodu]\n')
    for i in range(3):
        print('β%d = %0.2f' %(i,x[i]), end = '\t')
    print(f"\n\nBulunan Fonsiyon: y = {round(x[0])} + {round(x[1])}*X1 + {round(x[2])}*X2")
    return x

def fonk_uygula (beta,x1,x2):
    tahmin = round(beta[0]) + round(beta[1])*x1 + round(beta[2])*x2
    #print(f"Tahmin: {tahmin}")
    return tahmin

def fonk_test (x1_test,x2_test,y_test,beta):
    tahmin = []
    print ("\nGerçek Değer:     Tahmin:")
    for i in range (len(x1_test)):
        tahmin.append(fonk_uygula(beta,x1_test[i],x2_test[i]))
        print(y_test[i],"           ",tahmin[i])
    
    print ("\nr2 Score: ",r2_score(y_test,tahmin))
    
    """
    y2 = DataFrame (y_test)
    thm = DataFrame (tahmin)
    RSS = sum((y2 - thm)**2)
    TSS = sum((y2 - np.mean(y2))**2)
    R2 = 1 - (RSS/TSS)
    print(R2)
    """
    
def main ():
    x1= [3,2,4,2,3,2,5,4]
    x2= [2,1,3,1,2,2,3,2]
    y= [78800,74300,83800,74200,79700,74900,88400,82900]
    
    x1_test= [3,2,4,2,3,2,5,4]
    x2_test= [2,1,3,1,2,2,3,2]
    y_test= [78800,74300,83800,74200,79700,74900,88400,82900]

    beta= coklu_dogrusal_regresyon(x1,x2,y)
    
    #fonk_uygula (beta,2,1)
    fonk_test(x1_test,x2_test,y_test,beta)

main()
# -*- coding: utf-8 -*-

# Importing Required Libraries
import numpy as np
import sys
from sklearn.metrics import r2_score

# Manual Multiple Linear Regression
def multiple_linear_regression (x1,x2,y):
    n= len(x1)
    y_sum= sum(y)
    x1_sum= sum(x1)
    x2_sum= sum(x2)
    x1_sqr_sum = 0
    x2_sqr_sum = 0
    x1_x2_mlt_sum= 0
    x1_y_mlt_sum= 0
    x2_y_mlt_sum= 0
    
    for i in range(n):
        x1_sqr_sum += x1[i]*x1[i]
    
    for i in range(n):
        x2_sqr_sum += x2[i]*x2[i]
    
    for i in range(n):
        x1_x2_mlt_sum += x1[i]*x2[i]
        
    for i in range (n):
        x1_y_mlt_sum += x1[i]*y[i]
        
    for i in range (n):
        x2_y_mlt_sum += x2[i]*y[i]
    
    print("n ------> ",n)
    print("∑y -----> ",y_sum)
    print("∑x1 ----> ",x1_sum)
    print("∑x2 ----> ",x2_sum)
    print("∑x1^2 --> ",x1_sqr_sum)
    print("∑x2^2 --> ",x2_sqr_sum)
    print("∑x1*x2 -> ",x1_x2_mlt_sum)
    print("∑x1*y --> ",x1_y_mlt_sum)
    print("∑x2*y --> ",x2_y_mlt_sum)
    print("\nDenklem Sistemi:")
    print(f"\n{n}*β0 + {x1_sum}*β1 + {x2_sum}*β2 = {y_sum}")
    print(f"{x1_sum}*β0 + {x1_sqr_sum}*β1 + {x1_x2_mlt_sum}*β2 = {x1_y_mlt_sum}")
    print(f"{x2_sum}*β0 + {x1_x2_mlt_sum}*β1 + {x2_sqr_sum}*β2 = {x2_y_mlt_sum}")
    
# Solution of the System of Equations with the Gaussian Elimination Method // For details of the algorithm:
# https://github.com/SametBELLUR/Python-Projects/tree/main/English%20(%C4%B0ngilizce)/Linear%20Algebra
    
    print("\nAugmented Coefficient Matrix:")
    
    a = np.zeros((3,4))
    x = np.zeros(3)

# Assignment of Augmented Coefficient Matrix.
    a[0][0] = n
    a[0][1] = x1_sum
    a[0][2] = x2_sum
    a[0][3] = y_sum
    
    a[1][0] = x1_sum
    a[1][1] = x1_sqr_sum
    a[1][2] = x1_x2_mlt_sum
    a[1][3] = x1_y_mlt_sum
    
    a[2][0] = x2_sum
    a[2][1] = x1_x2_mlt_sum
    a[2][2] = x2_sqr_sum
    a[2][3] = x2_y_mlt_sum
    
    print("\n",a)
    
# Gaussian Elimination Method Application.
    for i in range(3):
        if a[i][i] == 0.0:
            sys.exit('Division by Zero Detected!')
        
        for j in range(i+1, 3):
            ratio = a[j][i]/a[i][i]
        
            for k in range(4):
                a[j][k] = a[j][k] - ratio * a[i][k]

# Back Substitution.
    x[2] = a[2][3]/a[2][2]

    for i in range(1,-1,-1):
        x[i] = a[i][3]
    
        for j in range(i+1,3):
            x[i] = x[i] - a[i][j]*x[j]
    
        x[i] = x[i]/a[i][i]

# Printing the results to the screen.
    print('\nVariables Found: [Gaussian Elimination Method]\n')
    for i in range(3):
        print('β%d = %0.2f' %(i,x[i]), end = '\t')
    print(f"\n\nFound Function: y = {round(x[0])} + {round(x[1])}*X1 + {round(x[2])}*X2")
    return x

def func_apply (beta,x1,x2):
    prediction = round(beta[0]) + round(beta[1])*x1 + round(beta[2])*x2
    #print(f"Prediction: {prediction}")
    return prediction

def func_test (x1_test,x2_test,y_test,beta):
    prediction = []
    print ("\nReal Value:     Prediction:")
    for i in range (len(x1_test)):
        prediction.append(func_apply(beta,x1_test[i],x2_test[i]))
        print(y_test[i],"           ",prediction[i])
    
    print ("\nr2 Score: ",r2_score(y_test,prediction))
    
def main ():
    x1= [3,2,4,2,3,2,5,4]
    x2= [2,1,3,1,2,2,3,2]
    y= [78800,74300,83800,74200,79700,74900,88400,82900]
    
    x1_test= [3,2,4,2,3,2,5,4]
    x2_test= [2,1,3,1,2,2,3,2]
    y_test= [78800,74300,83800,74200,79700,74900,88400,82900]

    beta= multiple_linear_regression(x1,x2,y)
    
    #func_apply (beta,2,1)
    func_test(x1_test,x2_test,y_test,beta)

main()
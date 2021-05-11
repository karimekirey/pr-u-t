import pandas as pd
from matplotlib import pyplot as plt
#Será necesario conocer un rango de valores que podamos proporcionarle a las variables 

print('Teniendo en cuenta la ecuación Vf=(P1*Vi/P2)')
P1=int(input('Introduce el valor de P1: '))
P2=int(input('Introduce el valor de P2: '))
Vi=int(input('Introduce el valor de Vi: '))
Vf=(P1*Vi/P2)

#El volumen final es un factor de incremento por lo que el volumen total podría ser representado como la suma de Vf y Vi

Vt=Vf+Vi
print('Solución de Vf: ', Vf)
print('Solución de Vt: ', Vt)

#Gráfica de la relacón de variables al incremento de la P2 

x=[Vi,Vf]
y=[P1,P2]
plt.plot(x,y)
plt.title("Relación: Volumen/Presón")
plt.xlabel("Volumen")
plt.ylabel("Presión")
plt.grid()
plt.show()

#Gráfica del volumen total 

x=[Vi,Vt]
y=[P1,P2]
plt.plot(x,y)
plt.title("Volumen total")
plt.xlabel("Volumen")
plt.ylabel("Presión")
plt.grid()
plt.show()

import math
#Ahora realizamos los calculos de Tensión Máxima 

print('Teniendo el cuenta la ecuación Tmax=P(a*b)**2/w(a**2+b**2)c')
P=int(input('Introduce el valor de P: '))
a=int(input('Introduce el valor de a: '))
b=int(input('Introduce el valor de b: '))
c=int(input('Introduce el valor de c: '))
w=int(input('Introduce el valor de w: '))

Tmax=(P*((a*b)**2))/((w)*((a**2)+(b**2))*c)

#Podemos calcular de igual manera el volumen, este sería el volumen inicial que sería introducido en el desarrollo anterior

Vi= ((4/3)*(math.pi)*(a**2)*(b))

print('Solución de Tmax: ', Tmax)
print('Solucion de Vi:', Vi)

#Podemos graficar la relacón de la tensión con varias variables, en este caso con el Volumen inicial

x=[0,Vi]
y=[0,Tmax]
plt.plot(x,y)
plt.title("Relacón: Tensión/Volumen")
plt.xlabel("Volumen")
plt.ylabel("Tensón")
plt.grid()
plt.show()

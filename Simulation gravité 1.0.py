from math import * 
import cmath

import matplotlib.pyplot as plt
#constante grav
G=10**(-2)

#position initiale
X=[-3]
Y=[14]
#vitesse initiale
Vx=[0.01]
Vy=[-0.08]
vx=Vx[0]
vy=Vy[0]
#masse de l'objet
M=2


for i in range(1,100000):
    d=sqrt(X[i-1]**2+Y[i-1]**2)

    a=G*M/(d**2)
    ax=-a*X[i-1]/d
    ay=-a*Y[i-1]/d
    Vx.append(Vx[i-1]+ax)
    Vy.append(Vy[i-1]+ay)
    X.append(X[i-1]+Vx[i])
    Y.append(Y[i-1]+Vy[i])
plt.figure(figsize = [7,7])
plt.axis([-20,20,-20,20])
plt.scatter(X,Y,marker='$.$',s=0.55)
plt.plot([0],[0],'X',color='orange')
plt.plot([X[0]],[Y[0]],'o',color='red')
plt.show()


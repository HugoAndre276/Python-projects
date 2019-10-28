from math import * 
import cmath
import matplotlib.pyplot as plt
#cste grav
G=10**(-2)

#pos init
X1=[1]
Y1=[1]

X2=[0]
Y2=[0]

#vitesse init
v1 = (-0.05,0.05)
v2 = (0.05,-0.05)

#masse
m1=5
m2=1

for i in range(1,100000):
    d=sqrt((X1[i-1]-X2[i-1])**2+(Y1[i-1]-Y2[i-1])**2)
    F=G*m1*m2/(d**2)
    
    na1=F/m1
    na2=F/m2
    
    a1=(na1*(X2[i-1]-X1[i-1])/d,na1*(Y2[i-1]-Y1[i-1])/d)
    a2=(na2*(X1[i-1]-X2[i-1])/d,na2*(Y1[i-1]-Y2[i-1])/d)
    
    v1=(v1[0]+a1[0],v1[1]+a1[1])
    v2=(v2[0]+a2[0],v2[1]+a2[1])
    
    X1.append(X1[i-1]+v1[0])
    Y1.append(Y1[i-1]+v1[1])

    X2.append(X2[i-1]+v2[0])
    Y2.append(Y2[i-1]+v2[1])

plt.figure(figsize=[7,7])
#plt.axis([-20,20,-20,20])
plt.scatter(X1,Y1,marker='$.$',s=0.55,color='blue')
plt.scatter(X2,Y2,marker='$.$',s=0.55,color='orange')
plt.plot([X1[0]],[Y1[0]],'X',color='blue')
plt.plot([X2[0]],[Y2[0]],'X',color='orange')
plt.show()

    

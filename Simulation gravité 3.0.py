from math import * 
import cmath
import matplotlib.pyplot as plt
#cste grav
G=10**(-1)

#pos init
X1=[100]
Y1=[-500]

X2=[200]
Y2=[-100]

#vitesse init
v1 = (-0.05,0.01)
v2 = (0.05,-0.1)

#masse
m1=10
m2=800

#rayon
r1=10
r2=20
cld = False

plt.figure(figsize=[7,7])
plt.axis('equal')
plt.text(0.8,0.15,'G=%s \n m1=%s \n m2=%s \n r1=%s \n r2=%s \n v1=%s \n v2=%s'
    %(G,m1,m2,r1,r2,v1,v2) ,horizontalalignment='center',
    verticalalignment='center', transform = plt.gca().transAxes)

for i in range(1,100000):
    d=sqrt((X1[i-1]-X2[i-1])**2+(Y1[i-1]-Y2[i-1])**2)
    if d<r1+r2:
        cld = True
        break
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




plt.scatter(X1,Y1,marker='$.$',s=10,color='blue')
plt.scatter(X2,Y2,marker='$.$',s=10,color='orange')
plt.plot([X1[0]],[Y1[0]],'X',color='blue',label='Objet 1')
plt.plot([X2[0]],[Y2[0]],'X',color='orange',label='Objet 2')
plt.legend(framealpha=1, frameon=True)

p=i

#moyenne
if cld == True:
    p=i-1
    x=(X1[p]+X2[p]+((X2[p]-X1[p])*(r1-r2))/d)/2
    y=(Y1[p]+Y2[p]+((Y2[p]-Y1[p])*(r1-r2))/d)/2
    plt.plot([x],[y],'X',color='red')


c1=plt.Circle((X1[p],Y1[p]),r1,color='blue')
c2=plt.Circle((X2[p],Y2[p]),r2,color='orange')
plt.gca().add_artist(c1)
plt.gca().add_artist(c2)

plt.show()

    

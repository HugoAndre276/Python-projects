from PIL import Image
from PIL import ImageFilter
from PIL.Image import *
from math import *
import cmath
import matplotlib
import matplotlib.pyplot as plt


path = "/Prog/Python/Fourier/"
img = open(path+"698.png")
width, height = img.size

#Bornes initiales
xmin = width/2
xmax = width/2
ymin=height/2
ymax=height/2

xi = [] #liste des x
yi = [] #liste des y
f = 0 #fréquence
smr = 0 #somme réelle
smi = 0 #somme imaginaire
sm = [] #liste des sommes pour chaque fréquence
fi = [] #liste des fréquences


#remplacer les pixels non voulus
for x in range(width):
    for y in range(height):
        r,g,b,a = img.getpixel((x,y))
        if ((r+g)/2)-b>=-40:
            img.putpixel((x,y),(255,255,255))

#rogner l'image
for x in range(width):
    for y in range(height):
        r,g,b,a = img.getpixel((x,y))
        if (r,g,b) != (255,255,255):
            if x<xmin:
                xmin=x
            if y<ymin:
                ymin=y
            if x>xmax:
                xmax=x+1
            if y>=ymax:
                ymax=y+1
box = (xmin,ymin,xmax,ymax)
img = img.crop(box)

#nouvelles dimensions
width, height = img.size

#entrer les temps bornes
tmin= float(input("Temps minimal: "))
tmax= float(input("Temps maximal: "))

dt = tmax - tmin


for x in range(width):
        for y in range(height):
            r,g,b,a = img.getpixel((x,y))
            if r<120:
                xi.append(x)
                yi.append(y)
                break

while f<20000:
    smr = 0
    smi = 0
    for i in range(len(xi)):
        smr = smr + (yi[i]+height/2)*cos(2*pi*xi[i]*f*dt/width)
        smi = smi + (yi[i]+height/2)*sin(2*pi*xi[i]*f*dt/width)
    sm.append(abs(smr-1j*smi)*dt)
    fi.append(f)
    f = f+1


plt.plot(fi,sm,'b-',linewidth=0.5)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.title("Fourier graph of a sound wave")
plt.show()
        





            


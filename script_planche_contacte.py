#!/usr/bin/python3.4

from PIL import Image
from math import ceil

#input largeur de la mozaic
mozaicGrid=3

#origines des boxes
x0=0
y0=0

#input images
images= ["Camera.001.0.png","Camera.002.0.png","Camera.001.12.png","Camera.002.12.png","Camera.001.18.png","Camera.001.24.png"]
nbImages=len(images)

#liste des images PIL
carreaux=[]
for image in images:
    carreaux.append(Image.open(image))

#def de la taille de la mozaic    
mozaicMaxSizeX = carreaux[0].size[0]*mozaicGrid
mozaicMaxSizeY = ceil(nbImages/mozaicGrid)*carreaux[0].size[1]
mozaicSize = (mozaicMaxSizeX,mozaicMaxSizeY)

mozaic=Image.new('RGBA',mozaicSize)

#coller chaque image sur la mozaic
for carreau in carreaux:

    x1=x0+carreau.size[0]
    y1=y0+carreau.size[1] 
    print(x0,y0,x1,y1)
    mozaic.paste(carreau,(x0,y0,x1,y1))
    x0=x1
    if x0 ==  mozaicMaxSizeX:

        y0=y0+carreau.size[1]
        x0=0
    print(carreau)
    

mozaic.show()


    

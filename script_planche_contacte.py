#!/usr/bin/python3.4

from PIL import Image

#input taille de la mozaic
mozaicSize=(100,100)

#input carreaux
carreaux= ["Camera.001.0.png","Camera.002.0.png","Camera.001.12.png","Camera.002.12.png"]
for images in carreaux:
    carreaux=Image.open(images)

print("carreaux")

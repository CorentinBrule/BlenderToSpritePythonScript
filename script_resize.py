#!/usr/bin/python3.4
# coding: utf8

from PIL import Image
import os,sys 

inputPath=sys.argv[1]
outputPath=sys.argv[2]
img = Image.open(inputPath)
print("actual size : ",img.size[0],"x",img.size[1]," pixels.")
newSizeX=int(input("enter new size x : "))
newSizeY=int(input("enter new size y : "))
img = img.resize((newSizeX,newSizeY))
img.save(outputPath)



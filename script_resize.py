from PIL import Image
import os,sys 

inputPath=sys.argv[1]
outputPath=sys.argv[2]
img = Image.open(inputPath)
img = img.resize((1000,1000))
img.save(outputPath)



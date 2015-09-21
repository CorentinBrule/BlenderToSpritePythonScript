from PIL import Image

img = Image.open('testrendu1/Camera.001.0.png')
img = img.resize((1000,1000))
img.save('testrendu1/resized_image.png')



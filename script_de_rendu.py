import bpy
from PIL import Image #Rah putain mais pourquoi je n'arrive pas à l'importer ce foutu module !!! 

cameras=[]
temps_animation=(bpy.data.scenes['Scene'].frame_end)-(bpy.data.scenes['Scene'].frame_start-1)
nb_rendus=temps_animation/5
frame_to_render=[0,6,12,18,24]
fp = bpy.data.scenes['Scene'].render.filepath
bpy.data.scenes['Scene'].render.image_settings.file_format = 'PNG'

#define wich is camera
for object in bpy.data.objects:
    if object.type == 'CAMERA':
       cameras.append(object)

#make render for all cameras and for frames defined      
for camera in cameras : 
    bpy.context.scene.camera = camera
    for frame in frame_to_render :
        bpy.data.scenes['Scene'].frame_current=frame
        image_name = fp + str(camera.name) +'.'+ str(frame)
        bpy.data.scenes['Scene'].render.filepath = image_name
        bpy.ops.render.render(write_still=True)
        #img = Image.open(image_name)
bpy.data.scenes['Scene'].render.filepath = fp        
        

#!/usr/bin/python
import pi3d
import pyxlib
display = pi3d.Display.create(x=50,y=50)
shader = pi3d.Shader("star") # -- Type of shading
tex = pi3d.Texture("textures/radar.png") # -- Image of a Cube 
box = pi3d.Cuboid(x=0,y=0,z=2.2) # -- Length, Breadth, Height
box.set_draw_details(shader,[tex]) # -- Create box

tm = 0.0
dt = 0.01
sc = 0.0
ds = 0.001

mykeys = pi3d.Keyboard()

while display.loop_running():
   box.set_custom_data(48, [tm, sc, -0.5 * sc])
   tm += dt
   sc = (sc + ds) % 10.0
   box.rotateIncX(0.01)
   box.rotateIncY(0.071)
   box.draw()
   if mykeys.read() == 27:
      mykeys.close()
      display.destroy()
      break


 



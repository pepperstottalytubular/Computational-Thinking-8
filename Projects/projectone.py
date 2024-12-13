###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background("magenta-blue-teal-gradient-colorful-600nw-2137060107.webp")
q1 = codesters.Square(100, 100, 200, 'blue') 
q2 = codesters.Square(-100, 100, 200, 'black')
q3 = codesters.Square(-100, -100, 200, 'deeppink')
q4 = codesters.Square(100, -100, 200, 'black')
s1 = codesters.Sprite("pngtree-star-vector-icon-png-image_696411.png", 100, 100)
s1.set_size(0.5)
s2 = codesters.Sprite("cardinal", -100, -100)
s2.set_size(1.0)
s3 = codesters.Sprite("bg,f8f8f8-flat,750x,075,f-pad,750x1000,f8f8f8.png", 100, -100)
s3.set_size(0.2)
s4 = codesters.Sprite("cardinal", -100, 100)
s4.set_size(1.0)
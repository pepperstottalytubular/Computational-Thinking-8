# section one set up

import codesters, random
from codesters import StageClass
stage = StageClass()
stage.disable_floor()
player=codesters.Sprite("tvgirl")
stage.set_background("race")
player.set_size(0.25)

points=0
#section 2- objects 
def Falling_object():
    global points
    if points !=15:
        y=250
        x=random.randint(-250,250)
        object=codesters.Sprite("star",x,y)
        object.set_y_speed (-2)
stage.event_interval(Falling_object,2)
## draw game levels using strings
## use while and if

## the following line is just MAGIC ##############################################
## we need it to be able to draw images on the screen ############################
from medialib import *
initialize() # always the first instruction of the program
##################################################################################

trees = " BM     B  B"
floor = "GGGWWWGGGWGG"
clear()
## B: tileBush.png       M: tileMushroom.png
## G: tileGround.png     W: tileWater.png
## The width of each is 64.

x = 0
y=100 ##draw the imagese of floor in y=100


x = 0
y_Mushroom=60  ##draw the imagese of Mushroom in y=60
y_Bush=70      ##draw the imagese of Bush in y=70


## 1) draw as defined in trees and floor, then change the tiles, to have 2 more mushrooms!

## 2) reverse the 2 strings above so the whole image becomes mirrored.

text("click anywhere with the left mouse button to finish", 10,500,16)
wait_mouse_leftclick() # left-click your mouse to continue

all_done() # always the last instruction of the program

## tiles are from
## https://opengameart.org/content/free-platformer-game-tileset
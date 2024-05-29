#Liz Martin "Blizard Lizard Catclark Script"
#Catclark your Geo, yo.

import maya.cmds as cmds
import random

def catclarkscript() :

	sel = cmds.ls(sl=1)
	for catclark in sel:
		cmds.select(catclark, r=True)
		cmds.setAttr(".aiSubdivType", 1) 
		cmds.setAttr(".aiSubdivIterations", 3) 
catclarkscript()

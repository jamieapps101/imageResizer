#!/usr/bin/python3

from PIL import Image
import sys,os

args = sys.argv
nArgs = len(sys.argv)

xScale = 0.5
yScale = 0.5

if(nArgs == 2):
    pathArg = sys.argv[1]
    imageRef = Image.open(pathArg)
    imageSize = imageRef.size
    print("Current image size: {}".format(imageSize))
    newImageSize = (int(imageSize[0]*xScale),int(imageSize[1]*yScale))
    print("New image size: {}".format(newImageSize))
    imageRefResized = imageRef.resize(newImageSize,Image.ANTIALIAS)
    dotPos = pathArg.rfind(".")
    path = pathArg[:dotPos]
    type = pathArg[dotPos:]
    #os.rename(pathArg, path+"Old"+type)
    #imageRefResized.save(pathArg,quality=85)
    imageRefResized.save(path+"Mod"+type,quality=100)

elif(nArgs == 3):
    pathArg = sys.argv[1]
    sizeArg = sys.argv[2]
    print("I got:{}".format(sizeArg))
    a = int(sizeArg.rfind('(')+1)
    b = int(sizeArg.rfind(','))
    c = int(sizeArg.rfind(',')+1)
    d = int(sizeArg.rfind(')'))
    imageRef = Image.open(pathArg)
    imageSize = imageRef.size
    xVal = sizeArg[a:b]
    yVal = sizeArg[c:d]
    newImageSize = None
    if sizeArg[0] == "s": #ie scale mode
        print("Scale mode")
        newImageSize = (int(imageSize[0]*float(xVal)),int(imageSize[1]*float(yVal)))
    elif sizeArg[0] == "p": # ie pixel mode
        print("Pixel Mode")
        newImageSize = (int(xVal),int(yVal))

    print("Current image size: {}".format(imageSize))

    print("New image size: {}".format(newImageSize))
    imageRefResized = imageRef.resize(newImageSize,Image.ANTIALIAS)
    dotPos = pathArg.rfind(".")
    path = pathArg[:dotPos]
    type = pathArg[dotPos:]
    #os.rename(pathArg, path+"Old"+type)
    #imageRefResized.save(pathArg,quality=85)
    imageRefResized.save(path+"Mod"+type,quality=100)
else:
    print("Which pic though?")

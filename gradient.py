from PIL import Image
import glob, os, math

import tupleFunctions as tf

startColor = (66, 138, 255)
endColorX = (65, 255, 217)
endColorY = (118, 65, 255)
size = (500, 500)

im = Image.new("RGB", size, 'black')
pixels = im.load()

deltaX = ((endColorX[0]-startColor[0]) / float(size[0]), (endColorX[1]-startColor[1]) / float(size[0]), (endColorX[2]-startColor[2]) / float(size[0]))
deltaY = ((endColorY[0]-startColor[0]) / float(size[0]), (endColorY[1]-startColor[1]) / float(size[0]), (endColorY[2]-startColor[2]) / float(size[0]))
print deltaX, " DELTA X"
print deltaY, " DELTA Y"
print

thisPixelX = ()
thisPixelY = ()

for j in range(im.size[1]):    # for every pixel:
    if (j != 0):
        thisPixelY = tf.addTuples(thisPixelY, deltaY)
    else:
        thispixelY = startColor

    for i in range(im.size[0]):
        if (i == 0 and j == 0) :
            thisPixelX = startColor
            thisPixelY = startColor
            pixels[i,j] = startColor
            continue
        if (i != 0):
            thisPixelX = tf.addTuples(thisPixelX, deltaX)
        else:
            thisPixelX = startColor
        add = tf.divTuple(tf.addTuples(thisPixelY, thisPixelX), 2)
        pixels[i,j] = tf.roundTuple(add)

im.show()

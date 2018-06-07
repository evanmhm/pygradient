from PIL import Image
import glob, os, math
import sys
from ast import literal_eval as make_tuple
import tupleFunctions as tf



def make_gradient(start_color, end_color_x, end_color_y, size):
	startColor = start_color
	endColorX = end_color_x
	endColorY =  end_color_y
	size = size
	im = Image.new("RGB", size, 'black')
	pixels = im.load()

	deltaX = ((endColorX[0]-startColor[0]) / float(size[0]), (endColorX[1]-startColor[1]) / float(size[0]), (endColorX[2]-startColor[2]) / float(size[0]))
	deltaY = ((endColorY[0]-startColor[0]) / float(size[0]), (endColorY[1]-startColor[1]) / float(size[0]), (endColorY[2]-startColor[2]) / float(size[0]))
	print(deltaX, " DELTA X")
	print(deltaY, " DELTA Y")


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

	return im
	
if __name__ == '__main__':
	i = make_gradient(make_tuple(sys.argv[1]), make_tuple(sys.argv[2]), make_tuple(sys.argv[3]), make_tuple(sys.argv[4]))
	i.show()

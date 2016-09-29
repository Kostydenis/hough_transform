import sys
from PIL import Image
import matplotlib.pyplot as plt
import math
import json

import numpy as np
np.set_printoptions(threshold=np.inf)

EMPTY = 255
FILLED = 0

# THETA_MIN = math.radians(-180)
# THETA_MAX = math.radians(180)

THETA_MIN = math.radians(-200)
THETA_MAX = math.radians(200)

def isEmpty(dot):
	if dot == EMPTY:
		return True
	return False
def isFilled(dot):
	if dot == FILLED:
		return True
	return False
###############

# convert rectangle coordinates to polar
def rect2pol(x, y, theta):
	return x * math.cos(theta) + y * math.sin(theta)


def transform(in_img_name):
	img = Image.open(in_img_name)

	(width, height) = img.size
	img_map = np.array(list(img.getdata()))
	img_map = img_map.reshape((height, width))

	output = []
	indicesX = []
	indicesY = []

	for row_index, row_value in enumerate(img_map):
		for pix_index, pix_value in enumerate(row_value):
			if isFilled(pix_value):
				curr_output = []
				for theta in np.arange(THETA_MIN, THETA_MAX, 0.1):
					curr_output.append(rect2pol(pix_index, row_index, theta))
				indicesX.append(pix_index)
				indicesY.append(row_index)
				print(pix_index)
				print(row_index)

				output.append(curr_output)

	for v,i in enumerate(output):
		plt.plot(i, label='('+str(indicesX[v])+','+str(indicesY[v])+')')

	plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
	box = plt.subplot().get_position()
	plt.subplot().set_position([box.x0, box.y0, box.width * 0.8, box.height])

	plt.savefig('out/' + in_img_name[4:-4] + '.png')
	plt.gcf().clear()
	f.close()

transform(sys.argv[1])

# transform('src/bw_diag_3_dots.png')
# transform('src/bw_vert_3_dots.png')
# transform('src/bw_hor_3_dots.png')
# transform('src/cor_big_center.png')
# transform('src/cor_lil_center.png')



from PIL import Image
import matplotlib.pyplot as plt
import math

import numpy as np
np.set_printoptions(threshold=np.inf)

EMPTY = 255
FILLED = 0

def isEmpty(dot):
	if dot == EMPTY:
		return True
	return False
def isFilled(dot):
	if dot == FILLED:
		return True
	return False
###############

img = Image.open('src/bw_line.png')
# img = Image.open('src/bw_straiht_lines.bmp')
# img = Image.open('src/gs_diag_lines.png')


(width, height) = img.size
img_map = np.array(list(img.getdata()))
img_map = img_map.reshape((height, width))

THETA_MIN = math.radians(-180)
THETA_MAX = math.radians(180)

output = []

for row_index, row_value in enumerate(img_map):
	for pix_index, pix_value in enumerate(row_value):
		if isFilled(pix_value):
			curr_output = []
			for theta in np.arange(THETA_MIN, THETA_MAX, 0.1):
				curr_output.append(pix_index * math.cos(theta) + row_index * math.sin(theta))

			output.append(curr_output)

# for i in output:
# 	plt.plot(i)

plt.plot(output[0])

plt.savefig('oneline.png')
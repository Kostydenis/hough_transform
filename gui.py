############## imports ##############
import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

import tkinter as tk
from tkinter import *
import random
import math
import randomcolor
############## END imports ##############

############## params ##############
FIELD_WIDTH = 10 # cells
FIELD_HEIGHT = 10 # cells
CELL_SIZE = 40 # pix

THETA_MIN = math.radians(-90)
THETA_MAX = math.radians(90)

PLOT_DPI=80
############## END params ##############

root = tk.Tk()

f = Figure(figsize=(FIELD_WIDTH, FIELD_HEIGHT), dpi=PLOT_DPI)

canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)


field = [[0 for x in range(FIELD_WIDTH)] for y in range(FIELD_HEIGHT)]
rand_color = randomcolor.RandomColor()
colors = [[rand_color.generate()[0] for x in range(FIELD_WIDTH)] for y in range(FIELD_HEIGHT)]

# width x height + x_offset + y_offset:
root.geometry(str(CELL_SIZE*FIELD_WIDTH+FIELD_WIDTH*PLOT_DPI) + 'x' + str(CELL_SIZE*FIELD_HEIGHT+50))

def cb(e):
	place_dot(int(e.widget.winfo_x()/CELL_SIZE),
			int(e.widget.winfo_y()/CELL_SIZE),
			'invert')
	transform()


def place_dot(x,y,color='Black'):

	if color in ['Invert', 'invert']:
		color = 'White' if field[x][y] == 1 else colors[x][y]

	field[x][y] = 1 if not color=='White' else 0

	label = tk.Label(root,bg=color,relief=SUNKEN,borderwidth=1)
	label.place(x = (x)*CELL_SIZE,
			y = (y)*CELL_SIZE,
			width=CELL_SIZE,
			height=CELL_SIZE)
	label.bind("<Button-1>", lambda e: cb(e))

def isFilled(x,y):
	if field[x][y] == 1:
		return True
	return False
# convert rectangle coordinates to polar
def rect2pol(x, y, theta):
    return x * math.cos(theta) + y * math.sin(theta)
def pol2rect(r, theta):
    return (-math.cos(theta)/math.sin(theta))*x+(r/math.sin(theta))
def transform():

	output = []
	indicesX = []
	indicesY = []
	indicesColor = []

	f.clear()
	plt = f.add_subplot(111)

	for row_index, row_value in enumerate(field):
		for pix_index, pix_value in enumerate(row_value):
			if isFilled(pix_index,row_index):
				curr_output = []
				for theta in np.arange(THETA_MIN, THETA_MAX, 0.1):
					curr_output.append(rect2pol(pix_index, row_index, theta))
				indicesX.append(pix_index)
				indicesY.append(row_index)

				output.append(curr_output)

	for v,i in enumerate(output):
		plt.plot(i, label='('+str(indicesX[v])+','+str(indicesY[v])+')', color=colors[indicesX[v]][indicesY[v]])

	plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
	box = plt.get_position()
	plt.set_position([box.x0, box.y0, box.width * 1, box.height])
	f.subplots_adjust(left=0.05, right=0.8, top=0.95, bottom=0.05)
	canvas.draw()

def create_field():
	for i in range(FIELD_HEIGHT):
		for j in range(FIELD_WIDTH):
			place_dot(i,j, 'White')
	transform()

create_field()

clr_btn = tk.Button(root, text='Clear field')
clr_btn.place(x = 10,
			y = CELL_SIZE * FIELD_HEIGHT + 20)
clr_btn.bind("<Button-1>", lambda e: create_field())



root.mainloop()


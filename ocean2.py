import tkinter as tk
from random import uniform
import cell

def rgbToHex(red, green, blue):
	return "#%02x%02x%02x" % (red, green, blue) 

WIDTH  = 800
HEIGHT = 600
MARGIN = 5

CELL_SIZE = 5

cols = int((WIDTH - 2*MARGIN)/CELL_SIZE)
rows = int((HEIGHT - 2*MARGIN)/CELL_SIZE)

window = tk.Tk()

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)

# initialize all the cells
cells = []
for i in range(cols):
	for j in range(rows):
		x1 = i*CELL_SIZE + MARGIN
		y1 = j*CELL_SIZE + MARGIN
		x2 = i*CELL_SIZE + CELL_SIZE + MARGIN
		y2 = j*CELL_SIZE + CELL_SIZE + MARGIN
		a = int(uniform(5,200))
		cells.append(cell.Cell(canvas, x1, y1, x2, y2, uniform(80,100)/100))


while True:
	cells[int(uniform(0,len(cells)))].changeColor(0.8)
	window.update_idletasks()
	window.update()
	print("test")
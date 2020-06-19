import tkinter as tk
from random import uniform

def rgbToHex(red, green, blue):
	return "#%02x%02x%02x" % (red, green, blue) 

WIDTH  = 800
HEIGHT = 600
MARGIN = 5

CELL_SIZE = 5

cols = int((WIDTH - 2*MARGIN)/CELL_SIZE)
rows = int((HEIGHT - 2*MARGIN)/CELL_SIZE)

window = tk.Tk()

w = tk.Canvas(window, width=WIDTH, height=HEIGHT)
for i in range(cols):
	for j in range(rows):
		x1 = i*CELL_SIZE + MARGIN
		y1 = j*CELL_SIZE + MARGIN
		x2 = i*CELL_SIZE + CELL_SIZE + MARGIN
		y2 = j*CELL_SIZE + CELL_SIZE + MARGIN

		a = int(uniform(5,200))

		color = rgbToHex(a, a, 200)

		w.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
		w.pack()

window.mainloop()
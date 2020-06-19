import tkinter as tk


class Cell:
	"""
	Cell

	...

	Attributes
	----------
	coords : int
		includes: x1, y1, x2, y2. Location of where this cell is drawn
	canvas : tkinter Canvas object
		canvas on which cell will be drawn
	bfactor : int 0-1
		How "blue" the cell is. 1 is white, 0 is blue
	rect : tkinter Canvas Rectangle object
		objecting representing rectangle used to draw cell
	color: hex int
		rectangle's color as a hex value

	Methods
	-------
	rgbToHex(red, green, blue)
		input rgb value, returns its hex value
	setColor(red, green,  blue)
		changes the color of the rectangle 
	"""
	def __init__(self, canvas, x1, y1, x2, y2, bfactor):
		self.canvas = canvas
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		a = int(255*(1-bfactor))
		self.color = self.rgbToHex(a, a, 255)
		self.rect = canvas.create_rectangle(x1, y1, x2, y2, fill=self.color, outline="")
		canvas.pack()

	def rgbToHex(self, red, green, blue):
		""" input rgb value for a color and this function
		will return its hex value """
		return "#%02x%02x%02x" % (red, green, blue) 


	def changeColor(self, bfactor):
		a = int(255*(bfactor))
		self.canvas.itemconfig(self.rect, fill=self.rgbToHex(a, a, 255))
		print("test")
class Cell:

	# rgb should be inputted 
	def __init__(self, x1, y1, x2, y2, rgb):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.color = self.rgbToHex(rgb[0], rgb[1], rgb[2])

	def rgbToHex(self, red, green, blue):
		return "#%02x%02x%02x" % (red, green, blue) 
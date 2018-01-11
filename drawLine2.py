import numpy as np
from pylab import imshow, show

class Line:

	def __init__(self,interface,x_start,y_start,x_end, y_end):
		# Line(interface, xStart, yStart, xEnd, yEnd
		self.interface = interface
		self.x_start = x_start
		self.y_start = y_start
		self.x_end = x_end
		self.y_end = y_end
		self.unit_y, self.unit_x = 1,1

	def calculate(self):
		if (self.x_end - self.x_start)> (self.y_end - self.y_start):
			self.times = self.x_end - self.x_start
			self.unit_y = float((self.y_end - self.y_start)) / float(self.times)
 
		else:
			self.times = self.y_end - self.y_start
			self.unit_x = float((self.x_end - self.x_start)) / float(self.times)


	def get_rrCC(self):
		self.rr = [self.x_start]
		self.cc = [self.y_start]
		current_x = self.x_start
		current_y = self.y_start

		for loop in range(self.times):
			current_x += self.unit_x
			current_y += self.unit_y
	
			self.rr.append(int(current_x))
			self.cc.append(int(current_y))

	def draw(self):
		self.calculate()
		self.get_rrCC()

		self.interface[self.cc,self.rr] = 1
		#print self.interface
		return self.rr, self.cc, self.interface

def test():
	img = np.zeros((110,110), dtype = np.uint8)
	my_line = Line(img, 1,1,1,100)
	rr,cc,img = my_line.draw()
	imshow(img)
	show()
	print img

if __name__ == "__main__":
	test()

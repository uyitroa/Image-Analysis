import numpy
import mahotas

def openFile():
	name = input("file name: ")
	image = mahotas.imread(name)
	return image

class Detect:
	def __init__(self, matrix):
			self.matrix = matrix
	
	def edge(self):
		nRow = len(self.matrix)
		nCol = len(self.matrix[0])
		new = numpy.zeros((nRow, nCol))
		
		lastColor = self.matrix[0][0]
		for row in range(nRow):
			for column in range(nCol):
				currentColor = self.matrix[row][column]
				
				if not (lastColor - 10 < currentColor and lastColor + 10 > currentColor):
					#idk yet

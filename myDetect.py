import numpy
import mahotas
from pylab import imshow, show

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
		
		currentColor = self.matrix[0][0]
		for row in range(nRow):
			for column in range(nCol):
				if row + 1 < nRow:
					nextColor = self.matrix[row + 1][column]
					if not (currentColor + 10 > nextColor and currentColor - 10 < nextColor):
						new[row][column] = 1
				if column + 1 < nCol:
					nextColor = self.matrix[row][column + 1]
					if not (currentColor + 10 > nextColor and currentColor - 10 < nextColor):
						new[row][column] = 1
		return new
def test():
	myMatrix = openFile()
	detect = Detect(myMatrix)
	myMatrix = detect.edge()
	imshow(myMatrix)
	show()
	
if __name__ == "__main__":
	test()

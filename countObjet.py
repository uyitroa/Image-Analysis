import numpy
import pylab
import mahotas

image = raw_input("image name: ")
img = mahotas.imread(image)

pylab.gray()
T = mahotas.thresholding.otsu(img)

try:
	imgf = mahotas.gaussian_filter(img,8)
except:
	imgf = img
labeled, nbr = mahotas.label(imgf > T)
print nbr
pylab.imshow(labeled)
pylab.jet()
pylab.show()

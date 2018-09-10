#!/usr/bin/python3

from PyQt4 import QtGui
import pyqtgraph as pg
import numpy as np
from time import sleep
import sys

x = [0]
y = [0]
z = [0]
w = [0]
t = [0]
count = 0
iter = 500


app = QtGui.QApplication([])

win = pg.GraphicsWindow()

p1 = win.addPlot( row=0, col=0)
p2 = win.addPlot( row=1, col=0)

curve1 = p1.plot( pen='r')
curve1a = p1.plot(pen='g')
curve2 = p2.plot( pen='b')

#plt = pg.plot( title='Title for Plot Window!' )
#plt.setXRange(0, iter)
p1.showGrid(y=True)
p2.showGrid(y=True)

#plt.move(90,90)
#plt.setGeometry(100,100,400,400)

#curve = plt.plot(x, y, pen='r')
#curve2 = plt.plot(x,y, pen='b')
p1.addLine(y=0, pen=pg.mkPen('y', width=0.5) )
p2.addLine(y=1, pen=pg.mkPen('g', width=0.5) )

while( count <= iter):
	count += 1	
	# pretty print
	if count != 0 and count%10==0:
		if count!=0 and count %100==10:
			print("\n", end='')
		print(count, end=' ')
		sys.stdout.flush()
	x.append(count)
	y.append( y[count-1] + np.random.normal(0,1) )
	z.append( z[count-1] - np.random.normal(0,1)*5 )
	w.append( w[count-1] - np.random.normal( 0, 1)*3 )
	curve1.setData( x, y)
	curve1a.setData( x, w)
	curve2.setData(x,z)
	app.processEvents()
	sleep(0.05)

print("\n")
print("exiting now")
sleep(3)
pg.exit()

# Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
	import sys
	if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
		QtGui.QApplication.instance().exec_()





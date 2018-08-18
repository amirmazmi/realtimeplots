from PyQt4 import QtGui
import pyqtgraph as pg
import numpy as np
from time import sleep
import sys

x = [0]
y = [0]
z = [0]
count = 0
iter = 100

plt = pg.plot( title='Title for Plot Window!' )
#plt.setXRange(0, iter)
plt.showGrid(y=True)
curve = plt.plot(x, y, pen='r')
curve2 = plt.plot(x,y, pen='b')
plt.addLine(y=0, pen=pg.mkPen('y', width=0.2) )

while( count <= iter):
	count += 1	
	if count != 0 and count%10==0:
		print(count, end=' ')
		sys.stdout.flush()
	x.append(count)
	y.append( y[count-1] + np.random.normal(0,1) )
	z.append( z[count-1] - np.random.normal(0,1)*5 )
	curve.setData( x, y)
	curve2.setData(x,z)
	QtGui.QApplication.processEvents()  # need this to process events
	sleep(0.1)

print("\n")

# Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()


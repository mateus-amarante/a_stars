from point2d import *
from nav_msgs.msg import GridCells

class Frontier(object):
	def __init__(self, allPoints = []):
		self.points = []
		self.size = 0
		self.addAllPoints(allPoints)
	
	def addPoint(self, point):
		self.points.append(point)
		self.size+=1
	
	def addPoints(self, points):
		for point in points:
			self.addPoint(point)
	
	def addAllPoints(self, points):
		self.clear()
		self.addPoints(points)
	
	def clear(self):
		del self.points[:]
		self.size = 0
	
	#Return the smallest possible list of Frontiers where each frontier has connected points
	def split(self):
		pass
	
	def centroid(self):
		
		sumx = 0
		sumy = 0
		
		for point in self.points:
			sumx += point.x
			sumy += point.y

		return Point2D(sumx/self.size, sumy/self.size) # it can throw divisionByZero exception
		
	def toGridCell(self, resolution, origin):
		grid = GridCells()
		grid.header.frame_id = "map"
		grid.cell_width = resolution
		grid.cell_height = resolution
		
		for point in self.points:
			grid.cells.append(point.toRosPoint(resolution,origin))
		
		return grid

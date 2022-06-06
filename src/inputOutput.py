# Imports
import csv
import xml.etree.ElementTree as ET
import coordConvert as cc
import os

# Set root Dir
rootDir = os.path.dirname(__file__)
# Set InOutDir
InOutDir = os.path.join(rootDir, 'InOut')

# Load from default file
def loadDefaultFile():
	try:
		coordsRaw = open(os.path.join(InOutDir, 'coordsIn.csv'), 'r')
	except:
		print('No default file found')
		exit()
	coordsDict = csv.DictReader(coordsRaw, fieldnames=('lat', 'lon'))
	# Convert to arrays
	latArray = []
	lonArray = []

	for coordRow in coordsDict:
		latArray.append(coordRow['lat'])
		lonArray.append(coordRow['lon'])
	coordsRaw.close()

	return [latArray, lonArray]


def exportCSV(coords):
	# Convert to CSV
	coordsOut = open(os.path.join(InOutDir, 'coordsOut.csv'), 'w')
	coordsOut.write('lat,lon\n')
	coordNUM = 0
	degreeSign = u"\N{DEGREE SIGN}"
	while coordNUM < len(coords[0]):
		lat = coords[0][coordNUM][0] + degreeSign + ' ' + coords[0][coordNUM][1]# + '\' ' + coords[0][coordNUM][2]
		lon = coords[1][coordNUM][0] + degreeSign + ' ' + coords[1][coordNUM][1]# + '\' ' + coords[1][coordNUM][2]
		coordsOut.write(lat + ',' + lon + '\n')
		coordNUM += 1
	coordsOut.close()

# Convert to GPX
def exportGPX(coords, coordType):
	# Convert Coords to D
	if coordType == 'DM':
		coords[0] = cc.DM_D(coords[0])
		coords[1] = cc.DM_D(coords[1])

	# Create root element
	gpxRoot = ET.Element('gpx')
	gpxRoot.set('version', '1.1')
	gpxRoot.set('creator', 'Brendan Johnston')
	gpxRoot.set('xmlns', 'http://www.topografix.com/GPX/1/1')

	# Create Route
	route = ET.Element('rte')
	gpxRoot.append(route)

	# Add route points
	waypointID = 0
	while waypointID < len(coords[0]):
		waypoint = ET.SubElement(route, 'rtept')
		waypoint.set('lat', coords[0][waypointID][0])
		waypoint.set('lon', coords[1][waypointID][0])
		waypointID += 1

	# Create GPX file
	gpxTree = ET.ElementTree(gpxRoot)
	print(gpxTree)
	with open (os.path.join(InOutDir, 'GPXOut.gpx'), "wb") as file :
		gpxTree.write(file)
from imports import *

# Open Coordinate file
coordsRaw = open('coordsIn.csv', 'r')
coordsDict = csv.DictReader(coordsRaw, fieldnames=('lat', 'lon'))

# Convert to arrays
latArray = []
lonArray = []

for coordRow in coordsDict:
	latArray.append(coordRow['lat'])
	lonArray.append(coordRow['lon'])
coordsRaw.close()

# Convert to required format
latArray = cc.DMS_D(latArray)
lonArray = cc.DMS_DM(lonArray)

# Print Results
coordNum = 0
while coordNum < len(lonArray):

	# compress Arrays
	lat = ' '.join(str(elem) for elem in latArray[coordNum])
	lon = ' '.join(str(elem) for elem in lonArray[coordNum])

	# Print Results
	print(lat + " | " + lon)

	coordNum += 1
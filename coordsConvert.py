# Imports
import csv

# Open Coordinate file
coordsRaw = open('coordsIn.csv', 'r')
coordsDict = csv.DictReader(coordsRaw, fieldnames=('lat', 'lon'))

# Convert to arrays
latArray = []
lonArray = []

for coordRow in coordsDict:
	latArray.append(coordRow['lat'])
	lonArray.append(coordRow['lon'])

# Convert Coordinates to required formats
def convertArray(coordArray):
	# Iteration ID
	ID = 0

	while ID < len(coordArray):
		# Get Coord
		coordRaw = coordArray[ID]

		# Remove unwanted Charecters
		coordRaw = coordRaw.encode('ascii', 'ignore')
		coordRaw = coordRaw.decode()
		coordRaw = coordRaw.replace('\"', '')
		coordRaw = coordRaw.replace('\'', '')

		# Calculate required changes
		coordComp = coordRaw.split(' ')
		coordComp[2] = float(coordComp[2])/60
		coordComp = [[float(coordComp[0]),0], (float(coordComp[1])+coordComp[2]), coordComp[3]]
		coordComp[0][1] = coordComp[1]/60
		coordComp[0][1] = coordComp[0][0]+coordComp[0][1]

		# Check if negative
		coordComp[2] = coordComp[2].upper()
		if coordComp[2] == 'S' or coordComp == 'W':
			coordComp = [[(coordComp[0][0]), (coordComp[0][1]*-1)], coordComp[1], coordComp[2]]

		# Return to Strings
		coordComp[0][0] = str(coordComp[0][0])
		coordComp[0][1] = str(coordComp[0][1])
		coordComp[1] = str(coordComp[1])

		# Re add to Array
		coordArray[ID] = coordComp

		# Iterate
		ID += 1

	return coordArray


latArray = convertArray(latArray)
lonArray = convertArray(lonArray)

# Print Results
coordNum = 0
while coordNum < len(lonArray):

	# compress Arrays
	lat = ' '.join(str(elem) for elem in latArray[coordNum])
	lon = ' '.join(str(elem) for elem in lonArray[coordNum])

	# Print Results
	print(lat + " | " + lon)

	coordNum += 1
def cleanCoord(coord):

	# Get Coord
	coordRaw = coord

	# Remove unwanted Charecters
	coordRaw = coordRaw.encode('ascii', 'ignore')
	coordRaw = coordRaw.decode()
	coordRaw = coordRaw.replace('\"', '')
	coordRaw = coordRaw.replace('\'', '')

	coord = coordRaw

	return coord

# Convert Derees, Minutes Seconds to Degrees Decimal Minutes
def DMS_DM(coordArray):
	# Iteration ID
	ID = 0

	while ID < len(coordArray):
		# Get Coord
		coordRaw = coordArray[ID]

		coordRaw = cleanCoord(coordRaw)

		# Calculate required changes
		coordComp = coordRaw.split(' ')
		coordComp[2] = float(coordComp[2])/60
		coordComp = [float(coordComp[0]), (float(coordComp[1])+coordComp[2]), coordComp[3]]

		# Return to Strings
		coordComp[0] = str(coordComp[0])
		coordComp[1] = str(coordComp[1])

		# Re add to Array
		coordArray[ID] = coordComp

		# Iterate
		ID += 1

	return coordArray

# Convert Derees, Minutes Seconds to Decimal Degrees
def DMS_D(coordArray):
	# Iteration ID
	ID = 0

	while ID < len(coordArray):
		# Get Coord
		coordRaw = coordArray[ID]
		coordRaw = cleanCoord(coordRaw)


		# Calculate required changes
		coordComp = coordRaw.split(' ')
		coordComp[2] = float(coordComp[2])/60
		coordComp = [float(coordComp[0]), (float(coordComp[1])+coordComp[2]), coordComp[3]]
		coordComp[1] = coordComp[1]/60
		coordComp = [(float(coordComp[0])+coordComp[1]), coordComp[2]]

		# Check if negative
		coordComp[1] = coordComp[1].upper()
		if coordComp[1] == 'S' or coordComp == 'W':
			coordComp = [(coordComp[0]*-1), coordComp[1]]

		# Return to Strings
		coordComp[0] = str(coordComp[0])


		# Re add to Array
		coordArray[ID] = coordComp

		# Iterate
		ID += 1

	return coordArray

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


# Export Converters
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

# Convert Degrees Decimal Minutes to Degrees Decimal Minutes
def DM_DM(coordArray):
	# Iteration ID
	ID = 0

	while ID < len(coordArray):
		# Get Coord
		coordRaw = coordArray[ID]
		coordRaw = cleanCoord(coordRaw)

		# Calculate required changes
		coordComp = coordRaw.split(' ')
		coordComp = [float(coordComp[0]), (float(coordComp[1])), coordComp[2]]

		# Return to Strings
		coordComp[0] = str(coordComp[0])
		coordComp[1] = str(coordComp[1])

		# Re add to Array
		coordArray[ID] = coordComp

		# Iterate
		ID += 1

	return coordArray

# Convert Decimal Degrees to Derees, Decimal Minutes
def D_DM(coordArray):
	# Iteration ID
	ID = 0

	while ID < len(coordArray):
		# Get Coord
		coordRaw = coordArray[ID]
		coordRaw = cleanCoord(coordRaw)

		# Calculate required changes
		coordComp = coordRaw.split(' ')
		coordComp[0] = float(coordComp[0])
		coordComp[0] = abs(coordComp[0])
		coordComp[0] = divmod(coordComp[0], 1)
		coordComp = [float(coordComp[0][0]), float(coordComp[0][1]), coordComp[1]]
		coordComp[1] = coordComp[1]*60
		

		# Check if negative
		coordComp[0] = abs(coordComp[0])

		# Return to Strings
		coordComp[0] = str(coordComp[0])
		coordComp[1] = str(coordComp[1])


		# Re add to Array
		coordArray[ID] = coordComp

		# Iterate
		ID += 1

	return coordArray



# Other Converters
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

# Convert Derees, Decimal minutes to Decimal Degrees
def DM_D(coordArray):
	# Iteration ID
	ID = 0

	while ID < len(coordArray):
		# Get Coord
		coordRaw = coordArray[ID]


		# Calculate required changes
		coordComp = [float(coordRaw[0]), float(coordRaw[1]), coordRaw[2]]
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
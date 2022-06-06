# Imports
from imports import *
from tkinter import *
from tkinter import ttk

# Root Frame
def root():
	global rootFrame
	rootFrame = Tk()
	rootFrame.title('GPS Data Convertor')

	# Centering the window
	rootFrame.grid_rowconfigure(4, weight=1) # Bottom
	rootFrame.grid_columnconfigure(0, weight=1) #Left
	rootFrame.grid_columnconfigure(3, weight=1) # Right

	Label(rootFrame, text='GPS Data Convertor', font=(16)).grid(row=0, column=1, columnspan=2)
	Label(rootFrame, text='Please Select Operation:').grid(row=1, column=1, columnspan=2)
	Button(rootFrame, text='Create Route', command=generateRouteSettings).grid(row=2, column=1)
	Button(rootFrame, text='Convert Coordinates', command=convertCoords).grid(row=2, column=2)

	rootFrame.mainloop()

def generateRouteSettings():
	rootFrame.destroy()
	global routeGeneratorFrame
	routeGeneratorFrame = Tk()
	routeGeneratorFrame.title('Create Route')

	# Centering the window
	routeGeneratorFrame.grid_rowconfigure(5, weight=1) # Bottom
	routeGeneratorFrame.grid_columnconfigure(0, weight=1) #Left
	routeGeneratorFrame.grid_columnconfigure(4, weight=1) # Right

	# Wigets
	Label(routeGeneratorFrame, text='GPS Data Convertor', font=(16)).grid(row=0, column=1, columnspan=2)

	Label(routeGeneratorFrame, text='Enter Coordinates into coordsIn.csv,').grid(row=1, column=1, columnspan=2)
	Label(routeGeneratorFrame, text='Then enter settings and click continue.').grid(row=2, column=1, columnspan=2)

	# Input format dropdown
	# Heading
	Label(routeGeneratorFrame, text='Input Format:').grid(row=3, column=1,)
	# Possible Values
	inputOptionList = ['DMS', 'DM', 'D']
	inputOption = StringVar(routeGeneratorFrame, 'DMS')
	# Dropdown
	OptionMenu(routeGeneratorFrame, inputOption, *inputOptionList).grid(row=3, column=2,)


	Label(routeGeneratorFrame, text='Output Format:').grid(row=4, column=1,)
	outputOptionList = ['gpx', 'gpx & csv']
	outputOptions = StringVar(routeGeneratorFrame)
	outputOptions.set(outputOptionList[1])
	OptionMenu(routeGeneratorFrame, outputOptions, *outputOptionList).grid(row=4, column=2,)

	Button(routeGeneratorFrame, text='Continue', command=lambda: generateRoute(inputOption.get(), outputOptions.get())).grid(row=5, column=1, columnspan=2)

	routeGeneratorFrame.mainloop()

def generateRoute(inputFormat, exportFormats):
	# Frame Setup
	routeGeneratorFrame.destroy()
	global generatingRouteFrame
	generatingRouteFrame = Tk()
	generatingRouteFrame.title('GPS Data Convertor')

	# Centering the window
	generatingRouteFrame.grid_rowconfigure(0, weight=1) # Top
	generatingRouteFrame.grid_rowconfigure(4, weight=3) # Bottom
	generatingRouteFrame.grid_columnconfigure(0, weight=1) #Left
	generatingRouteFrame.grid_columnconfigure(2, weight=1) # Right

	# Wigets
	Label(generatingRouteFrame, text='Processing').grid(row=1, column=1)
	progress = ttk.Progressbar(generatingRouteFrame, orient=HORIZONTAL, length=300, mode='indeterminate')
	progress.grid(row=2, column=1)
	progress.start(30)
	operation = Label(generatingRouteFrame, text='Converting Coordinates...')
	operation.grid(row=3, column=1)

	# Get coords
	coords = io.loadDefaultFile()

	# Convert coords
	# Create Conversion Threads based on inputFormat
	if inputFormat == 'DMS':
		latThread = threading.Thread(target=cc.DMS_DM, args=(coords[0],), daemon=True)
		lonThread = threading.Thread(target=cc.DMS_DM, args=(coords[1],), daemon=True)
	elif inputFormat == 'DM':
		latThread = threading.Thread(target=cc.DM_DM, args=(coords[0],), daemon=True)
		lonThread = threading.Thread(target=cc.DM_DM, args=(coords[1],), daemon=True)
	elif inputFormat == 'D':
		latThread = threading.Thread(target=cc.D_DM, args=(coords[0],), daemon=True)
		lonThread = threading.Thread(target=cc.D_DM, args=(coords[1],), daemon=True)
	# Activate Conversion Threads
	latThread.start()
	lonThread.start()
	# Wait for threads to finish
	while latThread.is_alive() == True or lonThread.is_alive() == True:
		generatingRouteFrame.update()


	# Export coords
	operation.config(text='Exporting Coordinates...')
	# Set correct thread based on required format
	if exportFormats == 'gpx':
		# Create threads
		exportGPX = threading.Thread(target=io.exportGPX, args=(coords, 'DM',), daemon=True)
		# Activate threads
		exportGPX.start()
		# Wait for threads to finish
		while exportGPX.is_alive() == True:
			generatingRouteFrame.update()
		
	elif exportFormats == 'gpx & csv':
		# Create threads
		exportGPX = threading.Thread(target=io.exportGPX, args=(coords, 'DM',), daemon=True)
		exportCSV = threading.Thread(target=io.exportCSV, args=(coords,), daemon=True)
		# Activate threads
		exportGPX.start()
		exportCSV.start()
		# Wait for threads to finish
		while exportGPX.is_alive() == True or exportCSV.is_alive() == True:
			generatingRouteFrame.update()
	exit()



def convertCoords():
	rootFrame.destroy()
	global convertCoordsFrame
	convertCoordsFrame = Tk()
	convertCoordsFrame.title('Convert Coordinates')
	Label(convertCoordsFrame, text='GPS Data Convertor', font=(16)).grid(row=0, column=0, columnspan=2)


# Start First Function
root()
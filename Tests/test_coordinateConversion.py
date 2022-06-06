import os
import sys
sys.path.append(os.path.abspath('./'))
from imports import *


# Setup Test Data

# Input Data
inputArrayDMS = ['ï»¿"11Â° 46\' 8.62610"" S"', '11Â° 46\' 19.54373" S', '11Â° 46\' 14.81938" S']
inputArrayDM = ['ï»¿"11Â° 46.143768333333334\' S', '11Â° 46.325728833333336\' S', '11Â° 46.246989666666664\' S']
inputArrayD = ['ï»¿"-11.769062805555556Â°\' S', '-11.772095480555556Â°\' S', '-11.770783161111112Â°\' S']


# Expected Output Data
outputArrayDM = [['11.0', '46.143768333333334', 'S'], ['11.0', '46.325728833333336', 'S'], ['11.0', '46.246989666666664', 'S']]
outputArrayD = [['-11.769062805555556', 'S'], ['-11.772095480555556', 'S'], ['-11.770783161111112', 'S']]



# Export Converters
def test_DMS_DM():
	print(cc.DMS_DM(inputArrayDMS))
	assert cc.DMS_DM(inputArrayDMS) == outputArrayDM

def test_DM_DM():
	print(cc.DM_DM(inputArrayDM))
	assert cc.DM_DM(inputArrayDM) == outputArrayDM

def test_D_DM():
	print(cc.D_DM(inputArrayD))
	assert cc.D_DM(inputArrayD) == outputArrayDM

# Other Converters
def test_DMS_D():
	print(cc.DMS_D(inputArrayDMS))
	assert cc.DMS_D(inputArrayDMS) == outputArrayD

print(cc.D_DM(inputArrayD))
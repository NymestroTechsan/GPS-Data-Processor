import os
import sys
sys.path.append(os.path.abspath('./'))
from imports import *


# Setup Test Data

# Input Data
inputArray = ['ï»¿"11Â° 46\' 8.62610"" S"', '11Â° 46\' 19.54373" S', '11Â° 46\' 14.81938" S']


# Expected Output Data
outputArrayDM = [['11.0', '46.143768333333334', 'S'], ['11.0', '46.325728833333336', 'S'], ['11.0', '46.246989666666664', 'S']]

outputArrayD = [['-11.769062805555556', 'S'], ['-11.772095480555556', 'S'], ['-11.770783161111112', 'S']]




def test_DMS_DM():
	assert cc.DMS_DM(inputArray) == outputArrayDM

def test_DMS_D():
	assert cc.DMS_D(inputArray) == outputArrayD
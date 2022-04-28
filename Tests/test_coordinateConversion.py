import os
import sys
sys.path.append(os.path.abspath('./'))
import coordsConvert as cc


# Setup Test Data

# Input Data
inputArray = ['ï»¿"11Â° 46\' 8.62610"" S"', '11Â° 46\' 19.54373" S', '11Â° 46\' 14.81938" S', '11Â° 46\' 6.46131" S', '11Â° 45\' 58.54847" S', '11Â° 45\' 34.23448" S', '11Â° 45\' 25.85492" S', '11Â° 45\' 26.40000" S', '11Â° 45\' 29.56682" S', '11Â° 45\' 27.72718" S', '11Â° 45\' 27.61180" S', '11Â° 44\' 35.95017" S', '11Â° 44\' 35.83331" S', '11Â° 44\' 53.40001" S', '11Â° 45\' 25.02001" S']


# Expected Output Data
outputArrayDM_D = [[['11.0', '-11.769062805555556'], '46.143768333333334', 'S'], [['11.0', '-11.772095480555556'], '46.325728833333336', 'S'], [['11.0', '-11.770783161111112'], '46.246989666666664', 'S'], [['11.0', '-11.768461475'], '46.1076885', 'S'], [['11.0', '-11.766263463888889'], '45.975807833333334', 'S'], [['11.0', '-11.759509577777777'], '45.570574666666666', 'S'], [['11.0', '-11.757181922222221'], '45.43091533333333', 'S'], [['11.0', '-11.757333333333333'], '45.44', 'S'], [['11.0', '-11.758213005555556'], '45.492780333333336', 'S'], [['11.0', '-11.757701994444444'], '45.462119666666666', 'S'], [['11.0', '-11.757669944444444'], '45.46019666666667', 'S'], [['11.0', '-11.743319491666666'], '44.5991695', 'S'], [['11.0', '-11.743287030555555'], '44.597221833333336', 'S'], [['11.0', '-11.748166669444444'], '44.89000016666667', 'S'], [['11.0', '-11.756950002777778'], '45.41700016666667', 'S']]




def test_DMS_DM():
	assert cc.convertArray(inputArray) == outputArrayDM_D
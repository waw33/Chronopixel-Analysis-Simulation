# -*- coding: utf-8 -*-
"""
Created on Thu Oct 04 16:29:40 2018

Test Opal Kelly XEM7001 wire readout

Just run this script while the XEM 7001 board is connected and powered
A counters example bitfile will be flashed to the FPGA
And then we read out the status of the counter repeatedly by 
using the wire functionality of the Opal Kelly API


@author: ctw24
"""

############# Check the python version to lead the correct version of the API
import sys
import numpy as np

sys.version_info

if sys.version_info[0] == 2:
    import OpalKellyAPIPython2_7.ok as ok  #import the Opal Kelly API
elif sys.version_info[0] == 3:
    import OpalKellyAPIPython3_6.ok as ok  #import the Opal Kelly API


datain = np.empty(16, dtype=int)

############# Test the FrontPanel Interface #############
# https://opalkelly.com/examples/test-the-frontpanel-interface/#tab-python

dev = ok.okCFrontPanel()

# Enumerating Devices
# https://opalkelly.com/examples/enumerating-devices/#tab-cpp
deviceCount = dev.GetDeviceCount() #The number of devices attached.

for i in range(deviceCount):
    print( 'Device[{0}] Model: {1}'.format( i, dev.GetDeviceListModel(i)) )
    print( 'Device[{0}] Serial: {1}'.format(i, dev.GetDeviceListSerial(i)) )


# Open the first device available
# https://opalkelly.com/examples/open-the-first-device-available/#tab-python

dev.OpenBySerial("")

open=dev.IsOpen() # Returns true if a device is currently open

# Configure the FPGA
# https://opalkelly.com/examples/configure-the-fpga/#tab-python

# load the bit-file onto the FPGA
error = dev.ConfigureFPGA("Pipeout.bit") # It's a good idea to check for errors here!!
dev.SetWireInValue(0x10, 0xff, 0x01);
dev.UpdateWireIns();
dev.SetWireInValue(0x10, 0x00, 0x01);
dev.UpdateWireIns();
data=dev.ReadFromPipeOut(0xA0, datain);
print(datain)
        
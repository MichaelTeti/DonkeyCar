#Define a vehicle to take and record pictures 10 times per second.

from donkeycar import Vehicle
import os, sys
from parts.camera import PiCamera
from parts.datastore import Tub


V = Vehicle()

#add a camera part
cam = PiCamera()
V.add(cam, outputs=['image'], threaded=True)

#add tub part to record images
tub = Tub(path='~/d2/gettings_started', 
          inputs=['image'], 
          types=['image_array'])
V.add(tub, inputs=['image'])

#start the drive loop at 10 Hz
V.start(rate_hz=10)

#!/usr/bin/env python
# Scratch to Python, recieve broadcast message
# 2016-08-01 K.OHWADA

# https://code.google.com/archive/p/py-scratch/
import scratch

### main   
print("connecting...")
s = scratch.Scratch() 
print("connected")

try:
	# endless loop
	while True:
		# receive from scratch
		# {'broadcast': ['cat'], 'sensor-update': {}}
		obj = s.receive()
		print obj["broadcast"][0]
except KeyboardInterrupt:
	# exit the loop, if key Interrupt
	pass

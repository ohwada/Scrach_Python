#!/usr/bin/env python
# Python to Scratch, send broadcast message
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
		# wait to enter command
		msg = raw_input('> ')
		# send to scratch
		s.broadcast(msg)
except KeyboardInterrupt:
	# exit the loop, if key Interrupt
	pass

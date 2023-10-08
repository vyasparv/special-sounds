import datetime
from miditiime.miditime import MIDITime
import pandas as pd 
import numpy as np 

# Initiate MIDITime class 
# 1. a tempo "100 bpm" (120 is default)
# 2. an output file destination 
# 3. octave (5 is default at C5)
# 4. number of octaves the file is allowed to range over (default = 1)

mymidi = MIDITime(100, 'data_sonified.mid',7, 3, 4)

# [0, 60, 127, 3]
# [time, pitch, velocity, duration]
# starts at 0 bits, pitch is at middle C, velocity is 127 

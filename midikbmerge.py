#!/usr/bin/python3
import mido
from mido.ports import MultiPort

### Inputs
lpd8 = mido.open_input('LPD8:LPD8 MIDI 1')
lpk25 = mido.open_input('LPK25:LPK25 MIDI 1')

### Output
rtpmidi = mido.open_output('rtpmidi:rtpmidi')

m = MultiPort([lpd8,lpk25])

for msg in m:
    print(msg)
    rtpmidi.send(msg)


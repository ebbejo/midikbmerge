# Simple MIDI merge for one or more devices

Takes input from one or more MIDI input devices, and sends it to one output device. Useful when needing to combine multiple MIDI input controllers onto one output stream.

Requires (Ubuntu 18.04): 

```
sudo apt-get install python3-mido python3-rtmidi
```

Edit the `midikbmerge.py` file, set your inputs and outputs, and run

```
./midikbmerge.py

```


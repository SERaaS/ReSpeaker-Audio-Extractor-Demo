# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# By: Wei Kit Wong
# 
# This demo program continuously extracts audio via a USB device and
# creates .wav files for any detected speech (5s chunks).
# 
# Codebase Inspiration:
# http://wiki.seeedstudio.com/ReSpeaker_Mic_Array_v2.0/
# 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import pyaudio
import sys

""" Retrieving the USB audio device ID to perform the audio extraction """

p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
deviceCount = info.get('deviceCount')

inputDeviceId = -1
print("Retrieving USB Audio Input Device ID..")

for id in range(0, deviceCount):
  if (p.get_device_info_by_host_api_device_index(0, id).get('maxInputChannels')) > 0:
    inputDeviceId = id

    print("Input Device ID %d - %s" % (
      inputDeviceId,
      p.get_device_info_by_host_api_device_index(0, id).get('name')
    ))

if inputDeviceId == -1:
  print("No Input Device ID found..")
  sys.exit()
else:
  print("Using Input Device ID $d" % inputDeviceId)
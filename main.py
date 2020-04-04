# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# By: Wei Kit Wong
# 
# This demo program continuously extracts audio via a USB device and
# creates .wav files for any detected speech (5s chunks). This is
# sent to the SERaaS API to output the emotions shown in the file.
# 
# Codebase Inspiration:
# http://wiki.seeedstudio.com/ReSpeaker_Mic_Array_v2.0/
# 
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import pyaudio
import sys
import wave
import requests
import seraasURLHandler

""" Retrieving the USB audio device ID to perform the audio extraction """

p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
deviceCount = info.get('deviceCount')

inputDeviceId = -1
print("Retrieving USB Audio Input Device ID..")

# Find the current USB audio device to use
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

""" Extracting audio operation using the USB audio device found """

# Constants
RESPEAKER_RATE = 16000
RESPEAKER_CHANNELS = 6 # change base on firmwares, 1_channel_firmware.bin as 1 or 6_channels_firmware.bin as 6
RESPEAKER_WIDTH = 2
CHUNK = 1024
RECORD_FOR = 5 # in seconds
WAVE_OUTPUT_FILENAME = "output/output.wav"

audioLength = int(RESPEAKER_RATE / CHUNK * RECORD_FOR)
audioFrames = []

# Stream for listening to audio
stream = p.open(
  rate = RESPEAKER_RATE,
  format = p.get_format_from_width(RESPEAKER_WIDTH),
  channels = RESPEAKER_CHANNELS,
  input = True,
  input_device_index = inputDeviceId)

print("Listening to audio..")

# Listen to audio
for i in range(0, audioLength):
  audioStream = stream.read(CHUNK)
  audioFrames.append(audioStream)

print("fin. Extracting audio..")

# fin. with extraction; close all streams
stream.stop_stream()
stream.close()
p.terminate()

print("Outputting audio to file..")

# Output to file appropriately
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(RESPEAKER_CHANNELS)
wf.setsampwidth(p.get_sample_size(p.get_format_from_width(RESPEAKER_WIDTH)))
wf.setframerate(RESPEAKER_RATE)
wf.writeframes(b''.join(audioFrames))
wf.close()

print("fin. Outputting audio to file.")

""" Making API request to SERaaS using created audio file """

# Code generated using Postman, such a good tool !

apiEndpointURL = seraasURLHandler.endpoint

if apiEndpointURL is not None:
  print("Making API request to SERaaS at '%s'.." % apiEndpointURL)

  response = requests.request(
    "POST",
    apiEndpointURL,
    headers = { "Content-Type": "application/x-www-form-urlencoded" },
    data = {},
    files = [ ("file", open(WAVE_OUTPUT_FILENAME, "rb")) ]
  )

  print("Got response from SERaaS:")
  print(response.text.encode('utf8'))
  print("fin. API request operation.")
else:
  print("A seraasURLHandler.py file is required for making the API request. Please read README.md for more information.")
#!/usr/bin/env python

import pyaudio
import socket
import sys


form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 2 # 1 channel
samp_rate = 16000 # 44.1kHz sampling rate
chunk = 1024 # 2^12 samples for buffer
##record_secs = 3 # seconds to record
##dev_index = 0 # device index found by p.get_device_info_by_index(ii)
##wav_output_filename = 'test1.wav' # name of .wav file


HOST = '192.168.1.9'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

audio = pyaudio.PyAudio()

stream = audio.open(format = form_1, \
                    rate = samp_rate, \
                    channels = chans, \
                    output = True, \
                    frames_per_buffer=chunk)


try:
    while True:
        data = s.recv(chunk)
        stream.write(data)
except KeyboardInterrupt:
    print("keyboard interupt")

print('Shutting down')
s.close()
stream.close()
audio.terminate()

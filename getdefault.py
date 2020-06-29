import pyaudio
pa = pyaudio.PyAudio()
p = pa.get_default_input_device_info()
print(p)

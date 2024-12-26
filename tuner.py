import sounddevice as sd
import numpy as np

duration = 5  # seconds
fs = 44100  # sample rate

myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()  # Wait until recording is finished
sd.play(myrecording, fs)
sd.wait()  # Wait until playback is finished
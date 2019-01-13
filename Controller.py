import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import os
import pickle
placesList=[]
with open('listfile.data', 'rb') as filehandle:
    # read the data as binary data stream
    placesList = pickle.load(filehandle)
print(placesList)
freq_low=[1350, 1550, 1650, 1850, 1950, 2150, 2550, 2700]
freq_high=[1450, 1650, 1750, 1950, 2050, 2250, 2650, 2800]

np.set_printoptions(suppress=True) # don't use scientific notation

CHUNK = 4096 # number of data points to read at a time
RATE = 44100 # time resolution of the recording device (Hz)

p=pyaudio.PyAudio() # start the PyAudio class
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK) #uses default input device

# create a numpy array holding a single read of audio data
while True: #to it a few times just to see
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    data = data * np.hanning(len(data)) # smooth the FFT by windowing data
    fft = abs(np.fft.fft(data).real)
    fft = fft[:int(len(fft)/2)] # keep only first half
    freq = np.fft.fftfreq(CHUNK,1.0/RATE)
    freq = freq[:int(len(freq)/2)] # keep only first half
    freqPeak = freq[np.where(fft==np.max(fft))[0][0]]+1
    #print("peak frequency: %d Hz"%freqPeak)
    for i in range(8):
            if freqPeak<=freq_high[i] and freqPeak>=freq_low[i]:
                os.system("xdotool key "+placesList[i] +" >/dev/null 2>&1")
                print(placesList[i])

    # uncomment this if you want to see what the freq vs FFT looks like
    #plt.plot(freq,fft)
    #plt.axis([0,4000,None,None])
    #plt.show()
    #plt.close()

# close the stream gracefully
stream.stop_stream()
stream.close()
p.terminate()

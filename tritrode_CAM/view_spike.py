from numpy import *
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import filtfilt, butter
from scipy.signal import resample
from scipy import signal

# Create an order 3 bandpass butterworth filter.
def butter_bandpass(lowcut, highcut, fs, order=3):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

df = pd.read_csv('./Signal_50Hz_Spike1.csv', header=None)
raw_data = df.values[1:,:]
raw_data = asarray(raw_data,dtype=float)
dt = 2.5e-5; fs = 1/dt
T = len(raw_data)*dt
t = linspace(0,T,len(raw_data))
sig_ch1 = raw_data[:,0]
sig_ch2 = raw_data[:,1]
f, Pxx_den = signal.welch(raw_data.T, fs, nperseg=256*30, noverlap=128)

# semilogy(f[0:100],Pxx_den[0:100])

b, a = butter_bandpass(300,2000,fs)
y = filtfilt(b, a, raw_data.T, padlen=150, padtype="even")

y = y*1e6
colours = ["#348ABD", "r"]
plt.plot(t,y[0,:],color=colours[0], label='ch1')
plt.plot(t,y[1,:],color=colours[1], label='ch2')
plt.legend(loc='best')
plt.show()

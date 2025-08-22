import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt

DURATION = 5       # seconds
FS = 44100         # sample rate
FILENAME = "melodi_take1.wav"

print("Recording for", DURATION, "seconds... Start singing!")
audio = sd.rec(int(DURATION * FS), samplerate=FS, channels=1, dtype='float32')
sd.wait()
print("Recording done. Saving to", FILENAME)

# Save WAV
write(FILENAME, FS, audio)

# Quick stats
print("Shape:", audio.shape, " Sample rate:", FS)
print("File saved:", FILENAME)

# Plot waveform
plt.figure(figsize=(10,3))
plt.plot(audio, linewidth=0.8)
plt.title("Your Voice Waveform")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.show()

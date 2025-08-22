import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

FILENAME = "melodi_take1.wav"   # your saved recording

# Load the audio
y, sr = librosa.load(FILENAME)

# ---- Spectrogram ----
plt.figure(figsize=(10, 4))
D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log', cmap='magma')
plt.colorbar(format='%+2.0f dB')
plt.title("Spectrogram of Your Singing")
plt.tight_layout()
plt.show()

# ---- Pitch Tracking ----
pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

pitch_curve = []
for t in range(pitches.shape[1]):
    index = magnitudes[:, t].argmax()
    pitch = pitches[index, t]
    pitch_curve.append(pitch)

# ---- Pitch Curve with Reference Note ----
plt.figure(figsize=(10, 3))
plt.plot(pitch_curve, color='green', label="Your Pitch")

# Add reference pitch line (Middle C = 261.63 Hz)
reference_pitch = 261.63
plt.axhline(y=reference_pitch, color='red', linestyle='--', label="Reference Note (C4 = 261 Hz)")

plt.title("Pitch Curve vs Reference Note")
plt.xlabel("Time frames")
plt.ylabel("Frequency (Hz)")
plt.legend()
plt.tight_layout()
plt.show()

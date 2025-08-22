import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

# Load your singing
y, sr = librosa.load("melodi_take1.wav")

# Extract pitch curve using librosa's pyin
f0, voiced_flag, voiced_probs = librosa.pyin(
    y,
    fmin=librosa.note_to_hz('C2'),
    fmax=librosa.note_to_hz('C7')
)

# Replace unvoiced frames with NaN
f0 = np.where(np.isnan(f0), 0, f0)

# Reference note (Middle C = C4 = 261 Hz)
reference_note = 261.0

# Calculate average pitch of the singing
avg_pitch = np.mean(f0[f0 > 0])  # consider only non-zero pitches

# Simple feedback
if avg_pitch < reference_note - 20:
    feedback = "Your pitch is lower than the target note."
elif avg_pitch > reference_note + 20:
    feedback = "Your pitch is higher than the target note."
else:
    feedback = "Great! You're close to the target note."

print(f"Average Pitch: {avg_pitch:.2f} Hz")
print("Feedback:", feedback)

# Plot pitch curve vs reference
plt.figure(figsize=(10, 4))
plt.plot(f0, label="Your Pitch", color="green")
plt.axhline(y=reference_note, color="red", linestyle="--", label="Reference Note (C4)")
plt.xlabel("Time Frames")
plt.ylabel("Frequency (Hz)")
plt.title("Pitch Curve vs Reference Note")
plt.legend()
plt.savefig("pitch_curve.png")  # saves the graph as an image
plt.show()

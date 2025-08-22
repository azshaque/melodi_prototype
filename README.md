🎶 MELODI – Karaoke Coach

MELODI is a prototype application that helps singers practice and improve their pitch accuracy.
It records your singing, generates a spectrogram, and compares your pitch curve against a reference note — giving simple feedback through a GUI.

## 🚀 Features

🎤 Record your voice directly from the app

📊 Spectrogram Visualization of your singing

🎼 Pitch Feedback compared to a reference note (default: C4)

🖥️ Clean, lightweight Tkinter GUI

## 🛠️ Tech Stack

Python 3.11+

Libraries:

sounddevice – audio recording

scipy, numpy – signal processing

matplotlib, librosa – visualization & pitch analysis

tkinter – GUI

## 📂 Project Structure

MELODI_project/
│-- .venv/                # Virtual environment (ignored in Git)
│-- melodi.py             # Main GUI
│-- step1_record.py       # Record audio
│-- step2_spectrogram.py  # Generate spectrogram
│-- step3_feedback.py     # Pitch feedback
│-- requirements.txt      # Dependencies
│-- .gitignore            # Ignore venv, wav, png, cache

## 📌 Notes

Default recording length: 5 seconds

Default reference note: C4 (261 Hz)

Audio files (*.wav) and graphs (*.png) are ignored in Git (kept local only).

## 👨‍👩‍👧‍👦 Team MELODI

This project was developed as part of TechAI 2.0 Hackathon by:

[Azshaque Rizvi]

[Naman Kumar]

[Nishka Priya]

[Afzal Amanullah]

## 📅 Future Improvements

Allow custom note selection

Add real-time pitch tracking

Save practice history & progress reports


✨ Built as a prototype for experimenting with voice analysis & singing practice.
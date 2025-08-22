import sys
import tkinter as tk
from tkinter import messagebox
import subprocess

# -------------------------------
# Button Functions
# -------------------------------
def record_audio():
    try:
        result = subprocess.run(
            [sys.executable, "step1_record.py"],
            check=True, capture_output=True, text=True
        )
        messagebox.showinfo("MELODI", "✅ Recording finished and saved as melodi_take1.wav")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Recording script failed!\n\n{e.stderr or e.stdout}")
    except Exception as e:
        messagebox.showerror("Error", f"Unexpected error:\n{e}")

def show_spectrogram():
    try:
        result = subprocess.run(
            [sys.executable, "step2_spectrogram.py"],
            check=True, capture_output=True, text=True
        )
        messagebox.showinfo("MELODI", "✅ Spectrogram generated (spectrogram_output.png)")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Spectrogram script failed!\n\n{e.stderr or e.stdout}")
    except Exception as e:
        messagebox.showerror("Error", f"Unexpected error:\n{e}")

def show_feedback():
    try:
        result = subprocess.run(
            [sys.executable, "step3_feedback.py"],
            check=True, capture_output=True, text=True
        )
        messagebox.showinfo("MELODI", "✅ Pitch feedback generated (pitch_curve.png)")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Feedback script failed!\n\n{e.stderr or e.stdout}")
    except Exception as e:
        messagebox.showerror("Error", f"Unexpected error:\n{e}")

# -------------------------------
# GUI Window
# -------------------------------
def main():
    root = tk.Tk()
    root.title("MELODI - Karaoke Coach")
    root.geometry("400x300")

    # Title
    tk.Label(root, text="🎵 MELODI 🎵", font=("Arial", 20, "bold")).pack(pady=20)

    # Buttons
    tk.Button(root, text="🎤 Record 5s", width=20, command=record_audio).pack(pady=10)
    tk.Button(root, text="📊 Show Spectrogram", width=20, command=show_spectrogram).pack(pady=10)
    tk.Button(root, text="🎼 Pitch Feedback", width=20, command=show_feedback).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()

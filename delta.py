import numpy as np
from scipy.io.wavfile import write
import os

# Parameters
duration = 60*30  # seconds (you can adjust this to any length of time)
sample_rate = 44100  # Hz (standard for audio CDs)
freq_left = 100  # Base frequency for left ear (Hz)
freq_right = freq_left + 3  # Right ear frequency to create a 3 Hz binaural beat (Delta range)

# Time array
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Generate sine waves for left and right channels
wave_left = 0.5 * np.sin(2 * np.pi * freq_left * t)
wave_right = 0.5 * np.sin(2 * np.pi * freq_right * t)

# Combine into stereo (2D array: left channel, right channel)
stereo_wave = np.column_stack((wave_left, wave_right))

# Scale to 16-bit PCM format
stereo_wave_int16 = np.int16(stereo_wave * 32767)

# Get the path to the Downloads folder
downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
output_file = os.path.join(downloads_folder, "delta_wave_3hz_30min.wav")

# Save as WAV file
write(output_file, sample_rate, stereo_wave_int16)

print(f"Audio file saved to {output_file}")

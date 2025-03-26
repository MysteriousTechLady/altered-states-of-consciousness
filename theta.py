import os
import numpy as np
import scipy.io.wavfile as wav



# findpy =os.path.expanduser("~","C:\Users\User\AppData\Local\Microsoft\WindowsApps\python.exe"),
# print(findpy)
# Create a sine wave for binaural beats
def create_binaural_beat(frequency_left, frequency_right, duration=60*30, sample_rate=44100):
    # Time array for the duration of the audio
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    
    # Left and right frequencies
    left_channel = np.sin(2 * np.pi * frequency_left * t)
    right_channel = np.sin(2 * np.pi * frequency_right * t)
    
    # Combine both channels into a stereo signal
    stereo_signal = np.vstack((left_channel, right_channel)).T
    
    return stereo_signal

# Generate binaural beat audio in the theta range (4 Hz - 8 Hz difference)
left_frequency = 400  # Frequency of the left ear
right_frequency = 406  # Frequency of the right ear (6 Hz difference - within theta range)

audio_signal = create_binaural_beat(left_frequency, right_frequency)

# Specify the path to save the file in the Downloads folder
downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
output_file = os.path.join(downloads_folder, "binaural_beat_theta_30min.wav")

# Write the audio to the WAV file
wav.write(output_file, 44100, (audio_signal * 32767).astype(np.int16))

print(f"Audio file saved to {output_file}")

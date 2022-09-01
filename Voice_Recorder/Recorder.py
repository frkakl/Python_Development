import sounddevice
from scipy.io.wavfile import write

def voice_recorder(seconds, file):
    print("Recording Now...")
    recording = sounddevice.rec((seconds * 44100), samplerate= 44100, channels=2)
    sounddevice.wait()
    write(file, 44100, recording)
    print("Your Voice Recorded...")

voice_recorder(3, "record.wav") #recording time and file name
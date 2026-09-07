import sounddevice as sd
import speech_recognition as sr
import scipy.io.wavfile as wav
import os


# -----------------------------
# Microphone Configuration
# -----------------------------

SAMPLE_RATE = 16000
RECORD_SECONDS = 5
MICROPHONE_DEVICE = 1

AUDIO_FILE = "microphone_test.wav"


# -----------------------------
# Record Voice
# -----------------------------

print("=" * 50)
print("       VOICE RECOGNITION TEST")
print("=" * 50)

print("\nSpeak clearly after the recording starts.")
print("Example: Hello, this is Ketan testing my voice assistant.\n")

try:

    print("🎤 Recording...")

    audio = sd.rec(
        int(RECORD_SECONDS * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16",
        device=MICROPHONE_DEVICE
    )

    sd.wait()

    print("✅ Recording completed.")

    wav.write(
        AUDIO_FILE,
        SAMPLE_RATE,
        audio
    )

except Exception as error:

    print(f"\n❌ Microphone error: {error}")
    exit()


# -----------------------------
# Speech Recognition
# -----------------------------

recognizer = sr.Recognizer()

print("\n🔄 Converting your voice to text...")

try:

    with sr.AudioFile(AUDIO_FILE) as source:

        audio_data = recognizer.record(source)

    text = recognizer.recognize_google(audio_data)

    print("\n" + "=" * 50)
    print("RECOGNIZED TEXT")
    print("=" * 50)

    print(f"You said: {text}")

    print("\n✅ Speech recognition is working!")

except sr.UnknownValueError:

    print("\n❌ Could not understand your voice.")
    print("Please speak clearly and try again.")

except sr.RequestError as error:

    print("\n❌ Google Speech Recognition service error.")
    print(f"Error: {error}")

except Exception as error:

    print("\n❌ Unexpected error.")
    print(f"Error: {error}")


# -----------------------------
# Remove Temporary Audio
# -----------------------------

if os.path.exists(AUDIO_FILE):

    os.remove(AUDIO_FILE)

    print("\nTemporary audio file removed.")
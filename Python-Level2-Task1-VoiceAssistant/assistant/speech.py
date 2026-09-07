"""
Speech Module
OASIS INFOBYTE - Python Programming Internship
Task 1: Advanced Voice Assistant
"""

import os
import sounddevice as sd
import speech_recognition as sr
import scipy.io.wavfile as wav
import pyttsx3


class SpeechManager:
    """Handles microphone recording, speech recognition and TTS."""

    def __init__(self):
        self.sample_rate = 16000
        self.microphone_device = 1
        self.recognizer = sr.Recognizer()

        # Text-to-Speech engine
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 170)
        self.engine.setProperty("volume", 1.0)

        self.audio_file = "temp_voice.wav"

    # --------------------------------------------------
    # Text to Speech
    # --------------------------------------------------

    def speak(self, text):
        """Speak the given text."""

        print(f"Assistant: {text}")

        self.engine.say(text)
        self.engine.runAndWait()

    # --------------------------------------------------
    # Record Voice
    # --------------------------------------------------

    def record_voice(self, seconds=5):
        """Record audio from the microphone."""

        print("\n🎤 Listening...")

        try:

            audio = sd.rec(
                int(seconds * self.sample_rate),
                samplerate=self.sample_rate,
                channels=1,
                dtype="int16",
                device=self.microphone_device
            )

            sd.wait()

            wav.write(
                self.audio_file,
                self.sample_rate,
                audio
            )

            print("Recording completed.")

            return True

        except Exception as error:

            print(f"Microphone error: {error}")

            return False

    # --------------------------------------------------
    # Speech To Text
    # --------------------------------------------------

    def recognize_voice(self):
        """Convert recorded audio into text."""

        try:

            with sr.AudioFile(self.audio_file) as source:

                audio_data = self.recognizer.record(source)

            print("🔄 Recognizing...")

            text = self.recognizer.recognize_google(
                audio_data
            )

            text = text.lower().strip()

            print(f"You: {text}")

            return text

        except sr.UnknownValueError:

            self.speak(
                "Sorry, I could not understand you."
            )

            return ""

        except sr.RequestError:

            self.speak(
                "Speech recognition service is unavailable."
            )

            return ""

        except Exception as error:

            print(f"Recognition error: {error}")

            return ""

    # --------------------------------------------------
    # Listen
    # --------------------------------------------------

    def listen(self, seconds=5):
        """
        Record voice and convert it to text.
        """

        success = self.record_voice(seconds)

        if not success:
            return ""

        text = self.recognize_voice()

        self.delete_audio_file()

        return text

    # --------------------------------------------------
    # Delete Temporary Audio
    # --------------------------------------------------

    def delete_audio_file(self):
        """Delete temporary audio file."""

        if os.path.exists(self.audio_file):

            try:
                os.remove(self.audio_file)

            except OSError:
                pass


# ------------------------------------------------------
# Test
# ------------------------------------------------------

if __name__ == "__main__":

    speech = SpeechManager()

    speech.speak(
        "Hello Ketan. Please say something."
    )

    command = speech.listen()

    if command:

        speech.speak(
            f"You said {command}"
        )

    else:

        speech.speak(
            "I did not receive a valid command."
        )
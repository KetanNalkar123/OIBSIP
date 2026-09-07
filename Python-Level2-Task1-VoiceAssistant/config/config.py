"""
Application configuration.
"""

import os

from dotenv import load_dotenv


# Load .env file
load_dotenv()


class Config:

    # ==================================================
    # Application
    # ==================================================

    APP_NAME = (
        "OASIS INFOBYTE Voice Assistant"
    )

    VERSION = "1.0.0"

    # ==================================================
    # User
    # ==================================================

    USER_NAME = os.getenv(
        "ASSISTANT_USER_NAME",
        "Ketan"
    )

    # ==================================================
    # Audio
    # ==================================================

    SAMPLE_RATE = 16000

    # Your working microphone device
    MICROPHONE_DEVICE = 1

    AUDIO_FILE = "temp_voice.wav"

    # ==================================================
    # Speech
    # ==================================================

    SPEECH_RATE = 170

    SPEECH_VOLUME = 1.0

    # ==================================================
    # Weather API
    # ==================================================

    WEATHER_API_KEY = os.getenv(
        "WEATHER_API_KEY",
        ""
    )

    # ==================================================
    # Email
    # ==================================================

    EMAIL_ADDRESS = os.getenv(
        "EMAIL_ADDRESS",
        ""
    )

    EMAIL_PASSWORD = os.getenv(
        "EMAIL_PASSWORD",
        ""
    )

    EMAIL_SMTP_SERVER = os.getenv(
        "EMAIL_SMTP_SERVER",
        "smtp.gmail.com"
    )

    EMAIL_SMTP_PORT = int(
        os.getenv(
            "EMAIL_SMTP_PORT",
            "587"
        )
    )
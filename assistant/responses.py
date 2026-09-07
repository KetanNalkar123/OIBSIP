"""
Standard voice assistant responses.
"""

from datetime import datetime

from config.config import Config


class ResponseManager:
    """Generate standard assistant responses."""

    # ==================================================
    # Greeting
    # ==================================================

    def get_greeting(self):

        hour = datetime.now().hour

        if hour < 12:

            greeting = "Good morning"

        elif hour < 17:

            greeting = "Good afternoon"

        else:

            greeting = "Good evening"

        return (
            f"{greeting}, {Config.USER_NAME}! "
            "How can I help you?"
        )

    # ==================================================
    # Goodbye
    # ==================================================

    def get_goodbye(self):

        return (
            f"Goodbye, {Config.USER_NAME}! "
            "Have a great day."
        )

    # ==================================================
    # Help
    # ==================================================

    def get_help(self):

        return (
            "I can tell you the time and date, "
            "check the weather, search the web, "
            "open websites and Windows applications, "
            "answer knowledge questions, send emails, "
            "and set reminders. "
            "You can also ask me to repeat or cancel."
        )

    # ==================================================
    # Unknown
    # ==================================================

    def get_not_understood(self):

        return (
            "Sorry, I could not understand that. "
            "Please try again."
        )

    # ==================================================
    # Alias
    # ==================================================

    def get_unknown(self):

        return self.get_not_understood()
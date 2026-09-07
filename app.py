"""
OASIS INFOBYTE
Python Programming Internship
Task 1 - Advanced Voice Assistant

Main application file.
"""

import re
import subprocess

from assistant.speech import SpeechManager
from assistant.commands import CommandProcessor
from assistant.responses import ResponseManager
from assistant.services import AssistantServices
from assistant.knowledge import KnowledgeService
from assistant.email_service import EmailService
from assistant.reminder import ReminderService
from assistant.weather import WeatherService


class VoiceAssistant:
    """Main Voice Assistant application."""

    def __init__(self):

        # ==================================================
        # Initialize Services
        # ==================================================

        self.speech = SpeechManager()
        self.commands = CommandProcessor()
        self.responses = ResponseManager()
        self.services = AssistantServices()
        self.knowledge = KnowledgeService()
        self.email = EmailService()
        self.reminder = ReminderService()
        self.weather = WeatherService()

        # ==================================================
        # Assistant State
        # ==================================================

        self.running = True
        self.last_response = ""
        self.waiting_for = None

        # Email conversation data
        self.email_recipient = ""
        self.email_subject = ""
        self.email_body = ""

    # ==================================================
    # Speech Helpers
    # ==================================================

    def speak(self, text):
        """Speak text without updating last_response."""

        if text:
            self.speech.speak(text)

    def speak_and_remember(self, response):
        """Speak response and remember it."""

        if response:
            self.last_response = response
            self.speech.speak(response)

    # ==================================================
    # Greeting
    # ==================================================

    def greet(self):

        response = self.responses.get_greeting()

        self.speak_and_remember(response)

    # ==================================================
    # Handle Command
    # ==================================================

    def handle_command(self, command):
        """Process and execute a user command."""

        # --------------------------------------------------
        # Empty command
        # --------------------------------------------------

        if not command:
            return

        command = command.strip()

        if not command:
            return

        # --------------------------------------------------
        # Detect intent first
        # This allows goodbye/cancel during follow-ups.
        # --------------------------------------------------

        result = self.commands.process(command)
        intent = result.get("intent", "unknown")

        # ==================================================
        # GOODBYE / EXIT
        # ==================================================

        if intent == "goodbye":

            response = self.responses.get_goodbye()

            self.speak_and_remember(response)

            self.running = False
            return

        # ==================================================
        # CANCEL
        # ==================================================

        if intent == "cancel":

            self.cancel_current_operation()
            return

        # ==================================================
        # WEATHER FOLLOW-UP
        # ==================================================

        if self.waiting_for == "weather_city":

            city = command.strip()

            if city:

                response = self.weather.get_weather(city)

                self.waiting_for = None

                self.speak_and_remember(response)

            else:

                self.speak_and_remember(
                    "Please tell me the city name."
                )

            return

        # ==================================================
        # EMAIL FOLLOW-UP
        # ==================================================

        if self.waiting_for in [
            "email_recipient",
            "email_subject",
            "email_body",
            "email_confirmation"
        ]:

            self.send_email_by_voice(command)

            return

        # ==================================================
        # GREETING
        # ==================================================

        if intent == "greeting":

            self.greet()
            return

        # ==================================================
        # TIME
        # ==================================================

        if intent == "time":

            response = self.services.get_current_time()

            self.speak_and_remember(response)

            return

        # ==================================================
        # DATE
        # ==================================================

        if intent == "date":

            response = self.services.get_current_date()

            self.speak_and_remember(response)

            return

        # ==================================================
        # SEARCH
        # ==================================================

        if intent == "search":

            query = result.get("search_query", "")

            if query:

                response = self.services.search_web(query)

                self.speak_and_remember(response)

            else:

                self.speak_and_remember(
                    "What would you like me to search for?"
                )

            return

        # ==================================================
        # OPEN WEBSITE
        # ==================================================

        if intent == "open_website":

            command_text = result.get("text", "").lower()

            websites = {
                "youtube": "https://www.youtube.com",
                "google": "https://www.google.com",
                "github": "https://github.com",
                "gmail": "https://mail.google.com",
                "linkedin": "https://www.linkedin.com",
                "stackoverflow": "https://stackoverflow.com"
            }

            opened = False

            for name, url in websites.items():

                if name in command_text:

                    response = self.services.open_website(url)

                    self.speak_and_remember(response)

                    opened = True
                    break

            if not opened:

                self.speak_and_remember(
                    "I could not identify the website you want to open."
                )

            return

        # ==================================================
        # SYSTEM APPLICATION
        # ==================================================

        if intent == "system_app":

            command_text = result.get("text", "").lower()

            self.open_system_app(command_text)

            return

        # ==================================================
        # WEATHER
        # ==================================================

        if intent == "weather":

            city = self.commands.extract_weather_city(command)

            if city:

                response = self.weather.get_weather(city)

                self.waiting_for = None

                self.speak_and_remember(response)

            else:

                self.waiting_for = "weather_city"

                self.speak_and_remember(
                    "Which city would you like the weather for?"
                )

            return

        # ==================================================
        # KNOWLEDGE
        # ==================================================

        if intent == "knowledge":

            question = result.get("text", command)

            response = self.knowledge.answer(question)

            self.speak_and_remember(response)

            return

        # ==================================================
        # EMAIL
        # ==================================================

        if intent == "email":

            self.start_email_flow()

            return

        # ==================================================
        # REMINDER
        # ==================================================

        if intent == "reminder":

            self.set_reminder_by_voice()

            return

        # ==================================================
        # HELP
        # ==================================================

        if intent == "help":

            response = self.responses.get_help()

            self.speak_and_remember(response)

            return

        # ==================================================
        # REPEAT
        # ==================================================

        if intent == "repeat":

            if self.last_response:

                self.speech.speak(self.last_response)

            else:

                self.speech.speak(
                    "There is no previous response to repeat."
                )

            return

        # ==================================================
        # UNKNOWN
        # ==================================================

        response = self.responses.get_not_understood()

        self.speak_and_remember(response)

    # ==================================================
    # Cancel Current Operation
    # ==================================================

    def cancel_current_operation(self):

        self.waiting_for = None

        self.email_recipient = ""
        self.email_subject = ""
        self.email_body = ""

        self.speak_and_remember(
            "Okay, the current operation has been cancelled."
        )

    # ==================================================
    # Open Windows System Application
    # ==================================================

    def open_system_app(self, command_text):

        try:

            if (
                "calculator" in command_text
                or "calc" in command_text
            ):

                subprocess.Popen("calc.exe")

                self.speak_and_remember(
                    "Opening Calculator."
                )

            elif "notepad" in command_text:

                subprocess.Popen("notepad.exe")

                self.speak_and_remember(
                    "Opening Notepad."
                )

            elif (
                "file explorer" in command_text
                or "explorer" in command_text
            ):

                subprocess.Popen("explorer.exe")

                self.speak_and_remember(
                    "Opening File Explorer."
                )

            elif (
                "command prompt" in command_text
                or "cmd" in command_text
            ):

                subprocess.Popen("cmd.exe")

                self.speak_and_remember(
                    "Opening Command Prompt."
                )

            else:

                self.speak_and_remember(
                    "I could not identify the application."
                )

        except Exception as error:

            print(
                f"Application error: {error}"
            )

            self.speak_and_remember(
                "I could not open that application."
            )

    # ==================================================
    # Start Email Flow
    # ==================================================

    def start_email_flow(self):
        """Start the email conversation."""

        if not self.email.is_configured():

            self.speak_and_remember(
                "The email service is not configured."
            )

            return

        self.email_recipient = ""
        self.email_subject = ""
        self.email_body = ""

        self.waiting_for = "email_recipient"

        self.speak_and_remember(
            "Who should I send the email to?"
        )

    # ==================================================
    # Email by Voice
    # ==================================================

    def send_email_by_voice(self, current_input=None):
        """Continue email conversation using voice input."""

        # ==================================================
        # Recipient
        # ==================================================

        if self.waiting_for == "email_recipient":

            recipient = (
                current_input
                if current_input
                else self.speech.listen(seconds=5)
            )

            if not recipient:

                self.speak_and_remember(
                    "I could not understand the recipient email address."
                )

                self.waiting_for = None
                return

            recipient = self.normalize_email(recipient)

            if not self.is_valid_email(recipient):

                self.speak_and_remember(
                    "That does not look like a valid email address. "
                    "Please say the email address again."
                )

                return

            self.email_recipient = recipient

            print(
                f"Recipient: {recipient}"
            )

            self.waiting_for = "email_subject"

            self.speak(
                "What is the subject of the email?"
            )

            return

        # ==================================================
        # Subject
        # ==================================================

        if self.waiting_for == "email_subject":

            subject = (
                current_input
                if current_input
                else self.speech.listen(seconds=5)
            )

            if not subject:

                self.speak_and_remember(
                    "I could not understand the email subject."
                )

                self.waiting_for = None
                return

            self.email_subject = subject.strip()

            self.waiting_for = "email_body"

            self.speak(
                "What would you like me to write in the email?"
            )

            return

        # ==================================================
        # Body
        # ==================================================

        if self.waiting_for == "email_body":

            body = (
                current_input
                if current_input
                else self.speech.listen(seconds=8)
            )

            if not body:

                self.speak_and_remember(
                    "I could not understand the email message."
                )

                self.waiting_for = None
                return

            self.email_body = body.strip()

            self.waiting_for = "email_confirmation"

            self.speak(
                f"I am going to send an email to "
                f"{self.email_recipient} "
                f"with the subject "
                f"{self.email_subject}. "
                f"Should I send it?"
            )

            return

        # ==================================================
        # Confirmation
        # ==================================================

        if self.waiting_for == "email_confirmation":

            confirmation = (
                current_input
                if current_input
                else self.speech.listen(seconds=5)
            )

            if not confirmation:

                self.waiting_for = None

                self.speak_and_remember(
                    "I did not receive confirmation. "
                    "The email was not sent."
                )

                return

            confirmation = confirmation.lower().strip()

            positive_words = [
                "yes",
                "yeah",
                "yep",
                "send",
                "send it",
                "confirm",
                "okay",
                "ok",
                "sure"
            ]

            negative_words = [
                "no",
                "nope",
                "cancel",
                "don't",
                "do not"
            ]

            # --------------------------------------------------
            # Negative confirmation
            # --------------------------------------------------

            if any(
                word in confirmation
                for word in negative_words
            ):

                self.waiting_for = None

                self.speak_and_remember(
                    "Okay. The email was not sent."
                )

                return

            # --------------------------------------------------
            # Positive confirmation
            # --------------------------------------------------

            if not any(
                word in confirmation
                for word in positive_words
            ):

                self.speak_and_remember(
                    "Please say yes to send the email "
                    "or no to cancel it."
                )

                return

            self.waiting_for = None

            self.speak(
                "Sending the email now."
            )

            success, message = self.email.send_email(
                self.email_recipient,
                self.email_subject,
                self.email_body
            )

            if success:

                self.speak_and_remember(
                    "Your email has been sent successfully."
                )

            else:

                self.speak_and_remember(message)

            # Clear email data after sending
            self.email_recipient = ""
            self.email_subject = ""
            self.email_body = ""

    # ==================================================
    # Normalize Email Address
    # ==================================================

    @staticmethod
    def normalize_email(email):

        email = email.lower().strip()

        replacements = {
            " at the rate ": "@",
            " at rate ": "@",
            " at ": "@",
            " dot ": ".",
            " underscore ": "_",
            " dash ": "-",
            " hyphen ": "-"
        }

        for spoken, symbol in replacements.items():

            email = email.replace(
                spoken,
                symbol
            )

        email = email.replace(" ", "")

        return email

    # ==================================================
    # Validate Email
    # ==================================================

    @staticmethod
    def is_valid_email(email):

        pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

        return re.match(pattern, email) is not None

    # ==================================================
    # Set Reminder by Voice
    # ==================================================

    def set_reminder_by_voice(self):
        """Create reminder using voice input."""

        self.speak(
            "What should I remind you about?"
        )

        reminder_text = self.speech.listen(
            seconds=5
        )

        if not reminder_text:

            self.speak_and_remember(
                "I could not understand the reminder."
            )

            return

        print(
            f"Reminder: {reminder_text}"
        )

        self.speak(
            "When should I remind you?"
        )

        reminder_time = self.speech.listen(
            seconds=5
        )

        if not reminder_time:

            self.speak_and_remember(
                "I could not understand the reminder time."
            )

            return

        print(
            f"Reminder time: {reminder_time}"
        )

        seconds = self.reminder.parse_duration(
            reminder_time
        )

        if seconds is None:

            self.speak_and_remember(
                "I could not understand the reminder time. "
                "Please say something like 10 minutes or 2 hours."
            )

            return

        result = self.reminder.add_reminder(
            reminder_text,
            seconds
        )

        self.speak_and_remember(result)

    # ==================================================
    # Run Assistant
    # ==================================================

    def run(self):

        print("=" * 65)
        print("             OASIS INFOBYTE")
        print("             VOICE ASSISTANT")
        print("=" * 65)

        print("\nVoice Assistant is ready.")
        print("You can speak naturally.")
        print("Say 'goodbye' or 'exit' to stop.")

        print("=" * 65)

        self.greet()

        while self.running:

            try:

                command = self.speech.listen(
                    seconds=5
                )

                self.handle_command(command)

            except KeyboardInterrupt:

                print(
                    "\nAssistant stopped by user."
                )

                self.running = False

            except Exception as error:

                print(
                    f"\nUnexpected error: {error}"
                )

                self.speech.speak(
                    "Something went wrong. "
                    "Please try again."
                )

        print(
            "\nVoice Assistant stopped."
        )

        print(
            "Thank you for using the assistant!"
        )


# ======================================================
# MAIN
# ======================================================

def main():

    assistant = VoiceAssistant()

    assistant.run()


if __name__ == "__main__":

    main()
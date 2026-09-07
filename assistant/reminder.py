"""
Reminder service for the voice assistant.
"""

import re
import threading


class ReminderService:
    """Manage timed reminders."""

    def __init__(self):

        self.active_reminders = []

        self.lock = threading.Lock()

    # ==================================================
    # Add Reminder
    # ==================================================

    def add_reminder(self, message, seconds):

        if not message:

            return (
                "The reminder message cannot be empty."
            )

        if seconds is None or seconds <= 0:

            return (
                "The reminder duration must be greater than zero."
            )

        timer = threading.Timer(
            seconds,
            self._trigger_reminder,
            args=(message,)
        )

        timer.daemon = True

        with self.lock:

            self.active_reminders.append(
                timer
            )

        timer.start()

        duration = self.format_duration(
            seconds
        )

        return (
            f"Reminder set for {duration}. "
            f"I will remind you to {message}."
        )

    # ==================================================
    # Trigger Reminder
    # ==================================================

    def _trigger_reminder(self, message):

        print("\n")
        print("=" * 50)
        print("🔔 REMINDER")
        print("=" * 50)
        print(
            f"Reminder: {message}"
        )
        print("=" * 50)
        print("\n")

    # ==================================================
    # Format Duration
    # ==================================================

    @staticmethod
    def format_duration(seconds):

        seconds = int(seconds)

        if seconds < 60:

            return (
                f"{seconds} seconds"
            )

        if seconds < 3600:

            minutes = seconds // 60

            return (
                f"{minutes} minute"
                f"{'s' if minutes != 1 else ''}"
            )

        hours = seconds // 3600

        remaining_minutes = (
            seconds % 3600
        ) // 60

        if remaining_minutes:

            return (
                f"{hours} hour"
                f"{'s' if hours != 1 else ''} "
                f"and {remaining_minutes} minute"
                f"{'s' if remaining_minutes != 1 else ''}"
            )

        return (
            f"{hours} hour"
            f"{'s' if hours != 1 else ''}"
        )

    # ==================================================
    # Parse Duration
    # ==================================================

    def parse_duration(self, text):

        if not text:

            return None

        text = text.lower().strip()

        # --------------------------------------------------
        # Convert common number words
        # --------------------------------------------------

        number_words = {
            "zero": 0,
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "ten": 10,
            "eleven": 11,
            "twelve": 12,
            "thirteen": 13,
            "fourteen": 14,
            "fifteen": 15,
            "sixteen": 16,
            "seventeen": 17,
            "eighteen": 18,
            "nineteen": 19,
            "twenty": 20
        }

        for word, number in number_words.items():

            text = re.sub(
                rf"\b{word}\b",
                str(number),
                text
            )

        # --------------------------------------------------
        # Number + unit
        # --------------------------------------------------

        pattern = (
            r"(\d+(?:\.\d+)?)\s*"
            r"(seconds?|secs?|s|"
            r"minutes?|mins?|m|"
            r"hours?|hrs?|h)"
        )

        match = re.search(
            pattern,
            text
        )

        if not match:

            return None

        value = float(
            match.group(1)
        )

        unit = match.group(2)

        if unit.startswith(
            ("second", "sec", "s")
        ):

            seconds = value

        elif unit.startswith(
            ("minute", "min", "m")
        ):

            seconds = value * 60

        elif unit.startswith(
            ("hour", "hr", "h")
        ):

            seconds = value * 3600

        else:

            return None

        return int(seconds)
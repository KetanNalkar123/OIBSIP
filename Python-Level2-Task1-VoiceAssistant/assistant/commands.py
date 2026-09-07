"""
Command processing and intent detection
for the OASIS INFOBYTE Advanced Voice Assistant.
"""

import re


class CommandProcessor:
    """Detect user intent and extract useful information."""

    def __init__(self):

        # ==================================================
        # Command Patterns
        # ==================================================

        self.command_patterns = {

            "greeting": [
                r"\bhello\b",
                r"\bhi\b",
                r"\bhey\b",
                r"\bgood morning\b",
                r"\bgood afternoon\b",
                r"\bgood evening\b"
            ],

            "time": [
                r"\bwhat(?:'s| is)? the time\b",
                r"\bcurrent time\b",
                r"\btell me the time\b",
                r"\btime now\b"
            ],

            "date": [
                r"\bwhat(?:'s| is)? the date\b",
                r"\bwhat day is it\b",
                r"\btoday(?:'s)? date\b",
                r"\btell me the date\b"
            ],

            "open_website": [
                r"^\s*open\s+(youtube|google|github|gmail|linkedin|stackoverflow)\s*$",
                r"^\s*open\s+(youtube|google|github|gmail|linkedin|stackoverflow)\b"
            ],

            "system_app": [
                r"\bopen calculator\b",
                r"\bopen calc\b",
                r"\bcalculator\b",
                r"\bopen notepad\b",
                r"\bnotepad\b",
                r"\bopen file explorer\b",
                r"\bfile explorer\b",
                r"\bopen explorer\b",
                r"\bopen command prompt\b",
                r"\bcommand prompt\b",
                r"\bopen cmd\b"
            ],

            "weather": [
                r"\bweather\b",
                r"\btemperature\b",
                r"\bforecast\b"
            ],

            "knowledge": [
                r"\bwho created\b",
                r"\bwho invented\b",
                r"\bwho developed\b",
                r"\bwhat is\b",
                r"\bwhat are\b",
                r"\bexplain\b",
                r"\bdefine\b",
                r"\bwho is\b"
            ],

            "email": [
                r"\bsend an email\b",
                r"\bsend email\b",
                r"\bwrite an email\b",
                r"\bemail\b"
            ],

            "reminder": [
                r"\bset a reminder\b",
                r"\bset reminder\b",
                r"\bremind me\b",
                r"\bcreate a reminder\b"
            ],

            "help": [
                r"\bhelp\b",
                r"\bwhat can you do\b",
                r"\bcommands\b",
                r"\bwhat can i ask\b"
            ],

            "repeat": [
                r"^\s*repeat\s*$",
                r"\brepeat that\b",
                r"\bsay that again\b",
                r"\bsay it again\b"
            ],

            "cancel": [
                r"^\s*cancel\s*$",
                r"\bcancel that\b",
                r"\bcancel it\b",
                r"\bstop that\b"
            ],

            "goodbye": [
                r"\bgoodbye\b",
                r"\bbye\b",
                r"\bexit\b",
                r"\bquit\b",
                r"\bstop assistant\b"
            ],

            "search": [
                r"^\s*search\b",
                r"^\s*google\s+",
                r"^\s*look up\b",
                r"^\s*find\b"
            ]
        }

    # ==================================================
    # Clean Text
    # ==================================================

    @staticmethod
    def clean_text(text):

        if not text:
            return ""

        text = text.lower().strip()

        text = re.sub(
            r"\s+",
            " ",
            text
        )

        return text

    # ==================================================
    # Detect Intent
    # ==================================================

    def detect_intent(self, text):

        text = self.clean_text(text)

        if not text:
            return "unknown"

        # --------------------------------------------------
        # Priority 1: Goodbye
        # --------------------------------------------------

        for pattern in self.command_patterns["goodbye"]:

            if re.search(pattern, text):
                return "goodbye"

        # --------------------------------------------------
        # Priority 2: Cancel
        # --------------------------------------------------

        for pattern in self.command_patterns["cancel"]:

            if re.search(pattern, text):
                return "cancel"

        # --------------------------------------------------
        # Priority 3: Open Website
        # --------------------------------------------------

        for pattern in self.command_patterns["open_website"]:

            if re.search(pattern, text):

                return "open_website"

        # --------------------------------------------------
        # Priority 4: System Applications
        # --------------------------------------------------

        for pattern in self.command_patterns["system_app"]:

            if re.search(pattern, text):

                return "system_app"

        # --------------------------------------------------
        # Priority 5: Search
        # --------------------------------------------------

        for pattern in self.command_patterns["search"]:

            if re.search(pattern, text):

                return "search"

        # --------------------------------------------------
        # Other intents
        # --------------------------------------------------

        priority_order = [
            "email",
            "reminder",
            "weather",
            "time",
            "date",
            "help",
            "repeat",
            "greeting",
            "knowledge"
        ]

        for intent in priority_order:

            for pattern in self.command_patterns[intent]:

                if re.search(pattern, text):

                    return intent

        return "unknown"

    # ==================================================
    # Extract Search Query
    # ==================================================

    def extract_search_query(self, text):

        text = self.clean_text(text)

        prefixes = [
            "search for ",
            "search ",
            "google ",
            "look up ",
            "find "
        ]

        for prefix in prefixes:

            if text.startswith(prefix):

                query = text[
                    len(prefix):
                ].strip()

                return query

        return ""

    # ==================================================
    # Extract Website
    # ==================================================

    def extract_website(self, text):

        text = self.clean_text(text)

        websites = [
            "youtube",
            "google",
            "github",
            "gmail",
            "linkedin",
            "stackoverflow"
        ]

        for website in websites:

            if website in text:

                return website

        return ""

    # ==================================================
    # Extract System App
    # ==================================================

    def extract_system_app(self, text):

        text = self.clean_text(text)

        if "calculator" in text or "calc" in text:
            return "calculator"

        if "notepad" in text:
            return "notepad"

        if "file explorer" in text or "explorer" in text:
            return "explorer"

        if "command prompt" in text or "cmd" in text:
            return "cmd"

        return ""

    # ==================================================
    # Extract Weather City
    # ==================================================

    def extract_weather_city(self, text):

        text = self.clean_text(text)

        phrases = [
            "weather in ",
            "temperature in ",
            "forecast for ",
            "weather at ",
            "temperature at ",
            "weather of "
        ]

        for phrase in phrases:

            if phrase in text:

                city = text.split(
                    phrase,
                    1
                )[1].strip()

                return city

        return ""

    # ==================================================
    # Process Command
    # ==================================================

    def process(self, text):

        clean = self.clean_text(text)

        intent = self.detect_intent(clean)

        result = {
            "text": clean,
            "intent": intent,
            "search_query": ""
        }

        if intent == "search":

            result["search_query"] = (
                self.extract_search_query(clean)
            )

        return result


# ======================================================
# Testing
# ======================================================

if __name__ == "__main__":

    processor = CommandProcessor()

    test_commands = [
        "Hello",
        "What time is it",
        "What is today's date",
        "Open Google",
        "Open YouTube",
        "Search machine learning",
        "Google Python programming",
        "What's the weather in Pune",
        "Who created Python",
        "What is artificial intelligence",
        "Send an email",
        "Set a reminder",
        "Help",
        "Repeat",
        "Cancel",
        "Goodbye"
    ]

    print("=" * 60)
    print("COMMAND PROCESSOR TEST")
    print("=" * 60)

    for command in test_commands:

        result = processor.process(command)

        print(
            f"{command:<35} -> "
            f"{result['intent']}"
        )

    print("=" * 60)
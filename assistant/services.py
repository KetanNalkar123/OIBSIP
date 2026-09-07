"""
Services Module
---------------
Provides actions that the Voice Assistant can perform.

OASIS INFOBYTE
Python Programming Internship
Task 1 - Advanced Voice Assistant
"""

from datetime import datetime
import webbrowser
from urllib.parse import quote_plus


class AssistantServices:
    """Handles external and system-related assistant services."""

    # --------------------------------------------------
    # Current Time
    # --------------------------------------------------

    @staticmethod
    def get_current_time():
        """Return the current local time."""

        current_time = datetime.now().strftime("%I:%M %p")

        return f"The current time is {current_time}."

    # --------------------------------------------------
    # Current Date
    # --------------------------------------------------

    @staticmethod
    def get_current_date():
        """Return the current date."""

        current_date = datetime.now().strftime("%A, %d %B %Y")

        return f"Today is {current_date}."

    # --------------------------------------------------
    # Web Search
    # --------------------------------------------------

    @staticmethod
    def search_web(query):
        """
        Open a Google search for the provided query.

        Parameters:
            query (str): Search query.

        Returns:
            str: Status message.
        """

        if not query:
            return "Please tell me what you want me to search for."

        encoded_query = quote_plus(query)

        search_url = (
            f"https://www.google.com/search?q={encoded_query}"
        )

        try:

            webbrowser.open(search_url)

            return f"Searching the web for {query}."

        except Exception as error:

            print(f"Search error: {error}")

            return "I could not open the web browser."

    # --------------------------------------------------
    # Open Website
    # --------------------------------------------------

    @staticmethod
    def open_website(url):
        """
        Open a website in the default browser.

        Parameters:
            url (str): Website URL.

        Returns:
            str: Status message.
        """

        try:

            webbrowser.open(url)

            return f"Opening {url}."

        except Exception as error:

            print(f"Website error: {error}")

            return "I could not open the website."


# ------------------------------------------------------
# Test
# ------------------------------------------------------

if __name__ == "__main__":

    services = AssistantServices()

    print("=" * 60)
    print("       ASSISTANT SERVICES TEST")
    print("=" * 60)

    # Test time
    print("\nTime:")
    print(services.get_current_time())

    # Test date
    print("\nDate:")
    print(services.get_current_date())

    # Test search
    print("\nSearch:")
    print(
        services.search_web(
            "Python programming"
        )
    )

    print("\n" + "=" * 60)
    print("Services test completed.")
    print("=" * 60)
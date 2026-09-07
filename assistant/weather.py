"""
Weather service using OpenWeather API.
"""

import requests

from config.config import Config


class WeatherService:
    """Retrieve current weather information."""

    def __init__(self):

        self.api_key = Config.WEATHER_API_KEY

        self.base_url = (
            "https://api.openweathermap.org/data/2.5/weather"
        )

    # ==================================================
    # Get Weather
    # ==================================================

    def get_weather(self, city):

        if not city:

            return (
                "Please tell me the city name."
            )

        if not self.api_key:

            return (
                "Weather API key is not configured."
            )

        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }

        try:

            response = requests.get(
                self.base_url,
                params=params,
                timeout=10
            )

            if response.status_code == 404:

                return (
                    f"I could not find the city {city}."
                )

            if response.status_code == 401:

                return (
                    "The weather API key is invalid."
                )

            response.raise_for_status()

            data = response.json()

            temperature = data["main"]["temp"]

            feels_like = data["main"]["feels_like"]

            humidity = data["main"]["humidity"]

            description = (
                data["weather"][0]["description"]
            )

            wind_speed = data["wind"]["speed"]

            return (
                f"Weather in {city}: {description}. "
                f"Temperature is "
                f"{temperature:.1f} degrees Celsius, "
                f"feels like "
                f"{feels_like:.1f} degrees Celsius. "
                f"Humidity is "
                f"{humidity} percent. "
                f"Wind speed is "
                f"{wind_speed} meters per second."
            )

        except requests.exceptions.Timeout:

            return (
                "The weather service took too long "
                "to respond."
            )

        except requests.exceptions.ConnectionError:

            return (
                "I could not connect to the weather service."
            )

        except requests.exceptions.RequestException as error:

            print(
                f"Weather API error: {error}"
            )

            return (
                "I could not retrieve the weather information."
            )

        except (
            KeyError,
            TypeError,
            ValueError
        ) as error:

            print(
                f"Weather data error: {error}"
            )

            return (
                "The weather service returned "
                "unexpected data."
            )
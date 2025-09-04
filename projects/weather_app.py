import os
from typing import Literal, Union

from dotenv import load_dotenv
import requests

ReportStyle = Literal["formal", "casual", "technical"]
TemperatureUnits = Literal["K", "F", "C"]


class WeatherApp:
    DEFAULT_TEMP_UNIT = "C"
    DEFAULT_HOT_TEMP = (30, None)
    DEFAULT_MID_TEMP = (16, 29)
    DEFAULT_COLD_TEMP = (None, 15)

    def __init__(self):
        load_dotenv()
        self.request_session = requests.Session()

    def get_weather(self, city: str) -> Union[dict, None]:
        try:
            params_payload = {
                "q": city,
                "appid": os.getenv("WEATHER_APP_API_KEY"),
                "units": "metric",
            }

            response = self.request_session.get(
                url="https://api.openweathermap.org/data/2.5/weather",
                params=params_payload,
            )

            response.raise_for_status()

            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"Oops! Something went wrong: {e}")
            return None

    def explain_weather(
        self, weather: dict, style: ReportStyle = "formal"
    ) -> Union[str, bool]:
        try:
            if not weather:
                raise Exception("Weather obj not found or invalid")

            ex_weather = f"The weather in {weather['name']} is {weather['weather'][0]['description']}."

            ex_temperature = self.explain_temperature(weather, style=style)

            if not ex_temperature:
                raise Exception(f"Error explaining temperature. {ex_temperature}")

            ex_weather = " ".join([ex_weather, ex_temperature])

            return ex_weather
        except Exception as e:
            print(f"Something went wrong: {e.with_traceback(None)}")
            return False

    def explain_temperature(
        self,
        weather: dict,
        prefered_temp_unit: TemperatureUnits = "C",
        style: ReportStyle = "formal",
    ) -> Union[str, bool]:
        try:
            weth = weather["main"]

            if not weth:
                raise Exception("Unknown weather obj")

            current_temp = weth["temp"]

            forecast_lines = {
                "hot": {
                    "formal": lambda temp, unit: f"Temperatures are expected to exceed {temp}{unit}, advising caution regarding heat exposure.",
                    "casual": lambda temp, unit: f"At {temp}{unit} it's gonna be a scorcher out there today, so drink plenty of water.",
                    "technical": lambda temp, unit: f"A high-pressure system is maintaining elevated surface temperatures above {temp}{unit}.",
                },
                "mid": {
                    "formal": lambda temp, unit: f"Today's forecast calls for mild conditions, with temperatures at {temp}{unit}.",
                    "casual": lambda temp, unit: f"It's a nice {temp}{unit} right now, perfect for enjoying the outdoors.",
                    "technical": lambda temp, unit: f"The atmospheric temperature is currently {temp}{unit}, consistent with a temperate air mass.",
                },
                "cold": {
                    "formal": lambda temp, unit: f"A cold front has lowered the temperature to {temp}{unit}, with colder conditions probably later in the day.",
                    "casual": lambda temp, unit: f"It feels a bit chilly at {temp}{unit}; make sure to grab a jacket.",
                    "technical": lambda temp, unit: f"The current thermal reading of {temp}{unit} is indicating a cold air mass advection.",
                },
            }

            forecast = None

            current_temp_int = int(current_temp)
            current_temp_unit = "°C"

            if current_temp_int >= self.DEFAULT_HOT_TEMP[0]:
                forecast = forecast_lines["hot"][style](
                    current_temp_int, current_temp_unit
                )
            elif (
                current_temp_int >= self.DEFAULT_MID_TEMP[0]
                and current_temp_int <= self.DEFAULT_MID_TEMP[1]
            ):
                forecast = forecast_lines["mid"][style](
                    current_temp_int, current_temp_unit
                )
            elif current_temp_int <= self.DEFAULT_COLD_TEMP[1]:
                forecast = forecast_lines["cold"][style](
                    current_temp_int, current_temp_unit
                )

            if not forecast:
                raise Exception(
                    "Could not set forecast, something might be wrong with the temperature."
                )

            return forecast

        except Exception as e:
            print(f"Somehting went wrong: {e}")
            return False


if __name__ == "__main__":
    app = WeatherApp()

    weather = app.get_weather("new york")

    if weather:
        print(app.explain_weather(weather))

        print(app.explain_weather(weather, style="casual"))

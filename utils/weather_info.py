from dotenv import load_dotenv
import os
import requests

class WeatherTool():
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("OPENWEATHERMAP_API_KEY")
        self.api_url = "https://api.openweathermap.org/data/2.5"

    def get_weather(self, place: str):
        try:
            url = f"{self.api_url}/weather"
            params = {
                "q": place,
                "appid": self.api_key,
                "units": "metric"
            }
            res = requests.get(url=url, params=params)
            return res.json() if res.status_code == 200 else {}
        except Exception as e:
            raise e

    def get_forecast(self, place:str):
        try:
            url = f"{self.api_url}/forecast"
            params = {
                "q": place,
                "appid": self.api_key,
                "units": "metric"
            }
            res = requests.get(url=url,params=params)
            return res.json() if res.status_code == 200 else {}
        except Exception as e:
            raise e
from langchain.tools import tool
from utils.weather_info import WeatherTool


class Weather():
    def __init__(self):
        self.weather_tool = WeatherTool()
        self.weather_tool_list = self._setup_tools()
    def _setup_tools(self):
        @tool
        def get_current_weather(city: str):
            """
            Fetch current weather information for a given city.
            Use this tool when the user asks about weather
            conditions at a travel destination.

            """
            weather_data = self.weather_tool.get_weather(place = city)
            if weather_data:
                temp = weather_data.get('main',{}).get('temp','N/A') # same as ---> temp = weather_data["main"]["temp"] 
                feels_like = weather_data.get('main',{}).get('feels_like','N/A')
                desc  = weather_data.get('weather',[{}])[0].get('description','N/A')
                return (
                    f"Current weather in {city}: "
                    f"Temperature: {temp}°C, "
                    f"Feels like: {feels_like}°C, "
                    f"Description: {desc}"
                )
            return f"Not able to retrieve weather information for {city}"

        @tool
        def get_weather_forecast(city: str):
            """
            Fetch weather foreast for the given city
            Use this tool when the user asks about the 
            forecast for a given location.
            """
            forecast_data = self.weather_tool.get_forecast(place = city)
            if forecast_data and 'list' in forecast_data:
                summary = []
                for item in forecast_data['list']:
                    date = item['dt_txt'].split(' ')[0] # dt_txt contains data like '2026-10-31 09:00:00', so we split it and take only the date part using "split(' ')[0]""
                    temp = item['main']['temp']
                    feels_like = item['main']['feels_like']
                    rain_prob = item['pop']
                    desc = item['weather'][0]['description']
                    weatherinfo = (
                        f"Date: {date}, "
                        f"Temperature: {temp}°C, "
                        f"Feels like: {feels_like}°C, "
                        f"Rain probability: {rain_prob * 100}%, "
                        f"Description: {desc}"
                    )
                    summary.append(weatherinfo)
                return f"Forecast for the {city}\n" + "\n".join(summary)
            return f" No forecast could be fetched for {city}"

        return [get_current_weather, get_weather_forecast]
                
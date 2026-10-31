from langchain.tools import tool
from utils.place_search import PlaceSearcher

class PlaceSearchTool():
    def __init__(self):
        self.search_api = PlaceSearcher()
        self.place_search_tool_list = self._setup_tools()
    def _setup_tools(self):
        @tool
        def search_restaurants(location:str, preference:str = 'any'):
            """Search for restaurants and cafes in a given location.

            Args:
                location: City or destination to search in.
                preference: Food preference, cuisine or budget.
            """
            query = f"Best {preference} restaurants in and around {location}"
            return self.search_api.search_places(query=query)

        @tool
        def search_hotels(location:str, budget: str = 0):
            """Search for hotels and accommodation in a destination.

            Args:
                location: City or destination.
                budget:(example: $150 or ₹1000) Preferred accommodation budget per room, per night. Use 0 if no budget is specified by user.
            """
            if budget > 0:
                query = f"Best hotels in and around {location} under {budget} per night."
            else:
                query = f"Best hotels in and around {location}."
            return self.search_api.search_places(query=query)

        @tool
        def search_tourist_attractions(location:str):
            """Search for tourist attractions and activities in a destination.

            Args:
                location: City or destination.
            """
            query = f"Best tourist attractions and activities to do in and around {location}."
            return self.search_api.search_places(query=query)

        @tool
        def search_transportation(starting_point:str, destination:str, type_of_transport: str = 'any'):
            """Search for transportation options in a destination.

            Args:
                starting_point: Place from which the trip starts.
                destinations: destination city or place.
                type_of_transport: Type of transport such as bus, train, flight or taxi.
            """
            query = f"{type_of_transport} options available from {starting_point} to {destination}"
            return self.search_api.search_places(query=query)
        
        return [
            search_hotels,
            search_restaurants,
            search_tourist_attractions,
            search_transportation
        ]



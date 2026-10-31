from langchain_tavily import TavilySearch
from dotenv import load_dotenv
load_dotenv()

class PlaceSearcher():
    def __init__(self):
        self.place_search_tool = TavilySearch(
            max_results = 5,
            search_depth = 'basic',
            topic = 'general',
            include_answer = True
        )
    def search_places(self, query:str):
        return self.place_search_tool.invoke({'query':query})
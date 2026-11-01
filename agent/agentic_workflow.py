from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.graph import START, END, StateGraph, MessagesState
from utils.model_loader import ModelLoader
from prompt_library.prompt import SYSTEM_PROMPT

from tools.weather import Weather
from tools.currency_conversion import CurrencyConvertorTool
from tools.place_search import PlaceSearchTool
from tools.calculator import CalculatorTool
from tools.budget_calculator import BudgetTool

class Agent():
    def __init__(self):
        self.tools = []
        self.weather_tools = Weather().weather_tool_list
        self.currency_convertor_tools = CurrencyConvertorTool().currency_convertor_tool_list
        self.place_search_tools = PlaceSearchTool().place_search_tool_list
        self.calculator_tool = CalculatorTool().calculator_tool_list
        self.budget_tool = BudgetTool().budget_tool_list
        self.tools.extend(self.weather_tools)
        self.tools.extend(self.currency_convertor_tools)
        self.tools.extend(self.place_search_tools)
        self.tools.extend(self.calculator_tool)
        self.tools.extend(self.budget_tool)
        
        self.system_prompt = SYSTEM_PROMPT
        self.llm = ModelLoader.load_llm()
        self.llm_with_tools = self.llm.bind_tools(tools = self.tools)
        
    def agent_function(self,state:MessagesState):
        """Main Agent Function"""
        user_question = state["messages"]
        input_question = [self.system_prompt] + user_question
        response = self.llm_with_tools.invoke(input_question)
        return {"messages":[response]}

    def build_graph(self):
        graph_builder = StateGraph(MessagesState)
        graph_builder.add_node("agent", self.agent_function)
        graph_builder.add_node("tools",ToolNode(tools=self.tools))
        graph_builder.add_edge(START, "agent")
        graph_builder.add_conditional_edges("agent",tools_condition)
        graph_builder.add_edge("tools","agent")
        

        self.graph = graph_builder.compile()
        return self.graph
    def __call__(self):
        return self.build_graph()
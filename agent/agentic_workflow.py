from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.graph import START, END, StateGraph, MessagesState
from utils.model_loader import ModelLoader
from prompt_library.prompt import SYSTEM_PROMPT

class GraphBuilder():
    def __init__(self):
        self.tools = [
            #Tools 
        ]
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
        graph_builder.add_edge("agent",END)

        self.graph = graph_builder.compile()
        return self.graph
    def __call__(self):
        return self.build_graph()
from pydantic import BaseModel, Field, ConfigDict
from typing_extensions import Literal, Optional
from config_loader import ConfigLoader
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()

class ModelLoader(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True) ## This allows us to use custom python classes for validation.
    ## "model_config" is a specially recognised variable in pydantic V2 so don't change the variable name.
    model_provider: Literal["groq"] = "groq"
    config: ConfigLoader = Field(default_factory=ConfigLoader ,exclude= True)


    def load_llm(self):
        print("LLM LOADING.....")
        print(f"LOADING MODEL FROM PROVIDER:{self.model_provider}")
        groq_api_key = os.getenv("GROQ_API_KEY")
        model_name = self.config["llm"]["groq"]["model_name"]
        llm = ChatGroq(model=model_name, api_key=groq_api_key)
        
        return llm

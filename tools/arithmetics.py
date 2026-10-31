import os
from dotenv import load_dotenv
from langchain.tools import tool

@tool
def add(a:int,b:int) -> int:
    """
    Returns sum of two integers.
    input: a:int,b:int
    output = a + b
    """
    return a+b

@tool
def multiply(a:int,b:int) -> int:
    """
    Returns prod of two integers.
    input: a:int,b:int
    output = a * b
    """
    return a*b
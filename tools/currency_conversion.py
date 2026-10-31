from utils.currency_converter import CurrencyConvertor
from langchain.tools import tool

class CurrencyConvertorTool():
    def __init__(self):
        self.api = CurrencyConvertor()
        self.currency_convertor_tool_list = self._setup_tools()

    def _setup_tools(self):
         @tool
         def currency_convertor_tool(amount:float, base_currency:str, target_currency:str):
            """Converts an amount from one currency to another using the latest exchange rates.

                Args:
                    amount (float): The amount to convert.
                    base_currency (str): The three-letter currency code of the original currency (e.g., INR, USD).
                    target_currency (str): The three-letter currency code of the desired currency (e.g., USD, EUR).

                Returns:
                    float: The converted amount in the target currency.
            """ 
            converted_amount = self.api.convert_currency(amount=amount, base_currency=base_currency, target_currency=target_currency)
            return converted_amount
         return [currency_convertor_tool]
import os
from dotenv import load_dotenv
import requests
load_dotenv()

class CurrencyConvertor():
    def __init__(self):
        self.api_key = os.getenv("EXCHANGE_RATE_API_KEY")
        self.base_url = f"https://v6.exchangerate-api.com/v6/{self.api_key}/latest"

    def convert_currency(self, amount: float, base_currency:str, target_currency:str):
        try:    
            url = f"{self.base_url}/{base_currency.upper()}"
            res = requests.get(url=url)
            exchange_rate = res.json()["conversion_rates"][target_currency.upper()]
            return amount * exchange_rate
        except Exception as e:
            raise e
        
#checking api
"""        
cur_con = CurrencyConvertor()

result = cur_con.convert_currency(5000.00, base_currency='USD', target_currency='INR')
print("$5000 = Rs. ",result)
"""

from langchain.tools import tool

class BudgetTool():
    def __init__(self):
        self.budget_tool_list = self._setup_tools()

    def _setup_tools(self):
        @tool
        def plan_trip_budget(total_budget: float, no_of_people: int, no_of_days: int, currency:str = 'INR') -> dict:
            
            """
            Create a budget allocation plan for a trip based on the
            traveller's available budget, number of travellers and
            trip duration.
            
            Use this tool when a user already has a total trip budget
            and wants to distribute it across different expense
            categories.
            
            Required inputs:
                total_budget (float):
                    Total amount available for the entire trip.
            
                no_of_people (int):
                    Number of travellers participating in the trip.
            
                no_of_days (int):
                    Total duration of the trip in days.
            
            Optional input:
                currency (str):
                    Currency of the provided budget.
                    Defaults to INR.
            
            Budget allocation:
                - Accommodation: 30%
                - Food: 25%
                - Transportation: 20%
                - Activities and sightseeing: 15%
                - Miscellaneous: 10%
            
            Calculations performed:
                1. Distributes the total budget across the five
                   predefined expense categories.
                2. Calculates the average daily budget.
                3. Calculates the budget available per person.
                4. Calculates the daily budget available per person.
            
            Returns:
                dict: A dictionary containing:
                    - success: Whether the operation succeeded.
                    - total_budget: Original available budget.
                    - no_of_people: Number of travellers.
                    - no_of_days: Trip duration.
                    - currency: Budget currency.
                    - allocation: Category-wise budget distribution.
                    - daily_budget: Average daily budget.
                    - per_person_budget: Budget per traveller.
                    - per_person_per_day: Daily budget per traveller.
            
            Important:
                - All numerical inputs must be positive.
                - The allocation percentages are predefined defaults.
                - This tool distributes an existing budget; it does
                  not estimate actual destination expenses.
                - It does not retrieve hotel, restaurant or transport
                  prices.
                - Use Place Search to research travel-related costs
                  and Calculator to perform additional calculations.
            """

            categories = {
                'accommodation': 0.3,
                'food': 0.25,
                'transportation': 0.20,
                'activities': 0.15,
                'misc': 0.10
            }
            if total_budget<=0 or no_of_days<=0 or no_of_people<=0 :
                return {
                    'success': False,
                    'error': "Budget, no_of_people and no_of_days can't be negative"
                }

            budget_allocation = {
                key: total_budget * value for (key, value) in categories.items()
            }
            return {
                'success': True,
                'total_budget': total_budget,
                'no_of_people': no_of_people,
                'no_of_days': no_of_days,
                'currency': currency,
                'allocation': budget_allocation,
                'daily_budget': total_budget/no_of_days,
                'per_person_budget': total_budget/no_of_people,
                'per_person_per_day': (total_budget/no_of_people)/no_of_days
            }

        return [plan_trip_budget]
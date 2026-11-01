import ast
import operator
from langchain.tools import tool


class CalculatorTool:

    def __init__(self):
        self.calculator_tool_list = self._setup_tools()

    def _setup_tools(self):

        @tool
        def calculate(expression: str) -> dict:
            
            """
            Perform mathematical calculations using a validated
            mathematical expression.
            
            Use this tool whenever numerical calculations are required,
            including travel expense calculations, budget comparisons,
            daily spending limits, percentage calculations and averages.
            
            Supported operations:
            - Addition (+)
            - Subtraction (-)
            - Multiplication (*)
            - Division (/)
            - Modulo (%)
            - Exponentiation (**)
            - Unary positive and negative operators
            - Parentheses for grouping expressions
            
            Input:
                expression (str): A valid mathematical expression.
                The expression must contain numerical values and
                supported mathematical operators.
            
            Examples:
                "5000 + 3000"
                "(1500 * 5) + 2000"
                "50000 / (5 * 2)"
                "5000 * 15 / 100"
            
            Returns:
                dict: A dictionary containing:
                    - success: Whether the calculation succeeded.
                    - expression: The original mathematical expression.
                    - result: The calculated numerical result.
            
                    On failure, returns an error message.
            
            Important:
                - Convert natural-language calculations into valid
                  mathematical expressions before calling this tool.
                - Do not use this tool to retrieve prices, exchange
                  rates or other external information.
                - This tool performs calculations only.
            """


            operators = {
                ast.Add: operator.add,
                ast.Sub: operator.sub,
                ast.Mult: operator.mul,
                ast.Div: operator.truediv,
                ast.Mod: operator.mod,
                ast.Pow: operator.pow,
                ast.USub: operator.neg,
                ast.UAdd: operator.pos
            }

            def evaluate(node):

                # Handle numeric constants
                if isinstance(node, ast.Constant):

                    if type(node.value) not in (int, float):
                        raise ValueError("Only numbers are allowed.")

                    return node.value

                # Handle binary operations
                elif isinstance(node, ast.BinOp):

                    op_type = type(node.op)

                    if op_type not in operators:
                        raise ValueError("Unsupported operator.")

                    left = evaluate(node.left)
                    right = evaluate(node.right)

                    # Prevent excessively large exponents
                    if op_type == ast.Pow and abs(right) > 100:
                        raise ValueError("Exponent too large.")

                    result = operators[op_type](left, right)

                    if type(result) not in (int, float):
                        raise ValueError("Invalid result.")

                    if abs(result) > 1e100:
                        raise ValueError("Result too large.")

                    return result

                # Handle unary operations
                elif isinstance(node, ast.UnaryOp):

                    op_type = type(node.op)

                    if op_type not in operators:
                        raise ValueError("Unsupported operator.")

                    return operators[op_type](
                        evaluate(node.operand)
                    )

                else:
                    raise ValueError("Invalid expression.")

            try:

                # Parse expression into AST
                tree = ast.parse(expression, mode="eval")

                # Evaluate the AST
                result = evaluate(tree.body)

                return {
                    "success": True,
                    "expression": expression,
                    "result": result
                }

            except ZeroDivisionError:
                return {
                    "success": False,
                    "error": "Cannot divide by zero."
                }

            except (ValueError, TypeError, SyntaxError, OverflowError):
                return {
                    "success": False,
                    "error": "Invalid mathematical expression."
                }

        return [calculate]

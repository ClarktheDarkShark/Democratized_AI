from .base import BaseTool

class CalculatorTool(BaseTool):
    name = "calculator"

    def execute(self, args):
        expression = args.get("expression", "0")
        try:
            result = eval(expression, {"__builtins__": {}})
            return {"result": result}
        except Exception as exc:  # pragma: no cover
            return {"error": str(exc)}

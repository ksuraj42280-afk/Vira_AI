import ast
import operator

# Allowed operators
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}


def calculate(expression):
    """
    Safely evaluate a simple math expression.
    Example:
    2+2
    10*5
    20/4
    """

    try:
        node = ast.parse(expression, mode="eval").body

        return str(_evaluate(node))

    except ZeroDivisionError:
        return "Cannot divide by zero."

    except Exception:
        return None


def _evaluate(node):

    if isinstance(node, ast.Constant):
        return node.value

    elif isinstance(node, ast.BinOp):

        left = _evaluate(node.left)
        right = _evaluate(node.right)

        return OPERATORS[type(node.op)](left, right)

    else:
        raise TypeError(node)
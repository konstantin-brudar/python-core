OPERATIONS = "+-*/"
BRACKETS = "()"
POINT = "."


def state_error(char, tokens, token):
    pass


def state_reading_integer(char, tokens, token):
    if char.isdigit():
        token["type"] = "number"
        token["value"] += char
        state = state_reading_integer
    elif char == POINT:
        token["type"] = "number"
        token["value"] += POINT
        state = state_reading_fractional
    else:
        state = state_read_token(char, tokens, token)

    return state


def state_reading_fractional(char, tokens, token):
    if char.isdigit():
        token["type"] = "number"
        token["value"] += char
        state = state_reading_fractional
    elif char == POINT:
        state = state_error
    else:
        state = state_read_token(char, tokens, token)

    return state


def state_read_token(char, tokens, token):
    add_token(token, tokens)
    state = state_begin(char, tokens, token)

    return state


def state_begin(char, tokens, token):
    if char.isdigit():
        token["type"] = "number"
        token["value"] = char
        state = state_reading_integer
    elif char == POINT:
        token["type"] = "number"
        token["value"] = POINT
        state = state_reading_fractional
    elif char in OPERATIONS:
        token["type"] = "operation"
        token["value"] = char
        state = state_read_token
    elif char in BRACKETS:
        token["type"] = "brackets"
        token["value"] = char
        state = state_read_token
    else:
        state = state_error

    return state


def add_token(token, tokens):
    tokens.append(token.copy())
    token = {}


def get_tokens(expression):
    """
    Разбивает выражение на токены (лексемы).

    Args:
        expression (str): Алгебраическое выражение, состоящее из чисел,
            символов математических операций и скобок.

    Returns:
        list[dict] or None: Список токенов, None в случае ошибки.
    """

    state = state_begin
    tokens = []
    token = {}

    for idx, char in enumerate(expression):
        state = state(char, tokens, token)

        if state == state_error:
            print(f"Error at char {idx}: '{char}'")
            return None

    if token:
        add_token(token, tokens)

    return tokens


def priority(operation):
    if operation is None:
        return None

    level = None

    if operation in "()":
        level = 0
    elif operation in "+-":
        level = 1
    elif operation in "*/":
        level = 2

    return level


def get_postfix_tokens(tokens):
    """
    Переводит список токенов из инфиксной в постфиксную форму.

    Args:
        tokens (list[dict] or None): Список токенов в инфиксной форме.

    Returns:
        list[dict] or None: Список токенов в постфиксной форме, None в случае ошибки.
    """

    if tokens is None:
        return None

    postfix_tokens = []
    stack = []

    for token in tokens:
        if token["type"] == "number":
            postfix_tokens.append(token)
        elif token["type"] == "operation":
            while stack and priority(stack[-1]["value"]) >= priority(token["value"]):
                postfix_tokens.append(stack.pop())
            stack.append(token)
        elif token["type"] == "brackets":
            if token["value"] == "(":
                stack.append(token)
            elif token["value"] == ")":
                while stack and stack[-1]["value"] != "(":
                    postfix_tokens.append(stack.pop())
                if stack and stack[-1]["value"] == "(":
                    stack.pop()
                else:
                    print("Error: brackets")
                    return None

    while stack:
        if stack[-1]["value"] == "(":
            print("Error: brackets")
            return None
        postfix_tokens.append(stack.pop())

    return postfix_tokens

def evaluate_postfix_tokens(postfix_tokens):
    """
    Вычисляет результат выражения, заданного списком токенов в постфиксной форме.

    Args:
        postfix_tokens (list[dict] or None): Список токенов в постфиксной форме.

    Returns:
        float: Результат вычисления значения выражения, None в случае ошибки.
    """

    if postfix_tokens is None:
        return None

    stack = []

    for token in postfix_tokens:
        if token["type"] == "number":
            stack.append(float(token["value"]))
        elif token["type"] == "operation":
            if len(stack) < 2:
                print("Error: no data in stack")
                return None
            operation = token["value"]
            y = float(stack.pop())
            x = float(stack.pop())
            if operation == "+":
                stack.append(x + y)
            elif operation == "-":
                stack.append(x - y)
            elif operation == "*":
                stack.append(x * y)
            elif operation == "/":
                stack.append(x / y)
            else:
                print("Error: unknown operation")
                return None
        else:
            print("Error: unexpected token")
            return None

    if len(stack) != 1:
        print("Error: calculation")
        return None

    result = float(stack.pop())

    return result


def calc(raw_expression):
    expression = raw_expression.strip()
    tokens = get_tokens(expression)
    postfix_tokens = get_postfix_tokens(tokens)
    result = evaluate_postfix_tokens(postfix_tokens)

    return result


if __name__ == "__main__":
    expressions = [
        "",
        "1",
        "123456789",
        "+",
        "+-",
        "1+2",
        "123+42-7",
        "(",
        "()(())",
        ")(",
        "1+(20-8)*a+3"
        ".",
        "1.",
        "123.",
        ".1",
        ".123",
        "1.2",
        "123.456",
        "1+123.456*22/333",
        "1.2.3",
        "..",

        "2+3",              # 5
        "1-2*3",            # -5
        "(1-2)*3",          # -3
        "(1+(2/2))-(3-5)",  # 4
        "1/2-1/2"           # 0
    ]

    for expr in expressions:
        print(f"{expr} = {calc(expr)}")

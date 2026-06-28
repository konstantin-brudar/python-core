# python3 -m pip install mypy
# mypy example.py --strict

def format(val: float) -> str:
    return f"{val=:.2f}"

print(format(2.009))

print(format("value"))

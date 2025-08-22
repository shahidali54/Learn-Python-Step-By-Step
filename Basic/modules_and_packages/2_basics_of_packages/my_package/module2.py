# my_package/module2.py

def farewell(name: str) -> str:
    """Return a farewell message."""
    return f"Goodbye, {name}! See you again soon."

def multiply(a: int, b: int) -> int:
    """Return the product of two numbers."""
    return a * b


# Agar directly is file ko run karo to yeh chalega
if __name__ == "__main__":
    print(farewell("Tester"))
    print("5 * 10 =", multiply(5, 10))

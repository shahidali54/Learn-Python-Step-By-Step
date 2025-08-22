# my_package/module1.py

def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}! Welcome to Module 1."

def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b


# Agar directly is file ko run karo to yeh chalega
if __name__ == "__main__":
    print(greet("Tester"))
    print("5 + 10 =", add(5, 10))

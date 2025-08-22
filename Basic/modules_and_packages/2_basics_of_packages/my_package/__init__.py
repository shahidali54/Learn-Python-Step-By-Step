# my_package/__init__.py

# Package ka version define karte hain
__version__ = "1.0.0"

# Specific functions ko direct package se accessible banate hain
from .module1 import greet, add
from .module2 import farewell, multiply

# Jab koi dir(my_package) kare to ye hi functions show honge
__all__ = ["greet", "add", "farewell", "multiply"]

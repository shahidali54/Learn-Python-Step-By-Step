# my_package/sub_package/__init__.py

# Submodules import karwa rahe hain taake direct sub_package se import kiya ja sake
from .sub_module1 import add, greet_from_submodule1
from .sub_module2 import multiply, greet_from_submodule2

__all__ = [
    "add",
    "greet_from_submodule1",
    "multiply",
    "greet_from_submodule2",
]

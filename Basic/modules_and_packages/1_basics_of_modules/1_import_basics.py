# ===========================================
# Basics of importing modules in Python
# - import module
# - from module import name
# - import module as alias
# - function-level import (scoped import)
# - handling ImportError (safe import)
# ===========================================

# --------- 1) Simple import (module-wide namespace) ---------
import math  # Imports the whole math module

print("\n[Simple import: math]")
print("math.sqrt(16) ->", math.sqrt(16))  # Access via module.name
print("math.pi ->", math.pi)              # Using a constant from module


# --------- 2) from module import name (direct names) ---------
from math import sqrt, pi  # Imports selected names directly into current namespace

print("\n[Selective import: from math import sqrt, pi]")
print("sqrt(25) ->", sqrt(25))  # No module prefix needed
print("pi ->", pi)


# --------- 3) import module as alias (short name) ---------
import random as rnd  # Give a short alias for convenience

print("\n[Alias import: import random as rnd]")
print("rnd.randint(1, 5) ->", rnd.randint(1, 5))  # Use alias instead of full module name


# --------- 4) from module import name as alias (alias a symbol) ---------
from random import randint as ri  # Import a single function with an alias

print("\n[Alias a symbol: from random import randint as ri]")
print("ri(10, 20) ->", ri(10, 20))


# --------- 5) Importing multiple useful names from a module ---------
from datetime import datetime, timedelta  # Import multiple names from the same module

print("\n[Multiple names: from datetime import datetime, timedelta]")
now = datetime.now()                       # Current date & time
print("Current time ->", now)
print("Two days later ->", now + timedelta(days=2))


# --------- 6) Importing multiple modules (recommended: one per line for readability) ---------
import os
import sys

print("\n[Multiple modules: os and sys]")
print("Current working directory ->", os.getcwd())  # Get current working directory
print("Python executable path ->", sys.executable)  # Path of the Python interpreter


# --------- 7) Importing inside a function (scoped import) ---------
def get_json_string(py_obj):
    """
    This function imports 'json' locally.
    Benefit: defers import until the function is used (sometimes helpful for performance/startup).
    """
    import json  # Local (function-scope) import
    return json.dumps(py_obj)  # Convert Python object to JSON string

print("\n[Function-level import]")
print("get_json_string({'name': 'Shahid'}) ->", get_json_string({"name": "Shahid"}))


# --------- 8) Handling ImportError safely (when a module may be missing) ---------
def try_import(module_name):
    """
    Tries to import a module by name.
    Returns the module if available, otherwise returns None and prints a message.
    """
    try:
        module = __import__(module_name)  # Built-in dynamic import
        print(f"Successfully imported '{module_name}'")
        return module
    except ImportError:
        print(f"Module '{module_name}' is not installed.")
        return None

print("\n[Safe import with try/except]")
_ = try_import("json")       # Should succeed (built-in)
_ = try_import("not_a_real") # Will fail gracefully


# --------- 9) Checking what a module provides (introspection) ---------
print("\n[Introspection: dir(module)]")
print("Some attributes in math ->", [name for name in dir(math)[:8]], "...")  # Show first few names


# --------- 10) Using __name__ guard (module vs script) ---------
def demo_when_run_directly():
    """
    This function prints a message to show how __name__ works.
    If this file is run directly, __name__ == '__main__'.
    If imported, __name__ == '1_import_basics' (module name).
    """
    print("This code runs only when the file is executed directly (not when imported).")

if __name__ == "__main__":
    print("\n[__name__ check]")
    demo_when_run_directly()

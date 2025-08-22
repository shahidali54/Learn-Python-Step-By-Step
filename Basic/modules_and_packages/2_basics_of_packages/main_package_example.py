"""
main_package_example.py

Goal:
- Demonstrate how to import and use a package and sub-packages.
- We will import from:
    my_package.module1
    my_package.module2
    my_package.sub_package.sub_module1
    my_package.sub_package.sub_module2

NOTE:
- This file expects the following structure to exist next (we will create them step-by-step):
    2_basics_of_packages/
        main_package_example.py   <-- (this file)
        my_package/
            __init__.py
            module1.py
            module2.py
            sub_package/
                __init__.py
                sub_module1.py
                sub_module2.py

How to run:
- Open terminal in: modules_and_packages/2_basics_of_packages
- Run: python main_package_example.py
"""

# --- Safe import with clear error message if package files are not created yet ---
try:
    # Import modules explicitly (does NOT rely on __init__.py exporting names)
    from my_package import module1, module2
    from my_package.sub_package import sub_module1, sub_module2
except ModuleNotFoundError as e:
    print("ImportError:", e)
    print(
        "\nIt looks like the package files are not created yet.\n"
        "Please make sure these files exist:\n"
        "  my_package/__init__.py\n"
        "  my_package/module1.py\n"
        "  my_package/module2.py\n"
        "  my_package/sub_package/__init__.py\n"
        "  my_package/sub_package/sub_module1.py\n"
        "  my_package/sub_package/sub_module2.py\n"
        "\nRun this script again after creating them."
    )
    raise SystemExit(1)

# ----------------------------------------------------------
# 1) Using functions via module imports (explicit module path)
#    This style works even if __init__.py does not export names.
# ----------------------------------------------------------
print("\n=== Using functions via module imports ===")

# Expected functions we will define soon:
# module1.greet(name) -> str
# module1.add(a, b) -> int
print("module1.greet('Shahid'):", module1.greet("Shahid"))   # Calls greet from module1
print("module1.add(5, 3):", module1.add(5, 3))               # Calls add from module1

# module2.farewell(name) -> str
# module2.multiply(a, b) -> int
print("module2.farewell('Iqra'):", module2.farewell("Iqra")) # Calls farewell from module2
print("module2.multiply(4, 6):", module2.multiply(4, 6))     # Calls multiply from module2

# sub_module1.power(base, exp) -> int
# sub_module1.is_even(n) -> bool
print("sub_module1.power(2, 5):", sub_module1.power(2, 5))   # 2 ** 5 = 32
print("sub_module1.is_even(10):", sub_module1.is_even(10))   # True

# sub_module2.reverse_string(s) -> str
# sub_module2.word_count(s) -> int
print("sub_module2.reverse_string('hello'):", sub_module2.reverse_string("hello"))
print("sub_module2.word_count('Python is awesome'):", sub_module2.word_count("Python is awesome"))

# ----------------------------------------------------------
# 2) Alias imports (import module with a shorter name)
#    Helpful when module path is long.
# ----------------------------------------------------------
print("\n=== Using alias imports ===")
import my_package.module1 as m1
import my_package.sub_package.sub_module1 as sm1

print("m1.greet('Ali'):", m1.greet("Ali"))
print("sm1.is_even(7):", sm1.is_even(7))  # False

# ----------------------------------------------------------
# 3) from ... import ... (optional style)
#    This relies on __init__.py to export names via __all__.
#    We'll enable this style after we create proper __init__.py files.
# ----------------------------------------------------------
print("\n=== Optional: from-package imports (will work after __init__.py exports) ===")
try:
    # These will work AFTER we add exports in my_package/__init__.py and sub_package/__init__.py
    from my_package import greet, add, farewell, multiply  # requires __all__ in my_package/__init__.py
    from my_package.sub_package import power, is_even, reverse_string, word_count  # requires __all__ in sub_package/__init__.py

    print("greet('Zain'):", greet("Zain"))
    print("add(10, 20):", add(10, 20))
    print("farewell('Sara'):", farewell("Sara"))
    print("multiply(7, 3):", multiply(7, 3))
    print("power(3, 4):", power(3, 4))
    print("is_even(14):", is_even(14))
    print("reverse_string('world'):", reverse_string("world"))
    print("word_count('I love Python a lot'):", word_count("I love Python a lot"))
except Exception as e:
    # If __init__.py is not exporting yet, we just show a friendly note.
    print("Note: from-package import skipped (will work after __init__.py sets __all__).")
    # Print the reason only for debugging clarity (optional)
    # print("Reason:", e)

print("\n--- Done. Now create the package files step-by-step and re-run this script. ---")

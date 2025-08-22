# Is file me hum OS related modules ka use seekhenge:
# 1. os → file system operations
# 2. os.path → path related operations
# 3. glob → pattern based file searching

import os
import os.path
import glob

print("========== OS Module ==========\n")

# Get current working directory
cwd = os.getcwd()
print("Current Working Directory:", cwd)

# List files in current directory
print("Files in current directory:", os.listdir(cwd))

# Environment variables
print("User environment variable (USERNAME or USER):", os.getenv("USERNAME") or os.getenv("USER"))


print("\n========== OS.PATH Module ==========\n")

# Join paths safely
file_path = os.path.join(cwd, "example.txt")
print("Joined file path:", file_path)

# Check if path exists and type
print("Does path exist?", os.path.exists(cwd))
print("Is directory?", os.path.isdir(cwd))
print("Is file?", os.path.isfile(file_path))

# Split path into dir and filename
print("Split path:", os.path.split(file_path))
print("File extension:", os.path.splitext(file_path))


print("\n========== GLOB Module ==========\n")

# Example 7: Find all Python files in current dir
print("Python files:", glob.glob("*.py"))

# Example 8: Find all text files in any subfolder
print("Text files in subfolders:", glob.glob("**/*.txt", recursive=True))

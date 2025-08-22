# Is file me hum 2 modules seekhenge:
# 1. shutil → file operations
# 2. subprocess → system commands

import shutil
import subprocess

print("========== SHUTIL Module ==========\n")

# Copy a file
shutil.copy("sample.txt", "sample_copy.txt")
print("File copied from sample.txt to sample_copy.txt")

# Move/Rename a file
shutil.move("sample_copy.txt", "moved_sample.txt")
print("File moved/renamed to moved_sample.txt")

# Disk usage
usage = shutil.disk_usage(".")
print(f"Disk Usage - Total: {usage.total // (2**30)} GB, Used: {usage.used // (2**30)} GB, Free: {usage.free // (2**30)} GB")

# Create an archive
shutil.make_archive("backup_folder", "zip", ".")
print("Archive created: backup_folder.zip")

print("\n========== SUBPROCESS Module ==========\n")

# Simple echo command (Windows fix: shell=True)
result = subprocess.run("echo Hello from subprocess!", capture_output=True, text=True, shell=True)
print("Output of echo command:", result.stdout.strip())

# Run Python version
result = subprocess.run(["python", "--version"], capture_output=True, text=True)
print("Python version:", result.stdout.strip() or result.stderr.strip())

# Run 'dir' command (Windows alternative to 'ls')
result = subprocess.run("dir", capture_output=True, text=True, shell=True)
print("\nContents of current directory:\n", result.stdout)

#  Run a command and check return code
completed = subprocess.run("echo Checking return code", shell=True)
print("Return code:", completed.returncode)

# Open notepad (Windows only)
# NOTE: ye notepad khol dega
# subprocess.run("notepad", shell=True)

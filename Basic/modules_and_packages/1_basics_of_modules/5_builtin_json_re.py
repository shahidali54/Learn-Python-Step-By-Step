# Is file me hum 2 built-in modules cover kar rahe hain:
# 1. json → JSON data ke saath kaam karne ke liye
# 2. re (regular expressions) → pattern matching aur text processing ke liye

import json
import re

print("========== JSON Module Examples ==========\n")

# Python dict to JSON string
person = {
    "name": "Shahid",
    "age": 23,
    "skills": ["Python", "Next.js", "Agentic AI"]
}
json_data = json.dumps(person, indent=4)
print("Dict → JSON string:\n", json_data)

# JSON string to Python dict
json_string = '{"name": "Shahid", "age": 23, "city": "Karachi"}'
parsed_dict = json.loads(json_string)
print("\nJSON string → Dict:", parsed_dict)

# Write JSON data to file
with open("person.json", "w") as f:
    json.dump(person, f, indent=4)
print("\nJSON data successfully written to person.json")

# Read JSON data from file
with open("person.json", "r") as f:
    loaded_person = json.load(f)
print("JSON data loaded from file:", loaded_person)


print("\n========== RE (Regular Expressions) ==========\n")

text = "My email is shahid@example.com and I was born in 2001."

# Search for a word
match = re.search(r"born", text)
if match:
    print("Found word 'born' at index:", match.start())

# Find all numbers in text
numbers = re.findall(r"\d+", text)
print("Numbers found in text:", numbers)

# Extract email address
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", text)
print("Email addresses found:", emails)

# Replace text using regex
updated_text = re.sub(r"2001", "1999", text)
print("After replacement:", updated_text)

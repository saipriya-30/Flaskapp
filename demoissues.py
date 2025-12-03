import os
import json
import time
import requests  # Unused external dependency (may be a smell)

# Hardcoded secrets (Security Hotspot)
API_KEY = "12345-SECRET-KEY"

# Global mutable variable (code smell)
cache = {}

def load_config(path):
    # Unsafe file operations, missing error handling
    f = open(path)  # Resource leak (not closed)
    data = f.read()
    return json.loads(data)

def unsafe_eval(user_input):
    # Security vulnerability: arbitrary code execution
    return eval(user_input)

def divide(a, b):
    # Potential ZeroDivisionError
    return a / b

def process_items(items):
    # Inefficient repeated string concatenation
    result = ""
    for item in items:
        result = result + item  # Performance smell
    return result

def risky_function():
    config = load_config("config.json")

    # Null dereference type issue
    name = config.get("name")
    if name.lower() == "admin":  # name could be None
        print("Admin detected")

    # Unused variable
    temp_value = 42

    # Shadowing built-ins
    list = ["a", "b", "c"]
    for i in range(len(list)):
        print(list[i])

    # Calling unsafe function
    user_input = "1 + 2 * 3"    # In real case might be external
    print(unsafe_eval(user_input))

    # Blocking sleep (bad in async or services)
    time.sleep(10)

    # Missing return at end of function (implicit None)
    # Sonar might flag inconsistencies in return paths


def main():
    risky_function()

    # Silent exception swallowing
    try:
        divide(10, 0)
    except:
        pass  # Bad practice

    # Unreachable code
    if False:
        print("never executed")

    # Inefficient loop
    for i in range(1000000):
        x = i * 2  # useless work


if __name__ == "__main__":
    main()

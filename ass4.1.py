filename = "sample.txt"

try:
    print("Reading file content:")
    with open(filename, "r") as file:
        for i, line in enumerate(file, start=1):
            print(f"Line {i}: {line.strip()}")
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")



# Day 10 - Python File Handling

# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, this is Meghana.\n")
    file.write("I am learning Python for AI.\n")

print("Data written to sample.txt")

# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print("\nFile Content:")
    print(content)

# Appending to a file
with open("sample.txt", "a") as file:
    file.write("This is an extra line added later.\n")

# Reading again after append
with open("sample.txt", "r") as file:
    updated_content = file.read()
    print("\nUpdated File Content:")
    print(updated_content)
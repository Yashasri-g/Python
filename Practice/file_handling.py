import os

# Create & write to file
with open("notes.txt", "w") as fh:
    fh.write("Hi\n")
    fh.write("Created a file notes.\n")
    fh.write("Added 3 lines into it\n")

# Read file
with open("notes.txt", "r") as fh:
    data = fh.read()
    print(data)

# Append to file
with open("notes.txt", "a") as fh:
    fh.write("Python File Handling\n")

# Check if file exists
if os.path.exists("notes.txt"):
    print("File exists")
else:
    print("File doesn't exist")

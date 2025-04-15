# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.

input_file = "input.txt"
output_file = "output.txt"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        # Write the original line
        outfile.write(line)
    # Add extra lines after writing the original content
    outfile.write("\nThis is a new line added to the output_file\n")
    outfile.write("Another added line.")

# Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
filename  = input("Enter the filename you want to read: ")
try:
    with open(filename, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"The file '{filename}' was not found.")

except PermissionError:
    print(f"You do not have permission to read the file '{filename}'.")

except Exception as e:
    print(f"An error occurred: {e}")
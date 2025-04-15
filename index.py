input_file = "input.txt"
output_file = "output.txt"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        # Write the original line
        outfile.write(line)
    # Add extra lines after writing the original content
    outfile.write("\nThis is a new line added to the output_file\n")
    outfile.write("Another added line.")

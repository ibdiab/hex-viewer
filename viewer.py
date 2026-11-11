#!/usr/bin/env python3

# Author: Ibrahim Diab
# Description: A Hex viewer allowing anyone to read a file in binary and display its bytes in hexadecimal. Then
# the result is written to a file for debugging and analyzing.

# Asks user for a file they want to view in hexadecimal
file = input("Enter the files name you want in hexadecimal (INCLUDE FILE EXTENSION): ")
print()

# Sends the resulting hex code to a file for debugging and analysis
import os
base = os.path.basename(file)
output = base + ".hex.txt"  # File extension used for viewing the results
counter = 1

# Function for classifying a byte into a category name. Later used to 
# look up its color
def classify(byte):
    if byte == 0:
        return "null"
    elif byte in (9,10,13):
        return "whitespace"
    elif 32 <= byte <= 126:
        return "printable"
    elif byte == 255:
        return "ff"
    elif byte >= 128:
        return "high"
    else: 
        return "control"
print()

# If the same file is scanned multiple times, appends a unique number so nothing gets lost
while os.path.exists(output):
    output = f"{base}.hex{counter}.txt"  # create new filename
    counter += 1  # increment counter for next check

# Prints a header for the code
bytes_per_line = 16
offset_w = 8
hex_w = bytes_per_line * 3
ascii_w = bytes_per_line
sep = "   "

header = (
        "Offset".ljust(offset_w) +
        sep +
        "Hexadecimal".center(hex_w) +
        sep +
        "ASCII".rjust(ascii_w)
)

separator = "-" * len(header)

print(header)
print(separator)
lines_printed = 0 

# Reads the file 16 bytes at a time
offset = 0
with open(file, "rb") as f, open(output, "w") as out:

    # Declares colors used to color-code common hex values
    COLORS = {
        "null": "\033[37m",
        "printable": "\033[32m",
        "whitespace": "\033[33m",
        "control": "\033[35m",
        "high": "\033[34m",
        "ff": "\033[31m"
    }
    RESET = "\033[0m"

    out.write(header + "\n")
    out.write(separator+ "\n")

    while True:
        chunk = f.read(16)
        if not chunk:
            break

        hex_line = ""
        ascii_line = ""
        plain_hex = ""
        plain_ascii = ""
        offset_str = f"{offset:08x}"

        # Converts bytes to hex and ASCII
        for byte in chunk:
            category = classify(byte)
            color = COLORS[category]
            hex_value = f"{byte:02X}"
            hex_line += color + hex_value + RESET + " "
            plain_hex += hex_value + " "

            if category == "printable":
                char = chr(byte)
            else:
                char = "."
        
            ascii_line += color + char + RESET
            plain_ascii += char

        # Pads the hex section if the last line is too short
        if len(chunk) < bytes_per_line:
            missing_bytes = bytes_per_line - len(chunk)
            plain_hex += "   " * missing_bytes
            hex_line += "   " * missing_bytes

        # Prints the result and writes it to a file
        result = (offset_str + " | " + hex_line + " | " + ascii_line)
        plain_result = (offset_str + " | " + plain_hex + " | " + plain_ascii)
    
        print(result)
        out.write(plain_result + "\n")

        # Asks user if they want to continue printing every 32 lines, if not then it ends the program to prevent crashing
        lines_printed += 1

        if lines_printed >= 32:
            print()
            choice = input("Press Enter to continue printing, or 'Q' to quit: ")
            print()
            if choice.lower() == "q":
                print("Results written to " + output)
                break
            lines_printed = 0

        # Moves offset forward
        offset += len(chunk)

# Author: Ibrahim Diab
# Description: A Hex viewer allowing anyone to read a file in binary and display its bytes in hexadecimal. Then
# the result is written to a file for debugging and analyzing.

# Asks user for a file they want to view in hexadecimal
file = input("Enter the files name you want in hexadecimal (INCLUDE FILE EXTENSION): ")
print()

# Sends the resulting hex code to a file for debugging and analysis
import os
base = os.path.basename(file)
output = base + ".hex.txt"  # first attempt
counter = 1

# If the same file is scanned multiple times, appends a unique number so nothing gets lost
while os.path.exists(output):
    output = f"{base}.hex{counter}.txt"  # create new filename
    counter += 1  # increment counter for next check

# Prints a header for the code
bytes_per_line = 16
offset_w = 8
hex_w = bytes_per_line * 3
ascii_w = bytes_per_line
sep = "  "

header = (
        "Offset".ljust(offset_w) +
        sep +
        "Hexadecimal".center(hex_w) +
        sep +
        "ASCII".rjust(ascii_w)
)

separator = "-" * (offset_w + len(sep) + hex_w + len(sep) + ascii_w)

print(header)
print(separator)

lines_printed = 0

# Reads the file 16 bytes at a time
offset = 0
with open(file, "rb") as f, open(output, "w") as out:

    out.write(header + "\n")
    out.write(separator+ "\n")

    while True:
        chunk = f.read(16)
        if not chunk:
            break

        hex_line = ""
        ascii_line = ""
        offset_str = f"{offset:08x}"

        # Converts bytes to hex and ASCII
        for byte in chunk:
            hex_value = f"{byte:02X}"
            hex_line += hex_value + " "

            if 32 <= byte <= 126:
                ascii_line += chr(byte)
            else:
                ascii_line += "."

        # Pads the hex section if the last line is too short
        if len(chunk) < bytes_per_line:
            missing_bytes = bytes_per_line - len(chunk)
            hex_line += "   " * missing_bytes

        # Prints the result and writes it to a file
        result = (offset_str + " | " + hex_line + " | " + ascii_line)
        print(result)
        out.write(result + "\n")

        # Asks user if they want to continue printing every 32 lines, if not then it ends the program to prevent crashing
        lines_printed += 1

        if lines_printed >= 32:
            print()
            choice = input("Press Enter to continue printing, or 'Q' to quit: ")
            print()
            if choice.lower() == "q":
                break
            lines_printed = 0

        # Moves offset forward
        offset += len(chunk)
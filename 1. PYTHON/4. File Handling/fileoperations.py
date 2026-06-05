## This script demonstrates basic file handling operations in Python:

#---------Text file operations: write, read, and append.

# -------- WRITE MODE (w) --------
# Creates file or overwrites existing content
with open("file/sample.txt", "w") as file:
    file.write("Hello World\n")
    file.write("This is write mode.\n")

print("Write operation completed.\n")


# -------- READ MODE (r) --------
# Reads content from file
with open("file/sample.txt", "r") as file:
    content = file.read()
    print("Read operation output:")
    print(content)


# -------- APPEND MODE (a) --------
# Adds content at the end of file
with open("file/sample.txt", "a") as file:
    file.write("This line is appended.\n")

print("\nAppend operation completed.\n")


# -------- READ AGAIN TO VERIFY --------
with open("file/sample.txt", "r") as file:
    print("Final file content:")
    print(file.read())
    
#---------Binary file operations: write and read.

# -------- WRITE BINARY (wb) --------
# Writes bytes (overwrites or creates file)
with open("file/sample.bin", "wb") as file:
    data = b"Hello Binary World\n"   # bytes (prefix b is important)
    file.write(data)

print("Binary write completed.\n")


# -------- READ BINARY (rb) --------
# Reads raw bytes from file
with open("file/sample.bin", "rb") as file:
    content = file.read()
    print("Binary read output (raw bytes):")
    print(content)

    print("\nDecoded output:")
    print(content.decode())   # convert bytes → string


# -------- APPEND BINARY (ab) --------
# Adds bytes at end of file
with open("file/sample.bin", "ab") as file:
    file.write(b"Appended Binary Line\n")

print("\nBinary append completed.\n")


# -------- READ AGAIN TO VERIFY --------
with open("file/sample.bin", "rb") as file:
    content = file.read()
    print("Final binary content (decoded):")
    print(content.decode())
    
#----------CSV file operations: write and read.

import csv

# -------- WRITE CSV (w) --------
# Creates/overwrites CSV file
with open("file/data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    # Writing header
    writer.writerow(["Name", "Age", "Marks"])
    
    # Writing rows
    writer.writerow(["Alice", 20, 85])
    writer.writerow(["Bob", 21, 90])
    writer.writerow(["Charlie", 19, 78])

print("CSV write completed.\n")


# -------- READ CSV (r) --------
with open("file/data.csv", "r") as file:
    reader = csv.reader(file)
    
    print("CSV read output:")
    for row in reader:
        print(row)


# -------- APPEND CSV (a) --------
with open("file/data.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["David", 22, 88])

print("\nCSV append completed.\n")


# -------- READ AGAIN TO VERIFY --------
with open("file/data.csv", "r") as file:
    reader = csv.reader(file)
    
    print("Final CSV content:")
    for row in reader:
        print(row)
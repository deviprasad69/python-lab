import os
source_file = "source.txt"
copy_file = "copy.txt"
content = input("Enter text to write into the file: ")
with open(source_file, "w", encoding="utf-8") as file:
    file.write(content + "\n")
additional = input("Enter text to append: ")
with open(source_file, "a", encoding="utf-8") as file:
    file.write(additional + "\n")
with open(source_file, "r", encoding="utf-8") as file:
    data = file.read()
print("\nComplete file contents:\n" + data)
print("Characters:", len(data))
print("Words :", len(data.split()))
print("Lines :", len(data.splitlines()))
with open(source_file, "r", encoding="utf-8") as file:
    print("\nUsing read():")
    print(file.read())
with open(source_file, "r", encoding="utf-8") as file:
    print("Using readline():", file.readline().rstrip())
    
with open(source_file, "r", encoding="utf-8") as file:
    lines = file.readlines()
    print("Using readlines():", lines)
    print("Lines with line numbers:")
    for number, line in enumerate(lines, start=1):
        print(f"{number}: {line.rstrip()}")
with open(source_file, "r", encoding="utf-8") as src:
    source_data = src.read()
with open(copy_file, "w", encoding="utf-8") as dst:
    dst.write(source_data)
with open(copy_file, "r", encoding="utf-8") as file:
    copied_data = file.read()
print("\nCopy verified:", source_data == copied_data)
print("Source contents:\n", source_data, sep="")
print("Copied contents:\n", copied_data, sep="")
print("Source file size:", os.path.getsize(source_file), "bytes")
print("Copy file size :", os.path.getsize(copy_file), "bytes")
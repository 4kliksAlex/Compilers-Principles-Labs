keywords = ["const", "var", "begin", "end", "read", "write"]

with open("input.txt", "r") as file:
    lines = file.readlines()

identifiers = {}

for line in lines:
    words = ''.join(ch if ch.isalnum() else ' ' for ch in line.lower()).split()
    for word in words:
        if word not in keywords and not word.isdigit():
            identifiers[word] = identifiers.get(word, 0) + 1

with open("output.txt", "w") as file:
    for identifier, count in identifiers.items():
        file.write(f"({identifier}: {count})\n")
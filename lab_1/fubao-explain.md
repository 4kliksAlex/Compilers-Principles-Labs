List of PL/0 keywords

```python
keywords = ["const", "var", "begin", "end", "read", "write"]
```

Open and read the input file

```python
with open("input.txt", "r") as file:
    lines = file.readlines()
```

Initialize an empty dictionary to store the identifiers and their counts

```python
identifiers = {}
```

Iterate over the lines

```python
for line in lines:
    # Convert the line to lowercase and split it into words by non-alphanumeric characters
    words = ''.join(ch if ch.isalnum() else ' ' for ch in line.lower()).split()
    # Iterate over the words
    for word in words:
        # If a word is an identifier (not a keyword or a number)
        if word not in keywords and not word.isdigit():
            # Increment its count in the dictionary
            identifiers[word] = identifiers.get(word, 0) + 1
```

Write the results to the output file in the order of appearance

```python
with open("output.txt", "w") as file:
    for identifier, count in identifiers.items():
        file.write(f"({identifier}: {count})\n")
```

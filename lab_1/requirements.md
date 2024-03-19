# Content

The input file is the PL/0 language source program, and the output file is the number of occurrences of all identifiers in the source program.

# Requirements

- Do not use regex.

- The recognition program reads the PL/0 language source program (text file), and the recognition results are also saved in text files.

- Output the results in the order in which the identifiers appear.

- The identifier in the source program are not case-sensitive, that is: "a1" and "A1" are the same identifier.

## Input and output examples

**Input: (text file)**
```
Const num=100,cst;
Var a1,b2=3;
Begin
    Read(A1);
    b2:=a1+num;
    write(A1,B2);
End.
```

**Output: (text file)**
```
(num: 2)
(cst: 1)
(a1: 4)
(b2: 3)
```
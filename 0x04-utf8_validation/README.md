# 0x04. UTF-8 Validation

## Specialization: Short Specializations  
**Average:** 63.91%  
**Project Weight:** 1  

**Project Duration:**  
- Start: Oct 28, 2024, 6:00 AM  
- End: Nov 1, 2024, 6:00 AM  

An auto review will be launched at the deadline.

---

## In a Nutshell…
### Auto QA Review: 0.0/14 mandatory  
- **Altogether:** 0.0%  
- **Mandatory:** 0.0%  
- **Optional:** No optional tasks  

---

## Project Overview
For the **“0x04. UTF-8 Validation”** project, you will apply your knowledge in:
- Bitwise operations
- Understanding the UTF-8 encoding scheme
- Python programming skills  

Your goal is to validate whether a given dataset represents a valid UTF-8 encoding.

---

## Concepts Needed
### 1. Bitwise Operations in Python
- Understand how to manipulate bits in Python using:
  - `AND (&)`
  - `OR (|)`
  - `XOR (^)`
  - `NOT (~)`
  - Bit shifts (`<<`, `>>`)
- **Resources**:  
  [Python Bitwise Operators](https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types)

### 2. UTF-8 Encoding Scheme
- Learn about the UTF-8 encoding rules:
  - Characters can be encoded in 1 to 4 bytes.
  - Rules for valid patterns.
- **Resources**:  
  - [UTF-8 Wikipedia](https://en.wikipedia.org/wiki/UTF-8)  
  - [Characters, Symbols, and the Unicode Miracle](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)  

### 3. Data Representation
- Represent and manipulate data at the byte level.
- Handle the **least significant bits (LSB)** of integers.

### 4. List Manipulation in Python
- Iterate through lists, access elements, and use list comprehensions.
- **Resource**: [Python Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

### 5. Boolean Logic
- Apply logical operations to make decisions within the program.

---

## Requirements
- **Allowed Editors:** `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using `python3` (version 3.4.3).
- Files must end with a new line.
- The first line of all files must be exactly: `#!/usr/bin/python3`
- A `README.md` file is mandatory at the root of the project folder.
- Code must follow the **PEP 8 style** (version 1.7.x).
- All files must be executable.

---

## Task
### 0. UTF-8 Validation (Mandatory)
Write a method that determines if a given dataset represents a valid UTF-8 encoding.

**Prototype:**  
```python
def validUTF8(data):
    """
    Determines if a given dataset represents a valid UTF-8 encoding.
    :param data: List of integers representing bytes of data.
    :return: True if data is valid UTF-8 encoding, False otherwise.
    """

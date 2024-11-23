# 0x07. Rotate 2D Matrix

## **Project Overview**
For the **“0. Rotate 2D Matrix”** project, your task is to implement an **in-place algorithm** to rotate an `n x n` 2D matrix by **90 degrees clockwise**. This challenge involves understanding matrix manipulation and in-place operations in Python.

---

### **Concepts Needed**
#### **Matrix Representation in Python**
- Understanding how 2D matrices are represented using **lists of lists**.
- Accessing and modifying elements in a 2D matrix.

#### **In-place Operations**
- Performing operations on data **without creating a copy** of the data structure.
- Minimizing space complexity by modifying the matrix in place.

#### **Matrix Transposition**
- Understanding the concept of transposing a matrix (**swapping rows and columns**).
- Implementing matrix transposition as a step in the rotation process.

#### **Reversing Rows in a Matrix**
- Manipulating rows of a matrix by **reversing their order** as part of the rotation process.

#### **Nested Loops**
- Using nested loops to iterate through 2D data structures like matrices.
- Modifying elements within nested loops to achieve the desired rotation.

---

### **Resources**
#### **Python Official Documentation**
- [Data Structures (list comprehensions)](https://docs.python.org/3/tutorial/datastructures.html)
- [More on Lists](https://docs.python.org/3/library/stdtypes.html#lists)

#### **GeeksforGeeks Articles**
- [In-place Rotate Square Matrix by 90 Degrees](https://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
- [Transpose a Matrix in a Single Line in Python](https://www.geeksforgeeks.org/python-transpose-matrix/)

#### **TutorialsPoint**
- [Python Lists](https://www.tutorialspoint.com/python/python_lists.htm)

---

### **Requirements**
#### **General**
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using `python3` (version 3.8.10).
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/python3`.
- A `README.md` file at the root of the folder is mandatory.
- Code should follow the **pycodestyle** style (version 2.8.0).
- You are **not allowed to import any module**.
- All modules and functions must be documented.
- All files must be executable.

---

### **Tasks**
#### **0. Rotate 2D Matrix** (Mandatory)  
**Score:** 0.0% (Checks completed: 0.0%)  

##### **Task Description**  
Given an `n x n` 2D matrix, rotate it **90 degrees clockwise**.

- **Prototype:**  
  ```python
  def rotate_2d_matrix(matrix):
  ```
- **Requirements:**  
  - Do not return anything. The matrix must be edited **in-place**.
  - Assume the matrix has **2 dimensions** and will **not be empty**.

##### **Example**
```python
# File: main_0.py
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
```

**Output:**
```
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

---

### **Repository Information**
- **GitHub Repository:** `alx-interview`
- **Directory:** `0x07-rotate_2d_matrix`
- **File:** `0-rotate_2d_matrix.py`

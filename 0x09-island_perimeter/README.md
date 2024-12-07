# **0x09. Island Perimeter**

## **Description**
This project focuses on solving the "Island Perimeter" problem using Python. The task involves calculating the perimeter of a single island in a grid representation where:
- `0` represents water.
- `1` represents land.

The grid is a 2D list of integers, and the goal is to compute the total perimeter of the land cells using logical operations and efficient traversal techniques.

---

## **Learning Objectives**
This project reinforces knowledge in:
1. **2D Arrays (Matrices):**
   - Accessing and iterating over elements in a 2D grid.
   - Navigating adjacent cells (up, down, left, right).

2. **Conditional Logic:**
   - Identifying land cells and determining if edges contribute to the perimeter.

3. **Algorithm Development:**
   - Breaking the problem into smaller tasks:
     - Recognizing land cells.
     - Counting perimeter edges using logical conditions.

4. **Python Programming Skills:**
   - Writing functions and recursive logic.
   - Applying PEP 8 coding standards.
   - Handling edge cases.

---

## **Requirements**
- **Language:** Python 3.x (compiled on Ubuntu 20.04 LTS using Python 3.4.3).
- **Style:** Follow PEP 8 (version 1.7).
- **Constraints:**
  - No external modules are allowed.
  - Grid dimensions (width and height) do not exceed 100.
  - The grid is surrounded by water.
  - Only one island exists, and there are no lakes (water fully enclosed by land).

---

## **Function Prototype**
```python
def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.
    
    Args:
        grid (List[List[int]]): A 2D list where 0 represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
```

---

## **Usage**
### Example Input and Output
#### Input Grid:
```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
```

#### Execution:
```bash
$ ./0-main.py
12
```

---

## **Algorithm Explanation**
The function employs **Depth First Search (DFS)** to calculate the perimeter:
1. **Iterate through the grid:** Find the first land cell (`1`).
2. **Recursive DFS:** Explore all adjacent cells to determine their contribution to the perimeter:
   - If an adjacent cell is water or out of bounds, it adds `1` to the perimeter.
   - If an adjacent cell is land and not visited, recurse into that cell.
3. **Base Cases:** Handle water, boundaries, and previously visited cells.
4. **Summation:** Combine results from all recursive calls to compute the total perimeter.

---

## **Files**
- `0-island_perimeter.py`: Contains the implementation of the `island_perimeter` function.
- `0-main.py`: Sample test file to verify the functionality of the `island_perimeter` function.

---

## **Environment**
- **OS:** Ubuntu 20.04 LTS
- **Editor:** vi, vim, emacs
- **Python Version:** Python 3.4.3
- **Style Guide:** PEP 8 (version 1.7)

---

## **How to Test**
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/alx-interview.git
   ```
2. Navigate to the project directory:
   ```bash
   cd alx-interview/0x09-island_perimeter
   ```
3. Run the test file:
   ```bash
   ./0-main.py
   ```

---

## **References**
- [Python Official Documentation](https://docs.python.org/3/)
- [PEP 8 Style Guide](https://pep8.org/)
- [GeeksforGeeks: Python Multi-dimensional Arrays](https://www.geeksforgeeks.org/python-using-2d-arrays-lists/)

#!/usr/bin/python3

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
        grid (List[List[int]]): A 2D list where 0 represents water
        and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    visit = set()

    def dfs(i, j):
        """
        Perform a Depth First Search (DFS) to calculate
        the contribution to the perimeter for the
        current cell and its neighbors.

        If the cell is out of bounds or represents water,
        it adds 1 to the perimeter.
        If the cell has been visited already, it adds 0.
        Otherwise, it recursively checks the neighboring cells (up, down, left,
        right).

        Args:
            i (int): The row index of the current cell.
            j (int): The column index of the current cell.

        Returns:
            int: The perimeter contribution for the current cell
            and its neighbors.
        """
        if (
            i >= len(grid) or j >= len(grid[0]) or
            i < 0 or j < 0 or grid[i][j] == 0
        ):
            return 1

        if (i, j) in visit:
            return 0

        visit.add((i, j))
        perim = dfs(i, j + 1)
        perim += dfs(i + 1, j)
        perim += dfs(i, j - 1)
        perim += dfs(i - 1, j)
        return perim

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                return dfs(i, j)

    return 0

from puzzle import Puzzle


class MNPuzzle(Puzzle):
    """
    An nxm puzzle, like the 15-puzzle, which may be solved, unsolved,
    or even unsolvable.
    """

    def __init__(self, from_grid, to_grid):
        """
        MNPuzzle in state from_grid, working towards
        state to_grid

        @param MNPuzzle self: this MNPuzzle
        @param tuple[tuple[str]] from_grid: current configuration
        @param tuple[tuple[str]] to_grid: solution configuration
        @rtype: None
        """
        # represent grid symbols with letters or numerals
        # represent the empty space with a "*"
        assert len(from_grid) > 0
        assert all([len(r) == len(from_grid[0]) for r in from_grid])
        assert all([len(r) == len(to_grid[0]) for r in to_grid])
        self.n, self.m = len(from_grid), len(from_grid[0])
        self.from_grid, self.to_grid = from_grid, to_grid

    def __eq__(self, other):
        """
        Return whether MNPuzzle self is equivalent to other MNPuzzle.

        @type self: MNPuzzle
        @type other: MNPuzzle
        @rtype: bool

        >>> target_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> start_grid = (("*", "2", "3"), ("1", "4", "5"))
        >>> start_grid1 = (("3", "2", "*"), ("1", "4", "5"))
        >>> mn = MNPuzzle(start_grid, target_grid)
        >>> mn1 = MNPuzzle(start_grid, target_grid)
        >>> mn2 = MNPuzzle(start_grid1, target_grid)
        >>> mn == mn1
        True
        >>> mn == mn2
        False
        """
        return (self.n == other.n and self.m == other.m and
                self.from_grid == other.from_grid and
                self.to_grid == other.to_grid)

    def __str__(self):
        """
        Return a human-readable string representation of MNPuzzle self.

        @type self: MNPuzzle
        @rtype: str

        >>> target_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> start_grid = (("3", "*", "2"), ("5", "4", "1"))
        >>> p = MNPuzzle(start_grid, target_grid)
        >>> print(p)
        3*2
        541
        """
        list_ = []
        for row in self.from_grid:
            for ch in row:
                list_.append(ch)
            list_.append('\n')
        list_ = list_[:-1]
        return ''.join(list_)

    def extensions(self):
        """
        Return all possible extensions of current configuration by swapping one
        symbol to the left, right, above, or below "*" with "*".

        @type self: MNPuzzle
        @rtype: list[MNPuzzle]

        >>> target_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> start_grid = (("*", "2", "3"), ("1", "4", "5"))
        >>> start_grid1 = (("2", "*", "3"), ("1", "4", "5"))
        >>> start_grid2 = (("1", "2", "3"), ("*", "4", "5"))
        >>> mn = MNPuzzle(start_grid, target_grid)
        >>> mn1 = MNPuzzle(start_grid1, target_grid)
        >>> mn2 = MNPuzzle(start_grid2, target_grid)
        >>> a = mn.extensions()
        >>> a[0] == mn1 or a[0] == mn2
        True
        """
        # helper function
        def to_tuple(list_):
            """
            Convert list into tuple, including all internal lists.

            @type list_: list | list[list]
            @rtype: tuple | tuple(tuple)
            """
            i = 0
            while i < len(list_):
                list_[i] = tuple(list_[i])
                i += 1
            return list_

        # find position of "*" in the grid
        row = 0
        column = 0
        for line in self.from_grid:
            if "*" in line:
                row = self.from_grid.index(line)
                column = self.from_grid[row].index("*")

        extensions = []
        # move "*" to the right
        if column < len(self.from_grid[row]) - 1:
            grid_list = [list(x) for x in self.from_grid]
            grid_list[row][column] = grid_list[row][column + 1]
            grid_list[row][column + 1] = "*"
            to_tuple(grid_list)
            extensions.append(MNPuzzle(tuple(grid_list), self.to_grid))

        # move "*" to the left
        if 1 < column < len(self.from_grid[row]):
            grid_list = [list(x) for x in self.from_grid]
            grid_list[row][column] = grid_list[row][column - 1]
            grid_list[row][column - 1] = "*"
            to_tuple(grid_list)
            extensions.append(MNPuzzle(tuple(grid_list), self.to_grid))

        # move "*" down
        if row < len(self.from_grid) - 1:
            grid_list = [list(x) for x in self.from_grid]
            grid_list[row][column] = grid_list[row + 1][column]
            grid_list[row + 1][column] = "*"
            to_tuple(grid_list)
            extensions.append(MNPuzzle(tuple(grid_list), self.to_grid))

        # move "*" up
        if 1 < row < len(self.from_grid):
            grid_list = [list(x) for x in self.from_grid]
            grid_list[row][column] = grid_list[row - 1][column]
            grid_list[row - 1][column] = "*"
            to_tuple(grid_list)
            extensions.append(MNPuzzle(tuple(grid_list), self.to_grid))

        return extensions

    def is_solved(self):
        """
        Return whether from_grid is the same as to_grid.

        @type self: MNPuzzle
        @rtype: bool

        >>> target_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> start_grid = (("*", "2", "3"), ("1", "4", "5"))
        >>> start_grid1 = (("1", "2", "3"), ("4", "5", "*"))
        >>> mn = MNPuzzle(start_grid, target_grid)
        >>> mn1 = MNPuzzle(start_grid1, target_grid)
        >>> mn.is_solved()
        False
        >>> mn1.is_solved()
        True
        """
        return self.from_grid == self.to_grid

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    target_grid = (("1", "2", "3"), ("4", "5", "*"))
    start_grid = (("*", "2", "3"), ("1", "4", "5"))
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    start = time()
    solution = breadth_first_solve(MNPuzzle(start_grid, target_grid))
    end = time()
    print("BFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))
    start = time()
    solution = depth_first_solve((MNPuzzle(start_grid, target_grid)))
    end = time()
    print("DFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))

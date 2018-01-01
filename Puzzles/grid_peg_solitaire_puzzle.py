from puzzle import Puzzle


class GridPegSolitairePuzzle(Puzzle):
    """
    Snapshot of peg solitaire on a rectangular grid. May be solved,
    unsolved, or even unsolvable.
    """

    def __init__(self, marker, marker_set):
        """
        Create a new GridPegSolitairePuzzle self with
        marker indicating pegs, spaces, and unused
        and marker_set indicating allowed markers.

        @type marker: list[list[str]]
        @type marker_set: set[str]
                          "#" for unused, "*" for peg, "." for empty
        """
        assert isinstance(marker, list)
        assert len(marker) > 0
        assert all([len(x) == len(marker[0]) for x in marker[1:]])
        assert all([all(x in marker_set for x in row) for row in marker])
        assert all([x == "*" or x == "." or x == "#" for x in marker_set])
        self._marker, self._marker_set = marker, marker_set

    def __eq__(self, other):
        """
        Return whether GridPegSolitairePuzzle self is equivalent to other
        GridPegSolitairePuzzle.

        @type self: GridPegSolitairePuzzle
        @type other: GridPegSolitairePuzzle | Any
        @rtype: bool

        >>> grid = [['#','*','*','*','#']]
        >>> grid.append(['#','*','.','*','#'])
        >>> grid.append(['#','*','*','*','#'])
        >>> marker_set = {'#','.','*'}
        >>> s = GridPegSolitairePuzzle(grid, marker_set)
        >>> grid1 = [['#','*','*','*','#']]
        >>> grid1.append(['#','*','.','*','#'])
        >>> grid1.append(['#','*','*','*','#'])
        >>> s1 = GridPegSolitairePuzzle(grid1, marker_set)
        >>> grid2 = [['#','*','*','*','#']]
        >>> grid2.append(['*','*','.','*','*'])
        >>> grid2.append(['#','*','*','*','#'])
        >>> s2 = GridPegSolitairePuzzle(grid2, marker_set)
        >>> s == s1
        True
        >>> s == s2
        False
        """
        return (type(self) == type(other) and
                self._marker == other._marker and
                self._marker_set == other._marker_set)

    def __str__(self):
        """
        Return a human-readable string representation of
        GridPegSolitairePuzzle self.

        @type self: GridPegSolitairePuzzle
        @rtype: str

        >>> grid = [['#','*','*','*','#']]
        >>> grid.append(['#','*','*','*','#'])
        >>> grid.append(['#','*','.','*','#'])
        >>> grid.append(['#','*','*','*','#'])
        >>> grid.append(['#','*','*','*','#'])
        >>> marker_set = {'#','.','*'}
        >>> s = GridPegSolitairePuzzle(grid, marker_set)
        >>> print(s)
        #***#
        #***#
        #*.*#
        #***#
        #***#
        """
        list_ = []
        for ch in self._marker:
            list_.append(''.join(ch))
        return '\n'.join(list_)

    def extensions(self):
        """
        Return all possible extensions that can be reached by making a single
        jump from current configuration.

        @param self: GridPegSolitairePuzzle
        @rtype: list[GridPegSolitairePuzzle]

        >>> marker_set = {'#','.','*'}
        >>> grid = [['#','*','*','*','#']]
        >>> grid.append(['#','*','*','*','#'])
        >>> grid.append(['#','*','.','*','#'])
        >>> s = GridPegSolitairePuzzle(grid, marker_set)
        >>> grid1 = [['#','*','.','*','#']]
        >>> grid1.append(['#','*','.','*','#'])
        >>> grid1.append(['#','*','*','*','#'])
        >>> b = GridPegSolitairePuzzle(grid1, marker_set)
        >>> a = s.extensions()[0]
        >>> a == b
        True
        """
        list_extensions = []
        # checking every line of the grid
        for line in self._marker:
            index = self._marker.index(line)

            # making moves horizontally from the left to the righy
            i = 0
            while i < len(line) - 2:
                if line[i] == "*" and line[i+1] == "*" and line[i+2] == ".":
                    # copy for not to change original grid
                    marker_copy = self._marker.copy()
                    marker_copy[index][i] = "."
                    marker_copy[index][i] = "."
                    marker_copy[index][i] = "*"
                    list_extensions.append(GridPegSolitairePuzzle
                                           (marker_copy, self._marker_set))
                i += 1

            # making moves horizontally from the right to the left
            j = 0
            while j < len(line) - 2:
                if line[i] == "." and line[i+1] == "*" and line[i+2] == "*":
                    marker_copy = self._marker.copy()
                    index = self._marker.index(line)
                    marker_copy[index][i] = "*"
                    marker_copy[index][i] = "."
                    marker_copy[index][i] = "."
                    list_extensions.append(GridPegSolitairePuzzle(
                            marker_copy, self._marker_set))
                j += 1

            # making moves vertically from the down to the up
            k = 0
            while k < len(line):
                if index < len(self._marker) - 2:
                    if (line[k] == '.' and self._marker[index + 1][k] ==
                            '*' and self._marker[index + 2][k] == '*'):
                        marker_copy = self._marker.copy()
                        marker_copy[index][k] = '*'
                        marker_copy[index + 1][k] = '.'
                        marker_copy[index + 2][k] = '.'
                        list_extensions.append(GridPegSolitairePuzzle(
                                marker_copy, self._marker_set))
                k += 1

            # making moves vertically from the up to the down
            l = 0
            while l < len(line):
                if index < len(self._marker) - 2:
                    if (line[l] == '*' and self._marker[index + 1][l] ==
                            '*' and self._marker[index + 2][l] == '.'):
                        marker_copy = self._marker.copy()
                        marker_copy[index][l] = '.'
                        marker_copy[index + 1][l] = '.'
                        marker_copy[index + 2][l] = '*'
                        list_extensions.append(GridPegSolitairePuzzle(
                                marker_copy, self._marker_set))
                l += 1

        return list_extensions

    def is_solved(self):
        """
        Return whether puzzle is solved, i.e there is only one "*" left/

        @type self: GridPegSolitairePuzzle
        @rtype: bool

        >>> grid = [['#','.','.','.','#']]
        >>> grid.append(['#','.','.','.','#'])
        >>> grid.append(['#','*','*','*','#'])
        >>> marker_set = {'#','.','*'}
        >>> s = GridPegSolitairePuzzle(grid, marker_set)
        >>> s.is_solved()
        False
        >>> grid1 = [['#','.','.','.','#']]
        >>> grid1.append(['#','.','.','.','#'])
        >>> grid1.append(['#','*','.','.','#'])
        >>> s1 = GridPegSolitairePuzzle(grid1, marker_set)
        >>> s1.is_solved()
        True
        """
        # override is_solved
        # A configuration is solved when there is exactly one "*" left
        counting = []
        for row in self._marker:
            for character in row:
                if character == '*':
                    counting.append(character)
        return len(counting) == 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    from puzzle_tools import depth_first_solve

    grid = [["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", ".", "*", "*"],
            ["*", "*", "*", "*", "*"]]
    gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
    import time

    start = time.time()
    solution = depth_first_solve(gpsp)
    end = time.time()
    print("Solved 5x5 peg solitaire in {} seconds.".format(end - start))
    print("Using depth-first: \n{}".format(solution))

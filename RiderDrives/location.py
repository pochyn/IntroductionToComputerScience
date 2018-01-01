class Location:
    def __init__(self, row, column):
        """Initialize a location.

        @type self: Location
        @type row: int
        @type column: int
        @rtype: None
        """
        self.row = row
        self.column = column

    def __str__(self):
        """Return a string representation.

        @rtype: str
        """
        return '({},{})'.format(self.row, self.column)

    def __eq__(self, other):
        """Return True if self equals other, and false otherwise.

        @rtype: bool
        """
        return (type(self) == type(other) and
                self.row == other.row and
                self.column == other.column)


def manhattan_distance(origin, destination):
    """Return the Manhattan distance between the origin and the destination.

    @type origin: Location
    @type destination: Location
    @rtype: int
    """
    return (abs(origin.row - destination.row) +
            abs(origin.column - destination.column))


def deserialize_location(location_str):
    """Deserialize a location.

    @type location_str: str
        A location in the format 'row,col'
    @rtype: Location
    """
    new_lst = location_str.split(",")
    return Location(int(new_lst[0]), int(new_lst[1]))

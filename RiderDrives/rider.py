from location import Location

"""
The rider module contains the Rider class. It also contains
constants that represent the status of the rider.

=== Constants ===
@type WAITING: str
    A constant used for the waiting rider status.
@type CANCELLED: str
    A constant used for the cancelled rider status.
@type SATISFIED: str
    A constant used for the satisfied rider status
"""

WAITING = "waiting"
CANCELLED = "cancelled"
SATISFIED = "satisfied"


class Rider:
    """
    A rider in  a ride-sharing service.

    === Attributes ===
    @type id: str
        A unique identifier for the rider.
    @type origin: Location
        The current location of the rider.
    @type destination: Location
        The destination of the rider.
    @type patience: int
        Patience of a rider.
    """

    def __init__(self, identifier, origin, destination, patience):
        """
        Initialize a rider.

        @type self: Rider
        @type identifier: str
        @type origin: Location
        @type destination: Location
        @type patience: int
        @rtype: None
        """
        self.status = None
        self.id = identifier
        self.origin = origin
        self.destination = destination
        self.patience = patience

    def __eq__(self, other):
        """
        Return True if self equals other, and false otherwise.

        @type self: Rider
        @type other: Rider
        @rtype: bool

        >>> r1 = Rider('Stas', Location(2,1), Location(3,4), 5)
        >>> r2 = Rider('Livia', Location(2,1), Location(3,4), 3)
        >>> r3 = Rider('Stas', Location(2,1), Location(3,4), 5)
        >>> r1 == r2
        False
        >>> r1 == r3
        True
        """
        return (type(self) == type(other) and
                self.destination == other.destination and
                self.origin == other.origin and
                self.id == other.id and
                self.patience == other.patience)

    def __str__(self):
        """
        Return a string representation.

        @type self: Rider
        @rtype: str

        >>> origin = Location(1, 1)
        >>> destination = Location(2, 2)
        >>> rider = Rider('Livia', origin, destination, 5)
        >>> print (rider)
        Livia
        """
        return self.id

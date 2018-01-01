from puzzle import Puzzle


class WordLadderPuzzle(Puzzle):
    """
    A word-ladder puzzle that may be solved, unsolved, or even unsolvable.
    """

    def __init__(self, from_word, to_word, ws):
        """
        Create a new word-ladder puzzle with the aim of stepping
        from from_word to to_word using words in ws, changing one
        character at each step.

        @type from_word: str
        @type to_word: str
        @type ws: set[str]
        @rtype: None
        """
        (self._from_word, self._to_word, self._word_set) = (from_word,
                                                            to_word, ws)
        # set of characters to use for 1-character changes
        self._chars = "abcdefghijklmnopqrstuvwxyz"

    def __eq__(self, other):
        """
        Return whether WordLadderPuzzle self is equivalent to other.

        @type self: WordLadderPuzzle
        @type other: WordLadderPuzzle | Any
        @rtype: bool

        >>> from_word = "car"
        >>> from_word1 = "red"
        >>> to_word = "rap"
        >>> ws = {"axe", "any", "bar"}
        >>> wlp = WordLadderPuzzle(from_word, to_word, ws)
        >>> wlp1 = WordLadderPuzzle(from_word, to_word, ws)
        >>> wlp2 = WordLadderPuzzle(from_word1, to_word, ws)
        >>> wlp == wlp1
        True
        >>> wlp == wlp2
        False
        """
        return (type(self) == type(other) and
                self._from_word == other._from_word and
                self._to_word == other._to_word and
                self._chars == other._chars and
                self._word_set == other._word_set)

    def __str__(self):
        """
        Return a human-readable string representation of WordLadderPuzzle self.

        @type self: WordLadderPuzzle
        @rtype: str

        >>> from_word = "car"
        >>> to_word = "rap"
        >>> ws = {"axe", "any", "bar"}
        >>> wlp = WordLadderPuzzle(from_word, to_word, ws)
        >>> print(wlp)
        car
        rap
        """
        return self._from_word + '\n' + self._to_word

    def extensions(self):
        """
        Return all possible extensions from from_word changing only one letter.

        @type self: WordLadderPuzzle
        @rtype: list[WordLadderPuzzle]

        >>> ws = {"axe", "any", "bar"}
        >>> wlp = WordLadderPuzzle("car", "rap", ws)
        >>> a = wlp.extensions()[0]
        >>> b = WordLadderPuzzle("bar", "rap", ws)
        >>> a == b
        True
        """
        # consider every word from dictionary
        possible_words = []
        for word in self._word_set:
            # according to rules we can use only words with same length
            if len(self._from_word) == len(word):
                i = 0
                difference = 0

                while i < len(word):
                    # count different letter of the word
                    if self._from_word[i] != word[i]:
                        difference += 1
                    i += 1

                # consider only words with difference of 1 letter
                if difference == 1:
                    possible_words.append(word)

        # return all possible extensions
        extensions = []
        for word in possible_words:
            extensions.append(
                    WordLadderPuzzle(word, self._to_word, self._word_set))
        return extensions

    def is_solved(self):
        """
        Return whether from_word is the same as to_word

        @type self: WordLadderPuzzle
        @rtype: bool

        >>> ws = {"axe", "any", "bar"}
        >>> wlp = WordLadderPuzzle("car", "rap", ws)
        >>> wlp1 = WordLadderPuzzle("car", "car", ws)
        >>> wlp.is_solved()
        False
        >>> wlp1.is_solved()
        True
        """
        return self._from_word == self._to_word


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    with open("words.txt", "r") as words:
        word_set = set(words.read().split())
    w = WordLadderPuzzle("same", "cost", word_set)
    start = time()
    sol = breadth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using breadth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))
    start = time()
    sol = depth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using depth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))

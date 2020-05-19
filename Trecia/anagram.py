import doctest


def anagram(word1, word2):
    """
    Tells if two words are anagrams
    >>> anagram("labas", "bsaal")
    True
    >>> anagram("hello", "oelhl")
    True
    >>> anagram("first", "second")
    False
    >>> anagram("first", "stRif")
    False
    >>> anagram("123546","643152")
    True
    >>> anagram()
    Traceback (most recent call last):
    ...
    TypeError: anagram() takes exactly 2 arguments (0 given)
    """
    if len(word1) != len(word2):
        return False
    sorted_first = sorted(word1)
    sorted_second = sorted(word2)
    if sorted_first == sorted_second:
        return True
    else:
        return False


if __name__ == "__main__":
    doctest.testmod()


# Run with python anagram.py -v
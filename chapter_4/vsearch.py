def search4vowels():
    """Display any vowels found in an asked-for word."""
    vowels = set('aeiou')
    word = "hitch-hiker"
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)
search4vowels()

#A function is FALSE if it evaluates to zero, the value NONE, an empty string or an empty data structure
bool(0)
bool(0.0)
bool('')
bool([])
bool({})
bool(None)

#A function is TRUE for every non-empty list, string or data structure
bool(1)
bool(-1)
bool(42)
bool(0.0000000001)
bool('panic')
bool([42, 43, 44])
bool({'a': 42, 'b': 43})

def search4vowels():
    """Display any vowels found in an asked-for word."""
    vowels = set('aeiou')
    word = "hitch-hiker"
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)
search4vowels()


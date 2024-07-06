vowels = ['a', 'e', 'e', 'i', 'o', 'u', 'u']
vowels = set('aaeiouu')
print(vowels)

vowels = set('aeiou')
word = 'hello'
u = vowels.union(set(word))
print(u)

uList = sorted(list(u))
print(uList)

d = vowels.difference(set(word))
print(d)

dList = sorted(list(d))
print(dList)

i = vowels.intersection(set(word))
print(i)

iList = sorted(list(i))
print(iList)

vowels = set('aeiou')
word = "hitch-hiker"
found = vowels.intersection(set(word))
for vowel in found:
    print(vowel)
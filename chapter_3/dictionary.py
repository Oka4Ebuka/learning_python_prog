person3 = {'gender': 'male', 'name': 'ford prefect', 'home planet': 'betelgeuse seven', 'occupation': 'researcher'}
print(person3)
person3['home planet']
print(person3['home planet'])
person3['name']
print(person3['name'])

found = {}
print(found)
vowels = ['a', 'e', 'i', 'o', 'u']
word = "hitch-hiker"
found = {}
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0
for letter in word:
    if letter in vowels:
        print(letter)
        found[letter] = found[letter] +1
        found[letter] += 1
        print(found)
for k in found:
    print(k, 'was found', found[k], 'time(s)')
for k in sorted(found):
    print(k, 'was found', found[k], 'time(s)')
for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s)')

fruits = {}
fruits['apples'] = 10
if 'bananas' in fruits:
    fruits['bananas'] +=1
else:
    fruits['bananas'] = 1
if 'pears' not in fruits:
    fruits['pears'] = 0
    fruits['pears'] +=1
fruits.setdefault('pears', 0)
fruits['pears'] +=1
print(fruits)

vowels = ['a', 'e', 'i', 'o', 'u']
word = "universe"
found = {}
for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] +=1
        print(found)

vowels = ['a', 'e', 'e', 'i', 'o', 'u', 'u']
vowels = set('aaeiouu')
print(vowels)
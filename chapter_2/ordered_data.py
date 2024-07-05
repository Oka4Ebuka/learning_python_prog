found = []
len(found)
print(len(found))

found.append('a')
len(found)
print(len(found))
found.append('e')
found.append('i')
found.append('o')
len(found)
print(len(found))

if 'u' not in found:
    found.append('u')
    len(found)
    print(len(found))

vowels = ['a', 'e', 'i', 'o', 'u']
word = "milliways"
for letter in word:
    if letter in vowels:
        print(letter)

vowels = ['a', 'e', 'i', 'o', 'u']
word = "chukwuebuka"
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
            print(found)
for vowel in found:
    print(vowel)

vowels = ['a', 'e', 'i', 'o', 'u']
word = input("provide a word to search for vowels:")
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)

nums = [1, 2, 3, 4]
nums.remove(3)
print(nums)

nums = [1, 2, 4]
nums.pop()
print(nums)

nums.pop(1)
print(nums)

nums.extend([2,3])
print(nums)

phrase = "don't panic"
plist = list(phrase)
plist.pop()
plist.pop(9)
plist.pop(8)
plist.pop(0)
plist.insert(5, plist.pop(6))
plist.pop(2)
plist.insert(2, plist.pop(3))
print(plist)

first = [1, 2, 3, 4, 5]
second = first
second.append(6)
print(second)
third = second.copy()
print(third)
third.append(7)
print(third)

car = list(u for u in range(1, 10, 1))
print(car)

word = "don't panic"
wordlist = list(word)
wordlist[0:10:3]
print(wordlist[0:10:3])
wordlist[3:]
print(wordlist[3:])

book = "the hitchhiker's guide to the galaxy"
booklist = list(book)
print(booklist)
booklist[0:3]
print(booklist[0:3])
''.join(booklist[0:3])
print(''.join(booklist[0:3]))
booklist[-6:]
print(booklist[-6:])
''.join(booklist[-6:])
print(''.join(booklist[-6:]))

backwards = booklist[::-1]
''.join(backwards)
print(''.join(backwards))

everyOther = booklist[::2]
print(everyOther)
''.join(everyOther)
print(''.join(everyOther))
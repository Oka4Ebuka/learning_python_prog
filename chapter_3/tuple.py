vowels = ['a', 'e', 'i', 'o', 'u']
type(vowels)
#print(vowels)

vowels2 = ('a', 'e', 'i', 'o', 'u')
#type(vowels2)
#print(vowels2)

#vowels[2] = 'I'
#print(vowels)

#vowels2[2] = 'I'
#print(vowels2[2])

#t = ('python')
#print(t)

#t2 = ('python',)
#print(t2)

people = {}
people['ford'] = {'name': 'ford prefect', 'gender': 'male', 'occupation': 'researcher', 'home planet': 'betelgeuse seven'}
{'ford': {'name': 'ford prefect', 'gender': 'male', 'occupation': 'resercher', 'home planet': 'betelgeuse seven'}}
#print(people)

people['tricia'] = {'name': 'tricia mcmillan', 'gender': 'female', 'occupation': 'mathematician', 'home planet': 'earth'}
people['arthur'] = {'name': 'arthur dent', 'gender': 'male', 'occupation': 'sandwich-maker', 'home planet': 'earth'}
people['robot'] = {'name': 'marvin', 'gender': 'male', 'occupation': 'paranoid android', 'home planet': 'unknown'}
#print(people)

import pprint
pprint.pprint(people)
print(pprint.pprint(people))

people['arthur'] = {'name': 'arthur dent', 'gender': 'male', 'occupation': 'sandwich-maker', 'home planet': 'earth'}
people['arthur']['occupation']
print(people['arthur']['occupation'])
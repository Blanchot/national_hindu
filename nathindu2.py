# nathindu02

import requests, json, random
from filter import *

nat = 'https://newsapi.org/v1/articles?source=national-geographic&sortBy=top&apiKey=bdad6b46afa44daa95cfe4b02f51a129'
hindu = 'https://newsapi.org/v1/articles?source=the-hindu&sortBy=top&apiKey=bdad6b46afa44daa95cfe4b02f51a129'

rnat = requests.get(nat).json()
rhindu = requests.get(hindu).json()
print('\n------------------------')
print('National Geographic Headline:')
tnat = rnat['articles'][0]['title']
print(tnat) # Top Headline
natwords = tnat.split(' ')
natwords = filter(natwords)
print(natwords)

print('\nThe Hindu Headline:')
thindu = rhindu['articles'][0]['title']
print(thindu) # Top Headline
hinduwords = thindu.split(' ')
hinduwords = filter(hinduwords)
print(hinduwords)

words = natwords + hinduwords # combine filtered lists

letters8 = []
letters7 = []
letters6 = []
letters5 = []
letters4 = []
letters3 = []
letters2 = []
letters1 = []

for i in words:
	if len(i) == 8:
		letters8.append(i)
	elif len(i) == 7:
		letters7.append(i)
	elif len(i) == 6:
		letters6.append(i)
	elif len(i) == 5:
		letters5.append(i)
	elif len(i) == 4:
		letters4.append(i)
	elif len(i) == 3:
		letters3.append(i)
	elif len(i) == 2:
		letters2.append(i)
	elif len(i) == 1:
		letters1.append(i)

print('\n8 letters: ' + str(letters8))
print('7 letters: ' + str(letters7))
print('6 letters: ' + str(letters6))
print('5 letters: ' + str(letters5))
print('4 letters: ' + str(letters4))
print('3 letters: ' + str(letters3))
print('2 letters: ' + str(letters2))
print('1 letters: ' + str(letters1))

print('\n--------')
if letters8:
	print(random.choice(letters8).upper())
if letters7:
	print(random.choice(letters7).upper())
if letters6:
	print(random.choice(letters6).upper())
if letters6 and letters1: 
	print(random.choice(letters1).upper() + ' ' + random.choice(letters6).upper())
if letters5 and letters1:
	print(random.choice(letters1).upper() + ' ' + random.choice(letters5).upper())
if letters5 and letters2:
	print(random.choice(letters2).upper() + ' ' + random.choice(letters5).upper())
if letters4:
	print(random.choice(letters4).upper() + random.choice(letters4).upper())
if letters4 and letters3:
	print(random.choice(letters3).upper() + ' ' + random.choice(letters4).upper())


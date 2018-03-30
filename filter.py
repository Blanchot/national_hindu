# filter function for nathindu v.1
# need to check for vs (leaving only the v)
# This caused an index error line 91: string index out of range
# '8th World Wonder' May Lie Below Volcanic Lakeshore
# I think it is because of: "Wonder'" single quote in double qotes

apostrophe = "'"
colon = ':'
comma = ','
period = '.'
question = '?'
hyphen = '-'
dash = '–'


def filter(l):
	l_filtered = []
	# filter apostrophes
	for i in l:
		if apostrophe in i:
			splitword = i.split(apostrophe)
			l_filtered.append(splitword[0])
		else:
			l_filtered.append(i)
	# print('Apostrophes gone: ' + str(l_filtered))
	l = l_filtered
	l_filtered = []

	# filter commas
	for i in l:
		if comma in i:
			splitword = i.split(comma)
			l_filtered.append(splitword[0])
		else:
			l_filtered.append(i)
	# print('Commas gone: ' + str(l_filtered))
	l = l_filtered
	l_filtered = []

	# filter colons
	for i in l:
		if colon in i:
			splitword = i.split(colon)
			l_filtered.append(splitword[0])
		else:
			l_filtered.append(i)
	# print('Colons gone: ' + str(l_filtered))
	l = l_filtered
	l_filtered = []

	# filter question marks
	for i in l:
		if question in i:
			splitword = i.split(question)
			l_filtered.append(splitword[0])
		else:
			l_filtered.append(i)
	# print('Question marks gone: ' + str(l_filtered))
	l = l_filtered
	l_filtered = []

	# remove all words with hyphens
	for i in l:
		if hyphen in i:
			splitword = i.split(hyphen)
			l_filtered.append(i)
		else:
			l_filtered.append(i)
	# print('Hyphens gone: ' + str(l_filtered))
	l = l_filtered
	l_filtered = []

	# remove dashes
	for i in l:
		if dash not in i:
			l_filtered.append(i)
	# print('Dashes gone: ' + str(l_filtered))
	l = l_filtered
	l_filtered = []


		# remove all words with periods
	for i in l:
		if period not in i:
			l_filtered.append(i)
	# print('Periods gone: ' + str(l_filtered))
	l = l_filtered
	l_filtered = []

	# filter plurals
	for i in l:
		if i[-1] == 's':
			i = i[:-1]
			l_filtered.append(i)
		else:
			l_filtered.append(i)
	# print('Plurals gone: ' + str(l_filtered))
	l = l_filtered
	l_filtered = []

		# filter ACRONYMS
	for i in l:
		if not i[:-1].isupper():
			l_filtered.append(i)
	# print('Acronyms gone: ' + str(l_filtered))
	l = l_filtered
	l_filtered = []

	# filter for length
	for i in l:
		if len(i) < 9:
			l_filtered.append(i)
	# print('Less than 9:' + str(l_filtered))
	return l_filtered

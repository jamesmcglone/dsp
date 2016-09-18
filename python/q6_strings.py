# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.
    
    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """

    if count < 10:
    	return 'Number of donuts: %d' % count
    elif count >= 10:
    	return 'Number of donuts: many'
    else:
    	print "ERROR"

#print donuts(4)
#print donuts(9)
#print donuts(10)
#print donuts(99)

def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    word_length = len(s)

    if word_length < 2:
    	return ''
    elif word_length >= 2:
    	return s[:2] + s[-2:]
    else:
    	print "ERROR"

#new_thing = raw_input('> ')
#print both_ends(new_thing)

def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    slist = list(s)
    first = slist[0]
    new_list = []
    new_string =''
    counter = 0

    
    for c in range(len(slist)):
    	
    	if (counter > 0) and (slist[c] == first):
    		slist[c] = '*'
    		new_list.append(slist[c])
    	else:
    		new_list.append(slist[c])
    	counter += 1
    return new_string.join(new_list)    	

#fix_start('babble')
#fix_start('aardvark')
#fix_start('google')
#fix_start('donut')


def mix_up(a, b):

	"""
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """

	heada = a[:2]
	headb = b[:2]
	taila = a[2:]
	tailb = b[2:]
	return '%s%s %s%s' % (headb, taila, heada, tailb)

#mix_up('mix', 'pod')
#mix_up('dog', 'dinner')
#mix_up('gnash', 'sport')
#mix_up('pezzy', 'firm')


def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """

    if len(s) > 2:
    	if s[-3:] != 'ing':
    		return s + 'ing'
    	else:
    		return s + 'ly'
    else: 
    	return s

#verbing('hail')
#verbing('swiming')
#verbing('do')

import re

def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """

    slist = re.split('(\W+)', s)
    new_string = ''
    	
    bad_num = 0
    not_num = 0

    for w in range(len(slist)):
    	
    	if slist[w] == 'bad':
    		bad_num = w
    	elif slist[w] == 'not':
    		not_num = w

    if bad_num > not_num:
    	slist[bad_num] = 'good'
    	del slist[not_num:bad_num]
    
    return new_string.join(slist)


#print not_bad('This movie is not so bad')
#print not_bad('This dinner is not that bad!')
#print not_bad('This tea is not hot')
#print not_bad("It's bad yet not")

def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """

    if len(a) % 2 == 0:
    	ahead = a[:len(a)/2]
    	aback = a[len(a)/2:]
    else:
    	ahead = a[:(len(a)/2)+1]
    	aback = a[(len(a)/2)+1:]

    if len(b) % 2 == 0:
    	bhead = b[:len(b)/2]
    	bback = b[len(b)/2:]
    else:
    	bhead = b[:(len(b)/2)+1]
    	bback = b[(len(b)/2)+1:]

    return ahead+bhead+aback+bback


print front_back('abcd', 'xy')
print front_back('abcde', 'xyz')
print front_back('Kitten', 'Donut')

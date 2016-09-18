# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both are sequences and are indexed by integers. Tuples differ from lists as they are immutable and use parentheses instead of square brackets. 

Tuples work as keys in dictionaries. Since dictionaries are implemented using hashtables, keys need to be hashable, i.e. taking a value of any kind will return an integer. Lists cannot be used as keys, their mutability would cause problems in searching the dictionary hashtable after keys are modified. Multiple keys could have the same entry or a key could no longer be found. Since a tuple's values cannot be changed, they provide appropriate keys for dictionaries.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists are ordered collections of elements whereas sets are unordered collections of unique (no duplicates) and immutable objects.

List Example:

```
animals = ['dog', 'cat', 'mouse']
animals.append('cat')

print animals
```

Set Example:

```
prime_set = {13, 7, 3, 5, 17}
prime_set.add(7)

print prime_set
```
For finding an element, the performance of sets is faster than lists. Using a hash function, one can map to an element's bucket. In lists, each element contained therein would need to be compared sequentially.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> It allows for the creation of anonymous functions. `Lambda` is often used to apply functional concepts.
```
fruit_inventory = {'apple': 5, 'orange': 10, 'banana': 3}
sorted(fruit_inventory, key=lambda fruit: fruit[1]) #sort by number of fruit pieces
```
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are used to construct lists in a concise manner. Operations are used to create an iterable list or one that meets specific criteria. 
Example of `map` with equivalent
```
cubes = [x**3 for x in range(10)] #more concise and readable than 'map' equivalent below

cubes = map(lambda x: x**2, range(10))

```
Example of `filter` with equivalent
```
number_list = range(10)
even_num = [x for x in number_list if x % 2 == 0] # more concise and faster than the 'filter' equivalent below

even_num = filter(lambda x: x % 2 == 0, number_list)
```
Set and Dictionary comprehensions, respectively:
```
s = { x for x in range(10) } #Set comprehension

d = {v: True for v in range(10)} #Dictionary comprehension
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)






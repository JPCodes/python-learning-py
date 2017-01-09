# Strings, immutable, sequence
len('hey') # Gets length

str = "hello world!"
str[1:] # Slicing from [1] to end (Includes index 1)
str[:3] # Slicing from [0] to [2] (3 items; up to (but not including) 3)
str[-1] # Like an array
str[:-1] # Like an array, grab everything except the last letter
str[::1] # :: (everything, front to back), 1 (steps)
str[::2] # :: (everything, front to back), 2 (every second index)
str[::-1] # Reverse string

str.upper() # uppercase all
str.lower() # lowercase all
str.split() # To array
str.split('') # To array by all letters

str = 'string'
print 'variable s: %s' %(str) # Interpolation; %s converts to string (also %r repr)

x = 13.13
print 'variable x: %s' %(x)

print 'Floating point number: %1.2f' %(13.145) # Before decimal how many spaces before the print; Significant figures after decimal
# Prints 13.14

print 'First: %s, second %s, third %s' %('hi', 'two', 3) # Passes in order

print 'First: {x} Second: {y} Third: {x}'.format(x='inserted', y ='two') # Inserts variable value

# https://pyformat.info/

# Lists, mutable, sequence (arrays)
my_list = [0, 1, 2, 3]
my_list[1:], [:3], len() # works the same as strings
my_list + [4] # Not permanent
my_list = my_list + [4] # Permanent
my_list*2 # Doubles list

my_list.append(4) # Like Push
my_list.pop() # Removes last index, destructive; Can take index argument
my_list.reverse(), .sort() # Permanent

# Lists in lists are called 'matrix'

first_col = [row[0] for row in matrix] # For every element or row (2) in the matrix (3), grab the zero index in the row (1)

# Dictionaries, mutable, mapping (Key:value pairs)

my_dict = {'key1':'value','key2':'value2'} # Declaration
my_dict['key2'] # Grabs 'value'
my_dict['key2'][1:] # You can use string methods

my_dict2 = {'k1':125}
my_dict2['k1'] - 120 # Not permanent
my_dict2['k1'] = my_dict2['k1'] - 120 # Permanently reassigns
my_dict2['k1'] += 100 # Permanent

d = {}
d['animal'] = 'Dog' # Adds key value pair

d = {'k1': {'nestkey': {'subnestkey': 'value'}}} # Nesting is cool
d['k1'] # nestkey object
d['k1']['nestkey'] # subnest object
d['k1']['nestkey']['subnestkey'] # 'value'; You can call methods on these
d.keys(), .values() # Returns keys or values (out of order)

d = {'k1': 1, 'k2': 2, 'k3': 3}
d.items() # Returns tuples of items (list): [('k3', 3), ('k2', 2), ('k1', 1)]

# Tuples, immutable
    # Use Tuples when you want something immutable (like a calendar)
t = (1, 2, 3, 'four', 3) # Declaration; mixed object types; can use len()
t[1] # Indexing like strings, lists
t.index(2) # Returns index of 2 which is [1]
t.count(3) # Returns number of times 3 appears in the Tuple, which is 2

# Files (interacting with external files)

f = open('test.txt') # Opens a file in the same directory
f.read() # Reads to the end, cursor stays at the end; use in larger files
f.seek(0) # Returns cursor to the beginning
f.readlines() # Puts it into a list
for line in open('new.txt'): # Reads..
    print line  # ..and prints

# Sets, unique items

x = set() # Declaration
x.add(1) # Add something to it, looks like a dictionary

l = [1, 1, 1, 2, 3, 3, 3, 4, 5] # Declare a list
x = set(l) # Results in {1, 2, 3, 4, 5} (unique)

# Booleans
    # True, False, None

    # http://www.codeabbey.com/index/task_list
    # https://www.reddit.com/r/dailyprogrammer/
    # http://www.pythonchallenge.com/

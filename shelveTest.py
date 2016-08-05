#--------------------------------#
# Testing shelve serialization   #
#--------------------------------#

import shelve

# ------- BASIC TEST -------
# ADD TO SHELF
#                 SAVE PATH          C is CREATE/READ/WRITE
with shelve.open('data/shelf-test', 'c') as shelf:
    integers = [1, 2, 3, 4, 5]
    shelf['ints'] = integers

# READ FROM SHELF
#                 SAVE PATH          R is READ ONLY
with shelve.open('data/shelf-test', 'r') as shelf:
    for key in shelf.keys():
        print(key, shelf[key])


# ------- TESTING DICTIONARY INSIDE SHELF -------
assets = ['Fire Effects',   'Fantasy Asset Pack',   'Cool Thing']
prices = [ 24.99,            60.00,                  5.00]
images = ['effects.png',    'fantasy.png',          'thing.png']
urls   = ['http://www.google.com/',
          'http://www.yahoo.com/',
          'http://www.facebook.com/']

# ADD TO SHELF
with shelve.open('data/latest-query', 'c') as shelf:
    for x in range(len(assets)):
        item_name = 'item{}'.format(x)
        item = {
            'asset' : assets[x],
            'price' : prices[x],
            'image' : images[x],
            'url'   : urls[x]
        }
        shelf[item_name] = item

# READ FROM SHELF
with shelve.open('data/latest-query', 'r') as shelf:
    # Dump all key/value pairs
    for key in shelf.keys():
        print (key, shelf[key])

    # Dump all asset names
    for value in shelf.values():
        print (value['asset'])
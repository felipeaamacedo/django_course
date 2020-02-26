#DICTIONARIES
## dictionaries is similar to the object of javascript, however they do not accept methods inside the dictionary like in a javascript object, thay are only hashtables.

### it can be writen in single line, as shown below,
my_stuff = {"key1":"value", 'key2':'value2', 'key3':{'123':[1,2,'grabMe']}}

### or, it may be writen similar to a object structure, making it easy to read.
my_stuff2 = {
    "key1":"value", 
    'key2':'value2',
    'key3':{
        '123':[1,2,'grabMe']
        }
}


print(my_stuff['key2'])
print(my_stuff)
print(my_stuff['key3']['123'][2]) #grabbing grabMe, it's in the index 2, of keyvalue '123' of the 'key3'
print(my_stuff['key3']['123'][2].upper()) #and I am able to make the value upper, since its a STRING


# REASIGNING OBJECT ITEMS
my_stuff3 = {'lunch':'pizza', 'bfast':'eggs'}

## reasigning lunch value. 
my_stuff3['lunch'] = 'burger'

## adding another keyvalue 'dinner'
my_stuff3['dinner'] = 'pasta'

print(my_stuff3['lunch'])
print(my_stuff3)
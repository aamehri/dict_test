#insertion and clearing
my_dict = {}
print("Print the initial empty dictionary: ", my_dict)
my_dict['key1'] = 15
print("After inserting the first value pair: ", my_dict)
#duplicating the key
my_dict['key1'] = 15
print("after duplicating the key: ", my_dict)
my_dict['key2'] = 15
print("after inserting another distinct key: ", my_dict)
#update a value item
my_dict.update({'key1': 'joe'})
print("Updated dictionary: ", my_dict)
#remove an item based on key value
my_dict.pop('key1')
print("Item removed based on key value, show what remains: ", my_dict)
#remove with del
del my_dict['key2']
print("Item removed with del, show waht remains:", my_dict)
#re-insert some items
for item in range(3):
    key = "key" + str(item)
    my_dict[key] = item
print("Content of automatically filled dictionary: ", my_dict)
#remove the last inserted item
my_dict.popitem()
print("Content after removing last inserted item: ", my_dict)

my_dict.clear()
print("After clearing the dictionary: ", my_dict)


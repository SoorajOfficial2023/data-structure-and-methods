my_dict = {}
content = {'name':'jhone','age':25,'city':'newyork'}
my_dict.update(content)
print(my_dict)

my_dict_copy = my_dict.copy()
print(my_dict_copy)

my_dict.pop('age')
print(my_dict)

my_dict.clear()
print(my_dict)
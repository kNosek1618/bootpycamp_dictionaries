
instructors = {
    "name": "Konrad",
    "own_dogs": True,
    "num_curses": 4,
    "favorite_language": "python",
    "is_hilarious": False,
    89: "ma favorite number"
}

for value in instructors.values():
    print(value)
# # # RESULT # # #
# Konrad
# True
# 4
# python
# False
# ma favorite number


print(instructors.values())
# # # RESULT # # #
# dict_values(['Konrad', True, 4, 'python', False, 'ma favorite number'])


for key in instructors.keys():
    print(key)
# # # RESULT # # #
# name
# own_dogs
# num_curses
# favorite_language
# is_hilarious
# 89


print(instructors.items())
# # # RESULT # # #
# dict_items([('name', 'Konrad'), ('own_dogs', True),
# ('num_curses', 4), ('favorite_language', 'python'),
# ('is_hilarious', False), (89, 'ma favorite number')])


for i in instructors.items():
    print(i)
# # # RESULT # # #
# ('name', 'Konrad')
# ('own_dogs', True)
# ('num_curses', 4)
# ('favorite_language', 'python')
# ('is_hilarious', False)
# (89, 'ma favorite number')


for k,v in instructors.items():
    print(f"key is {k} and value is {v}")
# # # RESULT # # #
# key is name and value is Konrad
# key is own_dogs and value is True
# key is num_curses and value is 4
# key is favorite_language and value is python
# key is is_hilarious and value is False
# key is 89 and value is ma favorite number



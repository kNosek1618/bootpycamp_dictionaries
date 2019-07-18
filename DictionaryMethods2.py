
learner = {
    "name": "Konrad",
    "own_dogs": True,
    "num_curses": 4,
    "favorite_language": "python",
    "is_hilarious": False,
    89: "ma favorite number"
}

learner.pop("own_dogs")
print(learner)
# # # RESULT # # #
# REMOVE THE own_dogs item from dictionary
# {'name': 'Konrad', 'num_curses': 4, 'favorite_language': 'python', 'is_hilarious': False, 89: 'ma favorite number'}

learner.popitem()
print(learner)
# # # RESULT # # #
# REMOVE THE LAST ITEM FROM DICTIONARY
# {'name': 'Konrad', 'num_curses': 4, 'favorite_language': 'python', 'is_hilarious': False}





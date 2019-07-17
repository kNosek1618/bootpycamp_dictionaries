
instructors = {
    "name": "Konrad",
    "own_dogs": True,
    "num_curses": 4,
    "favorite_language": "python",
    "is_hilarious": False,
    89: "ma favorite number"
}

print("name" in instructors)
# # # RESULT # # #
# True


# WAY FOR ACCESS TO VALUE
print(4 in instructors)
    # # # RESULT # # #
    # False

print(4 in instructors.values())
    # # # RESULT # # #
    # True
# Set items are enclosed in curly brackets
# Set is unordered
# Set is mutable, can contain only immutable items
# Set elements are unique
# Elements can contain only immutable items



"""
Python Set Attributes
"""

# print(dir(set))



"""
Creating Python Sets
"""

# set = set()
# set = {1,2,3}
# print(set)
# print(type(set))



"""
Modifying a set in Python
"""
# set_example = {"Day", "May"}
# # set_dosent_allow_indexing_example[0] = "Jay"
# # set_dosent_allow_mutable_data_to_be_added_example.add(["Hello", 1])

# set_example.add("Jay")
# set_example.add(5)
# set_example.add(7.5)
# set_example.add(3j+3)
# set_example.update([1,2,3])
# print(set_example)

# print(help(set.add))
# print(help(set.update))

"""
Removing elements from a set
"""
# set_example = {1,2,3,4,5}
# set_example.discard(1)
# set_example.remove(4)
# set_example.pop()
# print(set_example)
# print(type(set_example))
# print(help(set.pop))

# set_dosent_accept_duplicates_example = {"Hello",1, "Hello", 1, "Hello", 1}
# print(type(set_dosent_accept_duplicates_example))
# print(set_dosent_accept_duplicates_example)


"""
Set Union Operations
"""
# a = {1,2,3,6,7}
# b = {4,5,6,7,8,9}

# print(a | b)
# print(a.union(b))



"""
Set Intersection Operations
"""

# a = {1,2,3,6,7}
# b = {4,5,6,7,8,9}

# print(a & b)
# print(a.intersection(b))




"""
Set Difference Operations
"""

# a = {1,2,3,4,6,7,9}
# b = {2,5,6,7,8,9}
# print(a - b)
# print(a.difference(b))
# print(b - a)
# print(b.difference(a))

"""
Set Symmetric Difference
"""
# a = {1,2,3,4,6,7,9}
# b = {2,5,6,7,8,9}
# print(a ^ b)
# print(a.symmetric_difference(b))


"""
Set Methods
"""

# print(dir(set))

print("Splitting Examples")
example_str = "a b c d    e f    g    h i j k"
example_list = example_str.split(" ")
print("Example 1")
print(example_str)
print(example_list)
print("a b c d    e f    g    h i j k".split())
print()

example_str2 = "a,  b, c, d, e, f, g, h, i, j, k"
example_list2 = example_str2.split(", ")
print("Example 2")
print(example_str2)
print(example_list2)
print()

print("Stripping Examples")
strip_example1 = "    I am the very best    "
stripped_example1 = strip_example1.strip()
print("Example 1")
print(strip_example1, ".")
print(stripped_example1, ".")
print()

strip_example2 = "'this is a quote'"
stripped_example2 = strip_example2.strip("'")
print("Example 2")
print(strip_example2)
print(stripped_example2)
print()

strip_example3 = "(I am in a parenthesis)"
stripped_example3 = strip_example3.strip("()")
print("Example 3")
print(strip_example3)
print(stripped_example3)
print()

strip_example4 = "() hello ()"
stripped_example4 = strip_example4.strip("()")
print("Example 4")
print(strip_example4)
print(stripped_example4)
print()

strip_example5 = "(I am in a parenthesis)"
stripped_example5 = strip_example5.lstrip("()")
print("Example 5")
print(strip_example5)
print(stripped_example5)
print()

strip_example6 = "(I am in a parenthesis)"
stripped_example6 = strip_example6.rstrip("()")
print("Example 6")
print(strip_example6)
print(stripped_example6)
print()


# Exercises
# input: exercise1 = "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
# output: get the sum of the contents of the list

exercise1 = "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"

# Exercises
# input: exercise1 = "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
# output: get the sum of the contents of the list
exercise1 = "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
stripped_exercise1 = exercise1.strip("[]")
print(stripped_exercise1)
splited_e1 = stripped_exercise1.split(",")
print(splited_e1)

# Make a list of str into a list of int by using list comprehension
int_e1 = [int(i) for i in splited_e1]
print(int_e1)
print(sum(int_e1))

# total_sum = 0
# for i in splited_e1:
#     total_sum = total_sum + int(i)
# print(total_sum)

# Making it look like it's operating on the whole list
def list_int(my_list):
    return [int(x) for x in my_list]

new_list_e1 = list_int(splited_e1)
print(new_list_e1)

print()
# Working with lists

print("Working with Lists")
def list_add_one(my_list):
    for i in range(len(my_list)):
        my_list[i] += 1 # my_list[i] = my_list[i] + 1

print("List Add One")
list_ref_example1 = [1, 2, 3, 4]
list_add_one(list_ref_example1)
print(list_ref_example1)
print()

print("Avoiding modification outside the function")
list_ref_example2 = [1, 2, 3, 4]
list_add_one([x for x in list_ref_example2])
print(list_ref_example2)
print()

import copy

list_ref_example3 = [1, 2, 3, 4]
print("Before function call")
print(list_ref_example3)
list_add_one(copy.copy(list_ref_example3))
print("After function call")
print(list_ref_example3)
print()

def dict_add_one_a(my_dict):
    my_dict["a"] += 1

print("Dictionary Example")
dict_ref_example1 = {"a" : 1, "b" : 2}
print("Before function call")
print(dict_ref_example1)
dict_add_one_a(dict_ref_example1)
print("After function call")
print(dict_ref_example1)
print()





def int_add_one(my_x):
    my_x += 1
    print("In the function")
    print(my_x)

print("Int Add One")

x = 10
int_add_one(x)
print("Outside the function")
print(x)
print()






# Sorting lists
print("Sorting lists using .sort")
a = [10, 7, 18, 3, 0, 10]
a.sort(reverse = True)
print(a)
print()

print("Sorting lists using sorted()")
b = [10, 7, 18, 3, 0, 10]
print("b before sorted")
print(b)
b_sorted = sorted(b)
print("b after sorted")
print(b)

print("actual sorted b")
print(b_sorted)
print()

print("b.sort()")
b.sort()
print(b)
print()



# sorting with tuples
print("Tuples")
tuple_example = (1, 2, 3, 4, 5, 6)
print(tuple_example)
print(tuple_example[2])


my_list = [(1, 2), (3, 4), (-1, -2), (1, 5), (1, 10)]
sorted_list = sorted(my_list)
print("Sorting tuples")
print(sorted_list)


# Exercise:
exercise2 = "aabaccdaeeacdaeadddddda"

# output the list of letters sorted by the number of occurrences
# a = 8, b = 1, c = 3, d = 8
# output: ["a", "d", "c", "b"]








print("Exercise 2 begin")
# Exercise:
exercise2 = "aabaccdaeeacdaeadddddda"
# output the list of letters sorted by the number of occurrences
# a = 8, b = 1, c = 3, d = 8
# output: ["a", "d", "c", "b"]

#1. Change exercise2 into a list: split , " " ""
#2. Sort them acsending order : .sort()
#3. Print them without duplicate : conditionls
# splitted_e2 = exercise2.split()
# print(splitted_e2)


list_e2 = [x for x in exercise2]
# tupled_list_e2 = tuple(list_e2)
# sorted_tuple = sorted(tupled_list_e2)
# print(sorted_tuple)


a = 0
b = 0
c = 0
d = 0
e = 0
etc = 0
for x in list_e2:
    if x == "a":
        a += 1 
    elif x == "b":
        b += 1 
    elif x == "c":
        c += 1 
    elif x == "d":
        d += 1 
    elif x == "e":
        e += 1 
    else :
        etc += 1 





print("Counting begin")
counted_list = [(a, "a"), (b, "b"), (c, "c"), (d, "d"), (e, "e"), (etc, "etc")]
print(counted_list)
counted_list.sort(reverse = True)
print(counted_list)
print("list comprehension")
# listed_counted = [list(x) for x in counted_list]

print("Getting first element of list of tuples")
print(counted_list[0][1])

print("Final answer")
print([x[1] for x in counted_list])

# Sample solution 1
counter_dict = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'etc' : 0}
for x in list_e2:
    if x in counter_dict:
        counter_dict[x] += 1
    else:
        counter_dict['etc'] += 1

print("Counter Dictionary")

print(counter_dict)

counted_list = [(value, key) for key, value in counter_dict.items()]
print(counted_list)
counted_list.sort(reverse = True)
print([x[1] for x in counted_list])

# Sample solution 2 -> next time, to be continued


# a = ["a", "b", "f", "g", "k"]

# a.sort() # returns nothing, but sorts a

# b = ["a", "b", "f", "g", "k"]
# sorted_b = sorted(b) # returns the sorted list, but does nothing to b
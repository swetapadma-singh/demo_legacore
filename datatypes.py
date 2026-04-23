import sys

# num = [1,2,3,4,5]
# print(num)
# num.append(6)
# print("after adding 6 = ",num)
# num.remove(3)
# print("after removing 3 = ",num)
# print("length of num = ",len(num))

# s = "hello world"
# print("original string = ",s)
# upper = s.upper()
# print("in uppercase = ",upper)
# l_count = s.count("l")
# print("number of l in the string = ",l_count)
# replace = s.replace("world","python")
# print("after replacing world with python = ",replace)

# d = {"name": "Aman", "age": 20}
# print("original dictionary = ",d)
# d["city"] = "Delhi"
# print("after adding city = ",d)
# keys = d.keys()
# print("keys of the dictionary = ",keys)
# age = d.get("age")
# print("age = ",age)

# s = {1, 2, 2, 3, 4}
# print("original set = ",s)
# s.add(5)
# print("after adding 5 = ",s)
# s.remove(2)
# print("after removing 2 = ",s)

# t = (10, 20, 30, 10)
# count = t.count(10)
# print("count of 10 in the tuple = ",count)
# index = t.index(20)
# print("index of 20 in the tuple = ",index)

# a = [1,2]
# b = a
# print("a = ",a) # [1, 2]
# b.append(3)
# print("a = ",a) # [1, 2, 3]

# a = [1, 2]
# b = a
# a = a + [3]
# print("a = ",a) # [1, 2, 3]
# print("b = ",b) # [1, 2]

# a = [1, 2]
# b = a
# a += [3]
# print("a = ",a) # [1, 2, 3]
# print("b = ",b) # [1, 2, 3]

# x = 5
# def func():
#     print("x inside function = ",x) # Error: UnboundLocalError: local variable 'x' referenced before assignment
#     x = 10
#     print("x inside function after assignment = ",x)
# func()

# x = 5
# def func():
#     global x
#     x += 10
#     print("x inside function = ",x)
#     def inner():
#         nonlocal x
#         x = x + 5
#         print("x inside inner function = ",x)
#         return x
#     return inner()
# print ("func return is ",func())
# print("x outside function = ",x)


# import copy
# a = [[1], [2]]
# b = a.copy()          # shallow copy
# c = copy.deepcopy(a)  # deep copy
# d = a
# d.append([3])
# b[0].append(99)
# c[1].append(100)
# print("b = ",b) # [[1, 99], [2]]
# print("c = ",c) # [[1], [2, 100]]
# print("d = ",d) # [[1, 99], [2], [3]]
# print("a = ",a) # [[1, 99], [2], [3]]

# a = [1, 2]
# b = a
# b += [3]
# print("a = ",a) # a =  [1, 2, 3]
# print("b = ",b) # b =  [1, 2, 3]

# a = [1, 2]
# b = a
# a = a + [3]
# b += [4]
# print("a = ",a) # a =  [1, 2, 3]
# print("b = ",b) # b =  [1, 2, 4]

# a = [[1], [2]]
# b = a.copy()
# c = b
# c[0].append(99)
# print(a) # [[1, 99], [2]]
# print(b) # [[1, 99], [2]]
# print(c) # [[1, 99], [2]]

# x = 10
# def f():
#     x = 20
#     def g():
#         global x
#         x += 3
#     g()
# f()
# print(x) # 13

# funcs = []
# for i in range(3):
#     funcs.append(lambda: i)
#     print("i = ",i) # 0, 1, 2
#     print("funcs = ",funcs)
# print("funcs outside loop = ",funcs) # [<function <lambda> at 0x0000022BF83D3B60>, <function <lambda> at 0x0000022BF8443690>, <function <lambda> at 0x0000022BF8443740>]
# for f in funcs:
#     print("f = ",f)
#     print("f() = ",f()) # 2, 2, 2
# print(type(funcs)) # <class 'list'>
# print(funcs[0])  # <function <lambda> at 0x0000022BF83D3B60>  
# print(type(funcs[0])) # <class 'function'>
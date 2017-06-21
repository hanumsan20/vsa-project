# Name:
# Date:

# proj05: functions and lists

# Part I

# def divisors(num):
#     """
#     Takes a number and returns all divisors of the number, ordered least to greatest
#     :param num: int
#     :return: list (int)
#     """
#
#     list = []
#     x = 0
#
#     for var in range(0,num):
#         x = x + 1
#         if num % x == 0:
#             list.append(x)
#         return list
#
# c = divisors(6)
# print c
#
#
#
# def prime(num):
#     """
#     Takes a number and returns True if the number is prime, otherwise False
#     :param num: int
#     :return: bool
#     """
#     list = divisors(num)
#     list = list[2:]
#     if list != []:
#         return False
#     else:
#         return True
# c = prime(25)
# print c
#
#
# c = prime(10)
# print c


    # return 0


# Part II

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2 = [1, 2, 3, 5, 6, 7, 8, 9]
lst3 = []

def intersection(lst1, lst2):

    lst1.sort()
    lst2.sort()
    for numbers in lst1:
        if lst1[0] == lst2[0]:
            lst3.append(lst1[0])
c = intersection(lst1, lst2)
print c

#
# # Part III
#
# def find_ab(side1, side2, side3):
#     """
#     Takes three side lengths an returns two smallest in a list
#     :param side1: int or float
#     :param side2: int or float
#     :param side3: int or float
#     :return: list of 2 ints or floats
#     """
#     list = [side1, side2, side3]
#     list.sort()
#     return list[0:2]
#
# c = find_ab(279, 52, 102)
# print c
#
#
# def find_c(side1, side2, side3):
#     """
#     Takes three side lengths an returns the largest
#     :param side1: int or float
#     :param side2: int or float
#     :param side3: int or float
#     :return: int or float
#     """
#     list = [side1, side2, side3]
#     list.sort()
#     return list[2]
#
# d = find_c(5, 12, 13)
# print d
    # return 0

# def square(side):
#     """
#     COMPLETE
#     Takes a side length and returns the side length squared
#     :param side: int or float
#     :return: int or float
#     """
#     return side * side
#
# c = square(15)
# print c
#     #return 0
#
# def pythagorean(a,b,c):
#     """
#     COMPLETE
#     Takes three side lengths and returns true if a^2 + b^2 = c^2, otherwise false
#     :param a: int or float
#     :param b: int or float
#     :param c: int or float
#     :return: bool
#     """
#     # return False
#     return (a**2 + b**2) == c**2
#
# c = pythagorean(5, 12, 13)
# d = pythagorean(6, 8, 10)
# print c
# print d
#
# def is_right(side1, side2, side3):
#     """
#     Takes three side lengths and returns true if triangle is right
#     :param side1: int or float
#     :param side2: int or float
#     :param side3: int or float
#     :return: bool
#     """
#     list = [side1, side2, side3]
#     list.sort()
#     if (list[0] ** 2) + (list[1] ** 2) == (list[2] ** 2):
#         return True
#     else:
#         return False
#
# d = is_right(25, 7, 24)
# print d
    #return False
#
# TESTS
# Feel free to add your own tests as needed!
#
# print ("Divisors Tests")
# # Test 1
# if divisors(1) == [1]:
#     print("Test 1: PASS")
# else:
#     print("Test 1: FAIL")
#
# # Test 2
# if divisors(8) == [1,2,4,8]:
#     print("Test 2: PASS")
# else:
#     print("Test 2: FAIL")
#
# # Test 3
# if divisors(9) == [1,3,9]:
#     print("Test 3: PASS\n")
# else:
#     print("Test 3: FAIL\n")
#
# print("Prime Tests")
# # Test 4
# if prime(9):
#     print("Test 4: FAIL")
# else:
#     print("Test 4: PASS")
#
# # Test 5
# if prime(7):
#     print("Test 5: PASS\n")
# else:
#     print("Test 5: FAIL\n")
#
# L1 = []
# L2 = [3, 4]
# L3 = [3, "a"]
# L4 = [5, "b", 10, 7, "a"]
# L5 = [5, 7, 11]
#
# print("Intersection Tests")
# # Test 6
# if intersection(L1, L2) == []:
#     print("Test 6: PASS")
# else:
#     print("Test 6: FAIL")
#
# # Test 7
# if intersection(L2, L3) == [3]:
#     print("Test 7: PASS")
# else:
#     print("Test 7: FAIL")
#
# # Test 8
# if intersection(L2, L4) == []:
#     print("Test 8: PASS")
# else:
#     print("Test 8: FAIL")
#
# # Test 9
# if intersection(L3, L4) == ["a"]:
#     print("Test 9: PASS")
# else:
#     print("Test 9: FAIL")
#
# # Test 10
# if intersection(L4, L5) == [5, 7]:
#     print("Test 10: PASS\n")
# else:
#     print("Test 10: FAIL\n")
#
# print("Is_Right Tests")
# # Test 11
# if is_right(5, 12, 13):
#     print("Test 11: PASS")
# else:
#     print("Test 11: FAIL")
#
# # Test 12
# if is_right(5, 12, 13):
#     print("Test 12: FAIL")
# else:
#     print("Test 12: PASS")

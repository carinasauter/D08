# Borrowed from https://realpython.com/learn/python-first-steps/

###############################################################################
# Modify the variables so that all of the statements evaluate to True. ########
###############################################################################

var1 = 5  # int <35 and less than or equal to 6
var2 = "python"   # str p****n****..
var3 = [1, 2, 3, 4, 5]  # list len 5 [*, *, *, *, *]
var4 = (2, 3, "Hello, Python!")  # tuple (*, *, "Hello, Python!", *, ....)# dictionary (happy:*, tuna:7, egg:salad)
var5 = {'happy': 'face', 'tuna': 7, 'egg': 'salad'}
var6 = 6.7

###############################################################################
# Don't edit anything below this comment ######################################
###############################################################################

# integers
print(type(var1) is int)
print(type(var6) is float)
print(var1 < 35)
print(var1 <= var6)

# strings
print(type(var2) is str)
print(var2[5] == 'n' and var2[0] == "p")

# lists
print(type(var3) is list)
print(len(var3) == 5)

# tuples
print(type(var4) is tuple)
print(var4[2] == "Hello, Python!")

# dictionaries
print(type(var5) is dict)
print("happy" in var5)
print(7 in var5.values())
print(var5.get("egg") == "salad")
print(len(var5) == 3)
var5["tuna"] = "fish"
print(len(var5) == 3)

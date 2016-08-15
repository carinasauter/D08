#!/usr/bin/env python3
# HW08_ch11_ex02a
# This is discussed in ThinkPython2 but not formally an exercise.
# Dictionaries have a method called 'get' that takes a key and a default value.
# If the key appears in the dictionary, get returns the corresponding value;
# otherwise it returns the default value. For example:

# >>> h = histogram('a')
# >>> print h
# {'a': 1}
# >>> h.get('a', 0)
# 1
# >>> h.get('b', 0)
# 0

# (1) Use get to write histogram_old more concisely. You should be able to
# eliminate the if statement.

# (2) Use histogram_new to take pledge.txt and create a dict histogram with
# word counts (do not change the case of the words).
###############################################################################
# Imports


# Body
pledge_histogram = {}


def histogram_old(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


def histogram_new(s):
    dictionary = {}
    for word in s:
        dictionary[word] = dictionary.get(word, 0) + 1
    return dictionary


def get_pledge_list():
    with open("pledge.txt", "r") as doc:
        text = doc.readlines()
        pledge_list = []
        for line in text:
            word_list = line.split()  # creates list of words per line
            for word in word_list:
                # appends the stripped words to the pledge word list and does
                # so for each line
                pledge_list.append(word.strip("," "." ":"))
    return pledge_list


###############################################################################
def main():  # DO NOT CHANGE BELOW
    print(histogram_new(get_pledge_list()))

if __name__ == '__main__':
    main()

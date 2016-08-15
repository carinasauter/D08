#!/usr/bin/env python3
# HW08_ch11_ex02b
# This borrows from exercise two in the book.
# Dictionaries have a method called keys that returns the keys of the
# dictionary, in no particular order, as a list.

# (1) Modify print_hist_old to print the keys and their values in alphabetical
# order.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Within main() make the appropriate function calls to print the
# alphabetical histogram of pledge.txt
###############################################################################
# Imports


# Body
# def print_hist_old(h):
#     for c in h:
#         print(c, h[c])

def print_hist_new(d):
	list_of_keys = d.keys()
	list_of_keys = sorted(list_of_keys)
	for key in list_of_keys:
		print("{}: {}".format(key, d[key]))

###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################

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
            word_list = line.split()
            for word in word_list:
                if word == "I":
                    word = word.strip()
                    pledge_list.append(word)
                else:
                    word = word.lower()
                    word = word.strip("." "," ":")
                    pledge_list.append(word)
    return pledge_list

###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################


def main():

    print_hist_new(histogram_new(get_pledge_list()))


if __name__ == '__main__':
    main()

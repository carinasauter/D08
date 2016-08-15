#!/usr/bin/env python3
# HW08_ch11_ex02d.py
# (1) Write a more concise version of invert_dict_old.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Update print_hist_new from HW08_ch11_ex02b.py to be able to print
# a sorted version of the dict (print key/value pairs from 0 through the
# largest key values, (and those in between))
# Ex. If d = {1:["this, that"], 3: ["the"]}, it prints:
#    '1: ["this", "that"]'
#    '2:'
#    '3: ["the"]'
###############################################################################
# Imports


# Body
def invert_dict_old(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def invert_dict_new(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse


def print_hist_newest(d):
    list_of_keys = d.keys()
    list_of_keys = sorted(list_of_keys)
    counter = 1
    for key in list_of_keys:
        while counter != key:
            print("{}: []".format(counter))
            counter += 1
        print('{}: {}'.format(key, sorted(d[key])))
        counter += 1


###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
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


def main():  # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())
    pledge_invert = invert_dict_new(pledge_histogram)
    print_hist_newest(pledge_invert)

if __name__ == '__main__':
    main()

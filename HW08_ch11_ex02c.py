#!/usr/bin/env python3
# HW08_ch11_ex02c.py
# (1) Modify reverse_lookup_old so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Do not edit what is in main(). It should print what is returned, a list
# of the keys that map to the values passed.
###############################################################################
# Imports


# Body
def reverse_lookup_old(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError


def reverse_lookup_new(d, v):
    list_of_keys = []
    for k in d:
        if d[k] == v:
            list_of_keys.append(k)
    return list_of_keys


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


def main():   # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())
    print(reverse_lookup_new(pledge_histogram, 1))
    print(reverse_lookup_new(pledge_histogram, 9))
    print(reverse_lookup_new(pledge_histogram, "Python"))

if __name__ == '__main__':
    main()

import sys


# Author: Kevin Castell
# PS1 for CS 4150 Algorithms
def main():
    # read input
    lines = sys.stdin.readlines()

    print(count_non_anagrams(lines))


# This function will take the dictionary, sort the words individually, then sort the list as a whole, then count the
# non-anagrams.
def count_non_anagrams(raw_dict):

    # The information about the sizes is ignored
    dictionary = raw_dict[1:]
    sorted_dict = []
    count = 0

    # Sort the words
    for word in dictionary:
        sorted_dict.append(sorted(word.lower()))

    # Sort the list
    sorted_dict.sort()

    # Check for unique words
    if sorted_dict[0] != sorted_dict[1]:
        count = count + 1

    if sorted_dict[-1] != sorted_dict[-2]:
        count = count + 1

    for i in range(1, len(sorted_dict)-1):
        if sorted_dict[i] != sorted_dict[i-1] and sorted_dict[i] != sorted_dict[i+1]:
            count = count + 1

    return count


if __name__ == "__main__":
    main()
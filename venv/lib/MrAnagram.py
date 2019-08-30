import sys


def main():
    lines = sys.stdin.readlines()

    # print(count_non_anagrams_jumble(lines))

    print(count_non_anagrams_hashing(lines))


def count_non_anagrams_jumble(raw_dict):

    dictionary = raw_dict[1:]

    solutions = []
    rejected = []
    for word in dictionary:
        sorted_word = sorted(word.lower())
        if sorted_word in solutions:
            solutions.remove(sorted_word)
            rejected.append(sorted_word)
        elif sorted_word not in rejected:
            solutions.append(sorted_word)

    return len(solutions)


def count_non_anagrams_hashing(raw_dict):

    dictionary = raw_dict[1:]
    sorted_dict = []
    count = 0

    for word in dictionary:
        sorted_dict.append(sorted(word.lower()))

    sorted_dict.sort()

    for i in range(0,len(sorted_dict)):
        if i == 0:
            if sorted_dict[i] != sorted_dict[i+1]:
                count = count + 1
        elif i == len(sorted_dict) -1:
            if sorted_dict[i] != sorted_dict[i-1]:
                count = count + 1
        else:
            if sorted_dict[i] != sorted_dict[i-1] and sorted_dict[i] != sorted_dict[i+1]:
                count = count + 1

    return count


if __name__ == "__main__":
    main()
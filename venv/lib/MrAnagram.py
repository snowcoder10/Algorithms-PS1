import sys


def main():
    lines = sys.stdin.readlines()

    print(count_non_anagrams_hashing(lines))


def count_non_anagrams_hashing(raw_dict):

    dictionary = raw_dict[1:]
    sorted_dict = []
    count = 0

    for word in dictionary:
        sorted_dict.append(sorted(word.lower()))

    sorted_dict.sort()

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
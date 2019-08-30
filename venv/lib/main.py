import sys


def main():
    lines = sys.stdin.readlines()

    worker = MrAnaga(lines)
    print(worker.count_non_anagrams())


class MrAnaga:

    def __init__(self, raw_dictionary):
        self.raw_dict = raw_dictionary
        # self.sorted_dict = {}
        self.sorted_dict = []
        self.non_anagrams = 0

    def count_non_anagrams(self):

        self.sorted_dict = self.raw_dict[1:]

        solutions = []
        rejected = []

        for word in self.sorted_dict:
            sorted_word = sorted(word.lower())
            if sorted_word in solutions:
                solutions.remove(sorted_word)
                rejected.append(sorted_word)
            elif sorted_word not in rejected:
                solutions.append(sorted_word)

        self.non_anagrams = len(solutions)
        return self.non_anagrams


if __name__ == "__main__":
    main()


from time import time
import MrAnagram
import random
import string


def main():
    calculating_runtime_doubling_n()


def random_string_genrator(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


def calculating_runtime_doubling_n():
    k = 5
    n = 4
    while n < 2**16:
        test_input = []
        for i in range(n):
            test_input.append(random_string_genrator(k))

        run_time, count = running_test(test_input)
        final_time = run_time / count
        print(str(n) + '\t' + str(final_time))

    return run_times


def running_test(test_input):
    t = 0
    count = 0
    t0 = time()
    while t <= 5:
        MrAnagram.main(test_input)
        count = count + 1
        t = time() - t0

    return t, count


if __name__ == '__main__':
    main()

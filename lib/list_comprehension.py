#!/usr/bin/env python3

# squared_minus_one = list()

# for n in range(1,11):
#     squared_minus_one.append((n ** 2)- 1)

# print(squared_minus_one)

# squared_minus_one = [(n ** 2) - 1 for n in range(1, 11)]
# print(squared_minus_one)

def return_evens(num_list):
    even_numbers = [n for n in num_list if n % 2 == 0]
    return even_numbers

    # for n in num_list:
    #     if n % 2 == 0:
    #         return return_evens.append(n)
print(return_evens([0, 1, 3, 5, 7, 8, 9]))


def make_exclamation(sentence_list):
    exclaimed_sentence = [s + "!" for s in sentence_list]
    return exclaimed_sentence


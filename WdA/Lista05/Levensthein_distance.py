import numpy


def levenshtein_distance(token1, token2):
    """Returns the Levenshtein distance between two given strings using dynamic programming"""
    distances = numpy.zeros((len(token1) + 1, len(token2) + 1))

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2

    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if token1[t1 - 1] == token2[t2 - 1]:
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]

                if a <= b and a <= c:
                    distances[t1][t2] = a + 1
                elif b <= a and b <= c:
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1

    # print_distances(distances, len(token1), len(token2))
    return distances[len(token1)][len(token2)]


def print_distances(distances, token1_length, token2_length):
    """Prints the distances array to the console"""
    for t1 in range(token1_length + 1):
        for t2 in range(token2_length + 1):
            print(int(distances[t1][t2]), end=" ")
        print()


def calc_dict_distance(word, num_of_words):
    """Returns the given number of most similar words from the program's dictionary to the one given"""
    file = open('1-1000.txt', 'r')
    lines = file.readlines()
    file.close()
    dict_word_dist = []
    word_id = 0

    for line in lines:
        word_distance = levenshtein_distance(word, line.strip())
        if word_distance >= 10:
            word_distance = 9
        dict_word_dist.append(str(int(word_distance)) + "-" + line.strip())
        word_id = word_id + 1

    closest_words = []
    dict_word_dist.sort()
    # print(dict_word_dist)
    for i in range(num_of_words):
        current_word_dist = dict_word_dist[i]
        word_details = current_word_dist.split("-")
        closest_words.append(word_details[1])
    return closest_words


# print(levenshtein_distance("kelm", "hello"))
phrase = input("Type your word: ")
how_many = int(input("How many words would You like to receive? "))
result = calc_dict_distance(phrase, how_many)
print("\nThe closest words to the one You entered are:")
for word_ in result:
    print(word_)

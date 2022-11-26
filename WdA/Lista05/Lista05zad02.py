frequencyEnglish = {'a': 8.171, 'b': 1.492, 'c': 2.786, 'd': 4.249, 'e': 12.74, 'f': 2.227, 'g': 2.013, 'h': 6.088,
                    'i': 6.962, 'j': 0.153, 'k': 0.772, 'l': 4.021, 'm': 2.404, 'n': 6.746, 'o': 7.506, 'p': 1.928,
                    'q': 0.095, 'r': 5.982, 's': 6.321, 't': 9.048, 'u': 2.759, 'v': 0.978, 'w': 2.359, 'x': 0.151,
                    'y': 1.974, 'z': 0.075}

frequencyGerman = {'a': 7.094, 'b': 1.887, 'c': 2.733, 'd': 5.076, 'e': 16.38, 'f': 1.657, 'g': 3.011, 'h': 4.577,
                   'i': 6.550, 'j': 0.269, 'k': 1.418, 'l': 3.438, 'm': 2.535, 'n': 9.776, 'o': 3.038, 'p': 0.671,
                   'q': 0.018, 'r': 7.003, 's': 7.577, 't': 6.154, 'u': 5.162, 'v': 0.846, 'w': 1.922, 'x': 0.034,
                   'y': 0.039, 'z': 1.135}

frequencyPolish = {'a': 10.07, 'b': 1.511, 'c': 2.559, 'd': 3.308, 'e': 8.914, 'f': 0.329, 'g': 1.455, 'h': 1.118,
                   'i': 8.347, 'j': 2.324, 'k': 3.569, 'l': 3.977, 'm': 2.846, 'n': 5.824, 'o': 8.731, 'p': 3.189,
                   'q': 0.157, 'r': 4.784, 's': 5.079, 't': 4.065, 'u': 2.548, 'v': 0.053, 'w': 4.749, 'x': 0.034,
                   'y': 3.821, 'z': 6.639}


frequencyEnglishVowels = {'a': 8.171, 'e': 12.74, 'i': 6.962, 'o': 7.506, 'u': 2.759, 'y': 1.974}

frequencyGermanVowels = {'a': 7.094, 'e': 16.38, 'i': 6.550, 'o': 3.038, 'u': 5.162, 'y': 0.039}

frequencyPolishVowels = {'a': 10.07, 'e': 8.914, 'i': 8.347, 'o': 8.731, 'u': 2.548, 'y': 3.821}


frequencyEnglishConsonants = {'b': 1.492, 'c': 2.786, 'd': 4.249, 'f': 2.227, 'g': 2.013, 'h': 6.088, 'j': 0.153,
                              'k': 0.772, 'l': 4.021, 'm': 2.404, 'n': 6.746, 'p': 1.928, 'q': 0.095, 'r': 5.982,
                              's': 6.321, 't': 9.048, 'v': 0.978, 'w': 2.359, 'x': 0.151, 'z': 0.075}

frequencyGermanConsonants = {'b': 1.887, 'c': 2.733, 'd': 5.076, 'f': 1.657, 'g': 3.011, 'h': 4.577, 'j': 0.269,
                             'k': 1.418, 'l': 3.438, 'm': 2.535, 'n': 9.776, 'p': 0.671, 'q': 0.018, 'r': 7.003,
                             's': 7.577, 't': 6.154, 'v': 0.846, 'w': 1.922, 'x': 0.034, 'z': 1.135}

frequencyPolishConsonants = {'b': 1.511, 'c': 2.559, 'd': 3.308, 'f': 0.329, 'g': 1.455, 'h': 1.118, 'j': 2.324,
                             'k': 3.569, 'l': 3.977, 'm': 2.846, 'n': 5.824, 'p': 3.189, 'q': 0.157, 'r': 4.784,
                             's': 5.079, 't': 4.065, 'v': 0.053, 'w': 4.749, 'x': 0.034, 'z': 6.639}

diacritical_letters = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z',
                       'ä': 'a', 'ö': 'o', 'ü': 'u', 'ß': 's'}

symbols = """!@#$%^&*()_+1234567890-–=[]\\{}|;':",./<>?`~"""


def count_frequency(text):
    """Counts the percentage distribution of each latin letter in the given sequence, omitting any diacritical marks or
    special characters"""
    frequency = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0,
                 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0,
                 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
                 'y': 0, 'z': 0}
    for i in range(len(text)):
        if text[i] in symbols:
            text = text.replace(text[i], " ")
    text = text.replace(" ", "")
    text = text.lower()
    for i in range(len(text)):
        if text[i] in diacritical_letters.keys():
            text = text.replace(text[i], diacritical_letters[text[i]])
    for letter in text:
        frequency[letter] += (1 / len(text)) * 100
    # print(text)
    # print(frequency)
    # print(sum(frequency.values()))
    return frequency


def choose_language(text, dict_type=""):
    """Based on the percentage frequency of all latin letters/latin vowels/latin consonants returns the statistically
    most accurate language among English, German and Polish"""
    eng_cost = 0
    de_cost = 0
    pl_cost = 0
    dict_ = count_frequency(text)
    match dict_type:
        case "":
            eng_frequency = frequencyEnglish
            de_frequency = frequencyGerman
            pl_frequency = frequencyPolish
        case "vowels":
            eng_frequency = frequencyEnglishVowels
            de_frequency = frequencyGermanVowels
            pl_frequency = frequencyPolishVowels
        case "consonants":
            eng_frequency = frequencyEnglishConsonants
            de_frequency = frequencyGermanConsonants
            pl_frequency = frequencyPolishConsonants
        case _:
            print("Sorry, that was none of the given options.")
            print("Performing the default full match...")
            eng_frequency = frequencyEnglish
            de_frequency = frequencyGerman
            pl_frequency = frequencyPolish

    to_remove = []
    for key in dict_.keys():
        if key not in eng_frequency.keys():
            to_remove.append(key)
    for key in to_remove:
        del dict_[key]

    for key in eng_frequency.keys():
        if dict_[key] != 0:
            eng_cost += (eng_frequency[key] - dict_[key]) ** 2
            de_cost += (de_frequency[key] - dict_[key]) ** 2
            pl_cost += (pl_frequency[key] - dict_[key]) ** 2

    print(dict_)
    if eng_cost == min(eng_cost, de_cost, pl_cost):
        return "English"
    elif de_cost == min(eng_cost, de_cost, pl_cost):
        return "German"
    elif pl_cost == min(eng_cost, de_cost, pl_cost):
        return "Polish"


# count_frequency(input())
entry = input("Write your sentence below:\n")
print("\nWhat type of match would You like to perform?\n\t-For vowels only type \"vowels\",\n"
      "\t-For consonants only type \"consonants\".")
print("If You would like to perform a full match, just press \"Enter\".")
match_type = input()
print(choose_language(entry, match_type))

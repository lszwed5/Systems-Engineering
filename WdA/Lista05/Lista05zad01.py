key_distances = {'q': ['w', 's', 'ś', 'a', 'ą', '1', '!', '2', '@'],
                 'w': ['q', 'e', 'ę', 'd', 's', 'ś', 'a', 'ą', '2', '@', '3', '#'],
                 'e': ['w', 'r', 'f', 'd', 's', 'ś', '3', '#', '4', '$', 'ę'],
                 'r': ['e', 'ę', 't', 'g', 'f', 'd', '4', '$', '5', '%'],
                 't': ['r', 'y', 'f', 'g', 'h', '5', '%', '6', '^'],
                 'y': ['t', 'u', 'g', 'h', 'j', '6', '^', '7', '&'],
                 'u': ['y', 'i', 'k', 'j', 'h', '7', '&', '8', '*'],
                 'i': ['u', 'o', 'ó', 'l', 'ł', 'k', 'j', '8', '*', '9', '('],
                 'o': ['i', 'p', 'l', ';', ':', 'ł', 'k', 'ó'],
                 'p': ['o', 'ó', '[', '{', '\'', '"', ';', ':', 'l', 'ł'],
                 'a': ['q', 'w', 's', 'ś', 'x', 'ź', 'z', 'ż', 'ą'],
                 's': ['q', 'w', 'e', 'ę', 'd', 'c', 'ć', 'x', 'ź', 'z', 'ż', 'a', 'ą'],
                 'd': ['s', 'ś', 'w', 'e', 'ę', 'r', 'f', 'v', 'c', 'ć', 'x', 'ź'],
                 'f': ['d', 'e', 'ę', 'r', 't', 'g', 'b', 'v', 'c', 'ć'],
                 'g': ['f', 'r', 't', 'y', 'h', 'n', 'ń', 'b', 'v'],
                 'h': ['g', 't', 'y', 'u', 'j', 'm', 'n', 'ń', 'b'],
                 'j': ['h', 'y', 'u', 'i', 'k', ',', '<', 'm', 'n', 'ń'],
                 'k': ['j', 'u', 'i', 'o', 'ó', 'l', 'ł', '.', '>', ',', '<', 'm'],
                 'l': ['k', 'i', 'o', 'ó', 'p', ';', ':', '/', '?', '.', '>', ',', '<', 'ł'],
                 'z': ['a', 'ą', 's', 'ś', 'd', 'x', 'ź', 'ż'],
                 'x': ['z', 'ż', 'a', 'ą', 's', 'ś', 'd', 'c', 'ć', 'ź'],
                 'c': ['x', 'ź', 's', 'ś', 'd', 'f', 'v', 'ć'],
                 'v': ['c', 'ć', 'd', 'f', 'g', 'b'],
                 'b': ['v', 'f', 'g', 'h', 'n', 'ń'],
                 'n': ['b', 'g', 'h', 'j', 'm', 'ń'],
                 'm': ['n', 'ń', 'j', 'k', 'l', 'ł', ',', '<']}

diacritical_errors = {'a': 'ą', 'ą': 'a',
                      'c': 'ć', 'ć': 'c',
                      'e': 'ę', 'ę': 'e',
                      'l': 'ł', 'ł': 'l',
                      'n': 'ń', 'ń': 'n',
                      'o': 'ó', 'ó': 'o',
                      's': 'ś', 'ś': 's',
                      'z': ['ź', 'ż'], 'ź': 'z', 'ż': 'z'
                      }

dictionary = ['flota', 'enzym', 'kurczak', 'krab', 'emigrant', 'rosja', 'piknik', 'cel', 'syrena', 'beton',
              'unia', 'ankieta', 'kopiarka', 'cyrk', 'zysk', 'stanik', 'dziennikarz', 'podpis', 'curry', 'przyczepa',
              'termit', 'banan', 'wsparcie', 'waga', 'licencja', 'wybawca', 'piosenka', 'kamyk', 'hazard', 'spadochron',
              'plakat', 'energia', 'bilans', 'wzmacniacz', 'peleryna', 'klakson', 'wojna', 'balkon', 'aluminium',
              'bestia',
              'dziecko', 'planowanie', 'plakat', 'biedronka', 'kominek', 'ranek', 'jaskinia', 'strategia', 'akta',
              'tartan',
              'papier', 'ogon', 'groszek', 'fryzjer', 'higiena', 'szpital', 'region', 'marmur', 'gaz', 'zajazd',
              'egipt', 'mewa', 'kangur', 'krew', 'renifer', 'szminka', 'akwarium', 'cyrk', 'uczta', 'duch',
              'piwnica', 'tron', 'emerytura', 'rana', 'korporacja', 'stokrotka', 'skrzynka', 'telefon', 'parada',
              'oliwka',
              'gruszka', 'bakteria', 'biblia', 'syrena', 'kolana', 'spadochron', 'prawnik', 'wina', 'nerka', 'futro',
              'dym', 'karta', 'okulary', 'maska', 'wdowa', 'klucz', 'tost', 'sterta', 'pineska', 'obrazek']


def vanilla_hamming_distance(str1, str2):
    """Returns the hamming distance between two given strings of the same length. If the length differs, returns None"""
    if len(str1) != len(str2):
        return None
    else:
        dist = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                dist += 1
        return dist


def mod_hamming_distance(str1, str2):
    """Returns the hamming distance between two given strings of the same length, the distance depending on the physical
    distance of keys on the keyboard. If the length differs, returns None"""
    if len(str1) != len(str2):
        return None
    else:
        dist = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                if str1[i] in key_distances.keys():
                    if str2[i] in key_distances[str1[i]]:
                        dist += 1
                    else:
                        dist += 2
        return dist


def dictionary_check(word):
    """Searches for the given word in the program's dictionary. If found, returns OK, otherwise returns up to 3 most
    similar strings from the dictionary"""
    if word in dictionary:
        return "OK"
    else:
        distances = {}
        result = []
        for string in dictionary:
            if len(string) == len(word):
                distances[string] = mod_hamming_distance(string, word)
        for i in sorted(distances, key=distances.get):
            result.append(i)
        return result[:3]


print(vanilla_hamming_distance("mama", "nawa"))
print(mod_hamming_distance("mama", "nawa"))

print(dictionary_check("fryzjer"))
print(dictionary_check("gryzjer"))

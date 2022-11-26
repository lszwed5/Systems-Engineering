# Jeśli ilość sztuk produktu nie jest całkowita, to nie wliczać produktu do ceny całkowitej paragonu
import numpy as np
import math


def check_for_validity(receipt_array, description_array):
    """Checks if there are no major mistakes resulting in inability to compute the two given arrays"""
    receipt_array = np.array(receipt_array)
    description_array = np.array(description_array)
    valid_goods = 0
    for good_id in receipt_array[1]:
        if good_id not in description_array[0]:
            print(f"Błąd: Towaru o numerze id {good_id} nie ma na magazynie")
        else:
            valid_goods += 1
    if valid_goods == len(receipt_array[1]):
        print("Wszystkie numery towarów są poprawne")
    print()

    valid_quantities = 0
    for i in range(len(receipt_array[2])):
        if description_array[2][i] == 1:    # 1 is for countable goods, 0 is for uncountable goods
            if math.floor(receipt_array[2][i]) != receipt_array[2][i]:
                print(f"Błąd: Wprowadzono błędną liczbę towarów o id równym {receipt_array[1][i]} "
                      f"(liczba powinna być liczbą całkowitą. Proszę wprowadzic poprawną liczbę.)")
            else:
                valid_quantities += 1
        else:
            valid_quantities += 1
    if valid_quantities == len(receipt_array[2]):
        print("Wszystkie ilości towarów są poprawne")
    print()


def each_clients_price(receipt_array, description_array, client_id):
    """Calcutes the full receipt's price for a given client"""
    receipt_array = np.array(receipt_array)
    description_array = np.array(description_array)
    price = 0
    client_appearances = 0
    for client_index in range(len(receipt_array[0])):
        if receipt_array[0][client_index] == client_id:
            client_appearances += 1
            for i in range(len(description_array[0])):
                if receipt_array[1][client_index] == description_array[0][i]:
                    price += receipt_array[2][client_index] * description_array[1][i]
    if client_appearances > 0:
        print(f"Cena łączna za paragon osoby {client_id} wynosi {price}")
    else:
        print("Niestety na klienta o takim numerze nie został wystawiony żaden paragon")
    print()


print("---------------------------------------------------------------------------------------------\n")
check_for_validity([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [3, 8, 5, 23, 4]],
                   [[1, 2, 3, 4, 5], [15, 12, 7, 4, 30], [0, 1, 1, 0, 1]])
print("---------------------------------------------------------------------------------------------\n")
each_clients_price([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [3, 8, 3, 23, 4]],
                   [[1, 2, 3, 4, 5], [15, 12, 7, 4, 30], [0, 1, 1, 0, 1]],
                   3)
print("---------------------------------------------------------------------------------------------\n")

from datetime import datetime


class Restauracja:
    """Klasa reprezentująca Restaurację"""

    def __init__(self, nazwa, typ):
        """Metoda inicjalizująca"""
        self.nazwa = nazwa
        self.typ = typ
        self.number_of_clients = 0

    def opis_restauracji(self):
        """Metoda zwracająca opis restauracji"""
        print(f"Nazwa restauracji: {self.nazwa}\n"
              f"Typ serwowanej kuchni: {self.typ}\n"
              f"Liczba obsłużonych klientów: {self.number_of_clients}\n")

    def otwarta_restauracja(self):
        """Metoda informująca, czy restauracja jest aktualnie otwarta"""
        czas = datetime.now()
        if 1 <= czas.isoweekday() <= 4:
            if 8 < czas.hour < 20:
                print("Restauracja jest otwarta\n")
            else:
                print("Restauracja jest zamknięta\n")
        else:
            if 11 < czas.hour < 23:
                print("Restauracja jest otwarta\n")
            else:
                print("Restauracja jest zamknięta\n")

    def ustaw_liczbe_obsluzonych_klientow(self, liczba_obsluzonych_klientow):
        """Metoda pozwalająca ustawić żądaną przez użytkownika ilość obsłużonych klientów"""
        # liczba_obsluzonych_klientow = input("Podaj liczbę obsłużonych klientów: ")
        self.number_of_clients = liczba_obsluzonych_klientow
        print(f"Pomyślnie ustawiono liczbę obsłużonych klientów na {self.number_of_clients}\n")

    def dodaj_liczbe_obsluzonych_klientow(self, increase):
        """Metoda pozwalająca zwiększyć ilość obsłużonych klientów o podaną przez użytkownika liczbę"""
        # increase = input("Podaj liczbę, którą chcesz zwiększyć ilość obsłużonych klientów: ")
        self.number_of_clients += increase
        print(f"Pomyślnie zwiększono liczbę obsłużonych klientów o {increase}.\n"
              f"Liczba obsłuzonych klientów wynosi teraz {self.number_of_clients}\n")


class Lodziarnia(Restauracja):
    """Klasa reprezentująca lodziarnię"""

    def __init__(self, nazwa, typ, *smaki):
        super().__init__(nazwa, typ)
        self.smaki = smaki

    def smaki_lodow(self):
        print("Dostępne smaki lodów to: ")
        for i in self.smaki:
            print(f"\t {i}")


kuk_nuk = Restauracja("Kuk Nuk", "Kuchnia domowa")
matryoshka = Restauracja("Matryoshka", "Kuchnia wschodnia")
radosc = Restauracja("Radość", "Kuchnia indyjska")

print(kuk_nuk.nazwa)
print(radosc.typ)

print()

kuk_nuk.opis_restauracji()
kuk_nuk.otwarta_restauracja()
kuk_nuk.ustaw_liczbe_obsluzonych_klientow(3405)
kuk_nuk.dodaj_liczbe_obsluzonych_klientow(95)

print()

matryoshka.opis_restauracji()
matryoshka.otwarta_restauracja()
matryoshka.ustaw_liczbe_obsluzonych_klientow(2015)
matryoshka.dodaj_liczbe_obsluzonych_klientow(985)

print()

radosc.otwarta_restauracja()
radosc.ustaw_liczbe_obsluzonych_klientow(4517)
radosc.dodaj_liczbe_obsluzonych_klientow(483)
radosc.opis_restauracji()

print()

palce_lizac = Lodziarnia("Palce Lizać", "Lodziarnia", "Truskawkowy", "Czekoladowy", "Waniliowy",
                         "Śmietankowy", "Guma Balonowa")

palce_lizac.number_of_clients = 3500
palce_lizac.opis_restauracji()
palce_lizac.smaki_lodow()

from datetime import datetime
# from time import time

__all__ = ["Uzytkownik", "Admin", "Przywileje"]

class Uzytkownik:
    """Klasa reprezentująca użytkownika"""

    def __init__(self, imie, nazwisko, nick):
        """Metoda inicjalizująca nowy obiekt"""
        self.imie = imie
        self.nazwisko = nazwisko
        self.nick = nick
        self.proby_logowania = 0
        self.ilosc_znajomych = 0
        self.czas_zalozenia_konta = datetime.now()

    def opisz_uzytkownika(self):
        """Wypisuje w konsoli najważniejsze informacje o użytkowniku"""
        print(f"Nick: {self.nick}\n"
              f"Imie: {self.imie}\n"
              f"Nazwisko: {self.nazwisko}\n"
              f"Ilosc nieudanych prob logowania: {self.proby_logowania}\n"
              f"Liczba znajomych: {self.ilosc_znajomych}\n"
              f"Czas od zalozenia konta: {datetime.now() - self.czas_zalozenia_konta}")

    def pozdrow_uzytkownika(self):
        """Wyświetla spersonalizowane powitanie użytkownika"""
        print(f"Witaj {self.imie} {self.nazwisko}, super, że z nami jesteś!\n")

    def dodaj_probe_logowania(self):
        """Zwiększa ilość prób logowania o 1"""
        self.proby_logowania += 1

    def resetuj_proby_logowania(self):
        """Resetuję liczbę prób logowania"""
        self.proby_logowania = 0


class Admin(Uzytkownik):
    """Klasa reprezentująca specjalny rodzaj użytkownika - admina"""

    przywileje = ["Może dodawać posty", "Może usuwać posty", "Może zablokować użytkownika"]

    def __init__(self, imie, nazwisko, nick):
        """Metoda inicjalizująca nowy obiekt klasy Admin"""
        super().__init__(imie, nazwisko, nick)

    def pokaz_przywileje(self):
        print("Przywileje obiektu klasy \"Admin\" to: ")
        for i in Przywileje.przywileje:
            print(f"\t {i}")


class Przywileje:

    przywileje = Admin.przywileje

    def pokaz_przywileje(self):
        print("Przywileje obiektu klasy \"Admin\" to: ")
        for i in self.przywileje:
            print(f"\t {i}")


gosc1 = Uzytkownik("Brajanek", "Kowalski", "gosc1")
gosc2 = Uzytkownik("Seba", "Nowak", "gosc2")
adam1234 = Uzytkownik("Adam", "Glaglak", "adam1234")
zeeenooon = Uzytkownik("Zenon", "Ziembiewicz", "zeeenooon")
krycha525 = Uzytkownik("Krystian", "Wojnar", "krycha525")

admin1 = Admin("Lukasz", "Szwed", "admin1")

lista_przywilejow = Przywileje()


gosc1.opisz_uzytkownika()
# sleep(5)
gosc1.pozdrow_uzytkownika()

zeeenooon.dodaj_probe_logowania()

lista_przywilejow.pokaz_przywileje()

print()

admin1.pokaz_przywileje()

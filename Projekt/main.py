ASCII_MENU = """
    === BIBLIOTEKA ===
1) Dodaj ksiązke
2) Wypozycz ksiazke
3) Oddaj ksiazke
4) Sprawdz historie ksiazki
5) Wyjdź
"""


class Ksiazka:
    def __init__(self, tytul, autor, rokWydania, indeksKsiazki) -> None:
        self.tytul: str = tytul
        self.autor: str = autor
        self.rokWydania: int = rokWydania
        self.indeksKsiazki: int = indeksKsiazki


class Czytacz:
    def __init__(self, indeksCzytacza: int, imie: str, nazwisko: str) -> None:
        self.indeksCzytacza: int = indeksCzytacza
        self.imie: str = imie
        self.nazwisko: str = nazwisko
        self.wypozyczoneKsiazki: list[Ksiazka] = []


class Biblioteka:
    def __init__(self) -> None:
        self.iloscKsiazek: int = 0
        self.ksiazki: list[Ksiazka] = []
        self.czytacze: list[Czytacz] = []
        self.wypozyczoneKsiazki: list[Ksiazka] = []

    def dodajKsiazke(self) -> None:
        tytul = input("Podaj tytuł: ")
        autor = input("Podaj autora: ")
        rokWydania = input("Podaj rok wydania: ")
        self.ksiazki.append(
            Ksiazka(tytul, autor, rokWydania, self.iloscKsiazek+1))

    def wypozyczKsiazke(self):
        self.znajdzPoTytuleLubIndeksie(self)
        indeksCzytacza = int(input("numer czytacza"))
        imie = input("imię")
        nazwisko = input("nazwisko")
        self.znajdzCzytacza(indeksCzytacza)
        dataWypozyczenia = input("data wypozyczenia")

    def oddajKsiazke(self):
        self.znajdzPoTytuleLubIndeksie(self)
        dataOddania = input("Podaj datę oddania: ")

    def podejrzyjHistorieKsiazki(self):
        self.znajdzPoTytuleLubIndeksie(self)

    def znajdzCzytacza(self, indeks) -> Czytacz:
        for cz in self.czytacze:
            if (cz.indeksCzytacza == indeks):
                return cz
        raise ValueError("Wybrano nie istniejącą opcję w menu")

    def znajdzPoTytuleLubIndeksie(self) -> Ksiazka:
        tytulCzyIndeks = int(input("""Chcesz znaleźć ksiązke po tytule czy indeksie?
            1) Tytuł
            2) Indeks"""))
        if (tytulCzyIndeks == 1):
            tytul = input("Podaj tytul ksiazki")
            for ksiazka in self.ksiazki:
                if (ksiazka.tytul == tytul):
                    return ksiazka
        elif (tytulCzyIndeks == 2):
            indeks = input("Podaj indeks ksiazki")
            for ksiazka in self.ksiazki:
                if (ksiazka.indeksKsiazki == indeks):
                    return ksiazka
        else:
            raise ValueError("Wybrano nie istniejącą opcję w menu")


if __name__ == "__main__":
    biblioteka = Biblioteka()
    while True:
        menuWybor = input(ASCII_MENU)
        if (menuWybor == '1'):
            biblioteka.dodajKsiazke()
        elif (menuWybor == '2'):
            biblioteka.wypozyczKsiazke()
        elif (menuWybor == '3'):
            biblioteka.oddajKsiazke()
        elif (menuWybor == '4'):
            biblioteka.podejrzyjHistorieKsiazki()
        elif (menuWybor == '5'):
            print(f"Zamykanie programu...")
            break
        else:
            raise ValueError("Wybrano nie istniejącą opcję w menu")
    SystemExit(0)

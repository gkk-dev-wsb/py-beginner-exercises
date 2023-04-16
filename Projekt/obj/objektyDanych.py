from dataclasses import dataclass


@dataclass
class Ksiazka:
    tytul: str
    autor: str
    rokWydania: int
    indeksKsiazki: int
    status: str

    def __str__(self):
        return (f"tytul: {self.tytul}"
                f"autor: {self.autor}"
                f"rokWydania: {self.rokWydania}"
                f"indeksKsiazki: {self.indeksKsiazki}"
                f"status: {self.status}")


class Czytacz:
    def __init__(self, indeksCzytacza: int, imie: str, nazwisko: str) -> None:
        self.indeksCzytacza: int = indeksCzytacza
        self.imie: str = imie
        self.nazwisko: str = nazwisko
        self.wypozyczoneKsiazki: list[Ksiazka] = []

    @property
    def iloscWypozyczonychKsiazek(self):
        return len(self.wypozyczoneKsiazki)

    def __str__(self):
        return (f"indeksCzytacza: {self.indeksCzytacza}"
                f"imie: {self.imie}"
                f"nazwisko: {self.nazwisko}"
                f"wypozyczoneKsiazki: {self.wypozyczoneKsiazki}")

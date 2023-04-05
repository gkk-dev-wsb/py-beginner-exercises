from obj.KsiazkaObj import Ksiazka


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

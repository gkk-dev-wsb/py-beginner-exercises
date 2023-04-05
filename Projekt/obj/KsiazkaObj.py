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

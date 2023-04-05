
class Ksiazka:
    def __init__(self, tytul, autor, rokWydania, indeksKsiazki, status) -> None:
        self.tytul: str = tytul
        self.autor: str = autor
        self.rokWydania: int = rokWydania
        self.indeksKsiazki: int = indeksKsiazki
        self.status: str = status

    def __str__(self):
        return (f"tytul: {self.tytul}"
                f"autor: {self.autor}"
                f"rokWydania: {self.rokWydania}"
                f"indeksKsiazki: {self.indeksKsiazki}"
                f"status: {self.status}")

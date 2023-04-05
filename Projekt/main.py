from obj.BibliotekaObj import Biblioteka
import utils.constants as c
import utils.db as db


if __name__ == "__main__":
    db.inicjujDane()
    biblioteka = Biblioteka()
    biblioteka.ladujBiblioteke()
    while True:
        menuWybor = input(c.ASCII_MENU)
        if (menuWybor == '1'):
            biblioteka.dodajKsiazke()
        elif (menuWybor == '2'):
            biblioteka.wypozyczKsiazke()
        elif (menuWybor == '3'):
            biblioteka.oddajKsiazke()
        elif (menuWybor == '4'):
            biblioteka.podejrzyjHistorieKsiazki()
        elif (menuWybor == '5'):
            biblioteka.dodajCzytacza()
        elif (menuWybor == '6'):
            print(f"Zamykanie programu...")
            break
        else:
            print("Wybrano nie istniejącą opcję w menu...")
    SystemExit(0)

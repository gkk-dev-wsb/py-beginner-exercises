import sys
from obj.BibliotekaObj import Biblioteka
import utils.constants as c
import utils.db as db
import utils.utils as u

TEST_MODE = False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            TEST_MODE = True
            print("Uruchomiono w trybie testowym...")
    db.inicjujDane()
    biblioteka = Biblioteka(TEST_MODE)
    biblioteka.ladujBiblioteke()
    while True:
        menuWybor = u.cleanInput(input(c.ASCII_MENU), testMode=TEST_MODE)
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

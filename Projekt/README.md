# Biblioteka CLI

Projekt zaliczeniowy na Programowanie obiektowe.

## Uruchomienie

Zgodnie z poleceniem należy uruchomić program z argumentami:

```python3
pip3 install -r requirements.txt
python3 main.py
```

a potem wybrać opcję 1, 2, 3, 4.
Zmodyfikowano opcję 5 - zamiast kończyć program, pozwala na dodanie nowego
czytelnika głównego.

6 - kończy program.

## Testowanie

Wszystkie testy mozna wlaczyc komenda:

```python3
pytest tests/
```

Dołączony plik `.vscode/settings.json` powinine pozwolić na automatyczne
zaczytanie się testów do zakładki testy VS Code, pozwalając potwierdzić
działanie ich odpalając je lokalnie w dowolnej konfiguracji.

### E2E

Dla przetestowania działania programu należy uruchomić testy End to End z pliku `tests/test_E2E.py`.
Uruchamiają one program w trybie automatycznym - input przekazany PIPEm jest powtarzny w konsoli.

Testy weryfikują, ze powstale pliki bazy danych są zgodne z oczekiwaniami.

### Unit

Unit testy znajdują się w pliku `test_unit.py`

```python3
python3 tests/test_unit.py
```

## Wymagania projektu Programowanie Obiektowe w Języku Python

### Ogólne wymagania

- Użycie klas
- DRY (Don't Repeat Yourself)
- Hermetyzację
- Kreatywną obsługę błędów
- Dodanie dziedziczenia
Kod powinien być czysty i czytelny oraz napisany w języku polskim (metody i
funkcje mogą być w języku angielskim, ale preferowany jest język polski).

### Biblioteka

#### Ogólne

Wszystkie polskie znaki muszą być zamienione na analogiczne litery łacińskie.

Daty oddania nie mogą być wcześniejsze niż daty wypożyczenia, a data
wypożyczenia nie może być wcześniejsza niż data ostatniego oddania.
Oczywiście daty nie mogą być wcześniejsze niż rok wydania książki.

Dwa różni ludzie nie mogą mieć tego samego numeru lub nazywać się tak samo.
Bibliotekarka poprosi o ponowne podanie wszystkich trzech danych w razie
problemów i powie, które z nich było nieprawidłowe. Wyjście z programu w
sposób normalny powinno zagwarantować zapisanie obu plików i umożliwić
kontynuowanie pracy programu od tego samego punktu (wczytanie plików do bazy).

Zakończenie każdej opcji (z wyjątkiem opcji 5) powinno zostać potwierdzone i
natychmiast przekierować użytkownika do punktu wyjścia.

Przykładowe dane wejściowe
Wpisując odpowiednio hasła:

1, 451 stopni Fahrenheita, Ray Bradbury, 1953, 2, 1, 1, Janusz, Kowalski, 21/2/2002, 3, 1, 22/2/2002, 2, 1, 2, Michał, Michal, Staszewski, 21/2/2002, 23/2/2002, 2, 1, 3, Jadwiga, Mroczek, 3, 451 stopni Fahrenheita, 23/3/2005, 1, Zmierzch, Stephenie Meyer, 2005, 2, 1, 4, Paulina, Borsuk, 1/4/2010

[Powinniśmy otrzymać zawartość plików pokazaną na załączonych zrzutach ekranu.]((./img/screenshot.png))

#### Implementacja

##### Po kliknięciu 1

Po wybraniu opcji 1, zostajemy przywitani przez bibliotekarkę w konsoli,
która proponuje kilka opcji. Kliknięcie opcji 1 pozwala nam dodać książkę do
biblioteki. Musimy podać:

- Tytuł
- Autora
- Rok wydania
wszystko jako osobne inputy w konsoli. Książka otrzymuje status "W bibliotece"
i zostaje przypisany do niej najmniejszy dostępny numer indeksu.

##### Po kliknięciu 2

Po wybraniu opcji 2, możemy wypożyczyć książkę z biblioteki. Musimy podać:

- Tytuł lub numer indeksu książki
- Numer czytelnika
- Imię
- Nazwisko
- Datę wypożyczenia
wszystko jako osobne inputy w konsoli. Jeśli jest wiele kopii tej samej książki,
zostanie wybrana ta z najmniejszym numerem indeksu. Wypożyczona książka
otrzymuje status "Nie w bibliotece" i nie może być wypożyczona przez innego
czytelnika. Wypożyczający zwiększa ilość posiadanych przez niego książek.

##### Po kliknięciu 3

Po wybraniu opcji 3, możemy oddać książkę do biblioteki. Wystarczy podać:

- Numer indeksu lub tytuł książki
- Jeśli więcej niż jedna taka sama książka została wypożyczona, bibliotekarka
musi zapytać o numer indeksu
- Następnie jest pytanie o datę
Książka zostaje zwrócona, a ilość książek posiadanych przez czytelnika zostaje
zmniejszona.

##### Po kliknięciu 4

Po wybraniu opcji 4, możemy podejrzeć historię wypożyczeń książki. Podobnie jak
w punkcie 3, musimy wybrać książkę, a następnie zostaną wyświetlone wszystkie
informacje na temat wypożyczeń:

- Ilość udanych i nieudanych wypożyczeń wraz z datami i numerami osób
wypożyczających
Jeśli książka nie jest dostępna, bibliotekarka poinformuje nas o tym na końcu.

##### Kliknięcie 5 kończy program

Kliknięcie opcji 5 kończy program.

##### Logi

Wszystkie interakcje muszą zostać zapisane w pliku historia.csv, nawet jeśli
były nieudane. Kolumny w pliku biblioteka.csv powinny nazywać się następująco:

- ID
- Tytuł
- Autor
- Rok wydania
- Status
Kolumny w pliku historia.csv powinny wyglądać następująco:

- ID
- Numer czytelnika
- Czy wypożyczenie było udane
- Data wypożyczenia
- Data oddania
Kolumny w pliku czytelnicy.csv powinny wyglądać następująco:

- Numer czytelnika
- Imię
- Nazwisko
- Ilość książek

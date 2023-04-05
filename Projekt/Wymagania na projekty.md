# Wymagana projektu OOP

## General

Do wybrania jest jeden z 3 projetków.
Wymagania ogólne:

- Klasowość
- DRY
- hermetyzacja
- kreatywna obsługa błędów.
- Dodać dziedziczenie.

Kod czysty, czytelny, pisany w języku polskim
(przynajmniej metody i funkcje, zmienne wybaczę).

## Biblioteka

### Po kliknięciu 1

Biblioteka. Wita nas konsola bibliotekarka, która daje nam parę opcji.
Po kliknięciu 1 możemy dodać książkę do biblioteki.
Następnie musimy podać:

- tytuł
- autora
- rok wydania

wszystko jako osobne inputy w konsoli. Książka zyskuje status "W bibliotece".
Książka dostaje najmniejszy dostępny numer indeksu.

### Po kliknięciu 2

Po kliknięciu 2 możemy wypożyczyć książkę z biblioteki. Podać wtedy musimy:

- tytuł lub numer indeksu książki,
- numer czytacza
- imię,
- nazwisko i
- data wypozyczenia
  wszystko jako osobne inputy w konsoli. Jeżeli jest wiele powtórzeń książki,
  wybrana zostanie ta z najmniejszym indeksem. Książka ta otrzymuje wtedy status
  "Nie w bibliotece" i nie może zostać wypożyczona przez użytkownika, lecz próby
  muszą zostać zapisane do histori biblioteki. Wypożyczającemu zwiększa się ilość
  posiadanych przez niego książek.

### Po kliknięciu 3

Po kliknięciu 3 możemy oddać książkę do biblioteki. Wystarczy podać:

- numer indeksu, lub tytuł książki
  lecz jeżeli więcej, niż jeden taki sam tytuł został wypożyczony, bibliotekarka i
  tak musi zapytać o numer indeksu. Następnie jest zapytanie o datę. Książka
  zostaje zwrócona. Ilośc książek posiadanych przez czytacza dekrementuje się.

### Po kliknięciu 4

Po kliknięciu 4 możemy podejrzeć historię książki. Wybór książki jak
w punkcie 3, po czym wyświetlają nam się wszystkie informacje o książce:

- ilość udanych i nieudanych wypożyczeń wraz z datami i numerami osób
  wypożyczających.

Jeżeli książka nie jest dostępna, bibliotekarka opowie nam o tym na końcu
wypowiedzi.

### Kliknięcie 5 kończy program

Kliknięcie 5 kończy program.

### Logs

Wszystkie interakcje muszą być zapisane w pliku historia.csv nawet jeżeli były
nieudane. Kolumny w pliku biblioteka.csv powinny nazywać się następująco:

- ID,
- Tytul,
- Autor,
- Rok wydania,
- Status.

Kolumny w pliku historia.csv powinny wyglądać następująco:

- ID,
- Numer czytacza,
- Czy udana,
- Data wypozyczenia,
- Data oddania.

Kolumny w pliku czytacze.csv powinny wyglądać następująco:

- Numer czytacza,
- Imie,
- Nazwisko,
- Ilosc ksiazek.

### Wymagania

Odrzucenie polskich znaków w każdej formie, bibliotekarka poprosi o powtórzenie tego samego bez polskich znaków.

Daty oddania nie mogą być wcześniejsze, niż daty wypożyczenia i data
wypożyczenia nie może być wcześniejsza, niż data ostatniego oddania. Oczywiście
też daty nie mogą być wcześniejsze, niż rok wydania książki.

Dwóch ludzi nie może mieć tego samego numeru lub nazywać się tak samo,
bibliotekarka poprosi o powtórzenie wszystkich trzech danych w razie problemów
i powie, która była zła. Wyłączenie programu normalną metodą powinno
zagwarantować zapisanie obu plików oraz pozwolić na rozpoczęcie pracy programu
na tym samym etapie (wczytanie plików do bazy).

Zakończenie któregokolwiek z punktów(poza 5) powinno zostać potwierdzone i od razu przekierować do miejsca z powitaniem.

### Input examples

Wpisanie odpowiednio haseł :
1, 451 stopni Fahrenheita, Ray Bradbury, 1953, 2, 1, 1, Janusz, Kowalski, 21/2/2002, 3, 1, 22/2/2002, 2, 1, 2, Michał, Michal, Staszewski, 21/2/2002, 23/2/2002, 2, 1, 3, Jadwiga, Mroczek, 3, 451 stopni Fahrenheita, 23/3/2005, 1, Zmierzch, Stephenie Meyer, 2005, 2, 1, 4, Paulina, Borsuk, 1/4/2010
Powinniśmy otrzymać zawartość plików pokazaną w załączonych screenshotach

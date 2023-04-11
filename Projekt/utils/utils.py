from datetime import datetime, date


def date_to_str(objekt_daty: date, date_format='%Y-%m-%d'):
    """
    Konwertuje obiekt datetime.date na string.
    
    Args:
    data_obj: obiekt datetime.date
    format_daty: str, format zwracanej daty
    
    Returns:
    str, data w formacie string
    """
    return datetime.strftime(objekt_daty, date_format)

def waliduj_date_z_wejscia(lancuch_daty, format_daty='%Y-%m-%d'):
    """
    Waliduje i zwraca string z datą z wejścia użytkownika, konwertując ją na
    obiekt daty.
    
    Args:
    lancuch_daty: str, string daty wprowadzony przez użytkownika
    format_daty: str, format, w jakim funkcja odczytuje datę
    
    Returns:
    obiekt datetime.date, jeśli dane wejściowe są poprawne, w przeciwnym razie None
    """
    return datetime.strptime(lancuch_daty, format_daty).date()

def czyscWejscie(wejscie:str, trybTestowania=False):
    """
    Funkcja czyszczenia łańcucha znaków przez zastępowanie polskich znaków ich
    odpowiednikami łacińskimi przy użyciu metod str.maketrans() i str.translate().

    Args:
    wejscie (str): Łańcuch znaków do wyczyszczenia.
    trybTestowania (bool, opcjonalnie): Jeśli ustawione na True, drukuje łańcuch
    wejściowy przed i po wyczyszczeniu. Domyślnie False.

    Returns:
    str: Wyczyszczony łańcuch znaków, w którym wszystkie polskie znaki zostały
    zastąpione przez ich odpowiedniki łacińskie.
"""

    polskie_na_lacinskie = str.maketrans('ąćęłńóśźżĄĆĘŁŃÓŚŹŻ', 'acelnoszzACELNOSZZ')
    wyjscie = wejscie.translate(polskie_na_lacinskie)
    if trybTestowania:
        print("$: ", wejscie)
    return wyjscie

from datetime import datetime


def date_to_str(date_obj, date_format='%Y-%m-%d'):
    """
    Converts datetime.date object to string.
    :param date_obj: datetime.date object
    :param date_format: str, format in which function returns date
    :return: str, date in string format
    """
    date_string = datetime.strftime(date_obj, date_format)
    return date_string


def str_to_date(date_string, date_format='%Y-%m-%d'):
    """
    Converts string to datetime.date object.
    :param date_string: str, date in string format
    :param date_format: str, format in which function reads date
    :return: datetime.date object
    """
    date_obj = datetime.strptime(date_string, date_format).date()
    return date_obj


def validate_date_input(date_string, date_format='%Y-%m-%d'):
    """
    Validates and returns converted to date object string from user input.
    :param date_string: str, user input date string
    :param date_format: str, format in which function reads date
    :return: datetime.date object if input is valid, None otherwise
    """
    return datetime.strptime(date_string, date_format).date()


def cleanInput(input_str, testMode=False):
    """
This function cleans the input string by replacing Polish characters with their Latin equivalents using str.maketrans() and str.translate() methods.

Args:
input_str (str): The input string to be cleaned.
testMode (bool, optional): If set to True, prints the input string before and after cleaning. Defaults to False.

Returns:
str: The cleaned string with all Polish characters replaced by their Latin equivalents.
"""
    polish_to_latin = str.maketrans('ąćęłńóśźżĄĆĘŁŃÓŚŹŻ', 'acelnoszzACELNOSZZ')
    output_str = input_str.translate(polish_to_latin)
    if testMode:
        print("$: ", input_str)
    return output_str

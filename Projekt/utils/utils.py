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
    try:
        date_obj = datetime.strptime(date_string, date_format).date()
        return date_obj
    except ValueError:
        return None


def cleanInput(input_str):
    """
    Removes Polish characters from a string and replaces them with their closest Latin analogs.

    Args:
        input_str (str): The input string with Polish characters.

    Returns:
        str: The output string with Polish characters replaced with their Latin analogs.
    """
    polish_to_latin = str.maketrans('ąćęłńóśźżĄĆĘŁŃÓŚŹŻ', 'acelnoszzACELNOSZZ')
    output_str = input_str.translate(polish_to_latin)
    return output_str

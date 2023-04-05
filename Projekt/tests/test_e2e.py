import subprocess
import shutil
import os


def _remove_pycache_directories(directory):
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            if dir == '__pycache__':
                dir_path = os.path.join(root, dir)
                print(f'Removing directory {dir_path}')
                try:
                    shutil.rmtree(dir_path)
                except OSError as e:
                    print(f'Error deleting {dir_path}: {e}')


def teardown():
    _remove_pycache_directories('.')
    shutil.rmtree("data")


def test_main():

    # Set up test data
    TEST_INPUT_STRINGS = b'\n'

    # Add book 1
    for i in [b'1\n', b'451 Stopni Fahrenheita\n', b'Ray Bradbury\n', b'1953\n']:
        TEST_INPUT_STRINGS += i

    # Add book 2
    for i in [b'1\n', b'Zmierzch\n', b'Stephenie Meyer\n', b'2005\n']:
        TEST_INPUT_STRINGS += i

    # Add czytacze
    for cz in [[b'Janusz\n', b'Kowalski\n'], [b'Michal\n', b'Staszewski\n'],
               [b'Jadwiga\n', b'Mroczek\n'], [b'Paulina\n', b'Borsuk\n']]:
        for i in [b'5\n', cz[0], cz[1]]:
            TEST_INPUT_STRINGS += i

    # # Wypozycz ksiazke
    for i in [b'2\n', b'2\n', b'1\n', b'1\n', b'Janusz\n', b'Kowalski\n', b'2002-02-21\n',
              b'3\n', b'2\n', b'1\n', b'2002-02-22\n', b'1\n',
              b'2\n', b'1\n', b'451 Stopni Fahrenheita\n', b'2\n', b'Michal\n', b'Staszewski\n', b'2002-02-23\n',
              b'3\n', b'1\n', b'451 Stopni Fahrenheita\n', b'2005-02-23\n', b'2\n',
              b'2\n', b'2\n', b'1\n', b'3\n', '\n'  # Testcase where czytacz data is incorrect
              b'2\n', b'2\n', b'1\n', b'4\n', b'Paulina\n', b'Borsuk\n', b'2010-04-01\n']:
        TEST_INPUT_STRINGS += i
    process = subprocess.Popen(['python3', 'main.py', 'test'],
                               stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    try:
        # Provide the user input programmatically using the communicate() method
        output, error = process.communicate(
            input=TEST_INPUT_STRINGS)
        print(output.decode('utf-8'))
    except Exception as e:
        print(f'Error: {e}')


def test_data_folder():
    data_folder = "data"
    files = ["biblioteka.csv", "czytacze.csv", "historia.csv"]

    for file in files:
        assert os.path.isfile(os.path.join(data_folder, file))


def test_biblioteka_csv():
    with open('data/biblioteka.csv', 'r') as f:
        content = f.read().strip()
    expected_content = """ID,Tytul,Autor,Rok wydania,Status
1,451 Stopni Fahrenheita,Ray Bradbury,1953-01-01,Nie w bibliotece
2,Zmierzch,Stephenie Meyer,2005-01-01,W bibliotece"""
    assert content == expected_content, f"Expected '{expected_content}', but got '{content}'"


def test_historia_csv():
    with open('data/historia.csv', 'r') as f:
        content = f.read().strip()
    expected_content = """ID,Numer czytacza,Czy udana,Data wypozczenia,Data oddania
0,1,False,2002-02-21,2002-02-22
0,2,False,2002-02-23,2005-02-23
,3,False,,
0,4,True,2010-04-01,0"""
    assert content == expected_content, f"Expected '{expected_content}', but got '{content}'"


def test_czytacze_csv():
    with open('data/czytacze.csv', 'r') as f:
        content = f.read().strip()
    expected_content = """Numer czytacza,Imie,Nazwisko,llosc ksiazek
1,Janusz,Kowalski,0
2,Michal,Staszewski,0
3,Jadwiga,Mroczek,0
4,Paulina,Borsuk,1"""
    assert content == expected_content, f"Expected '{expected_content}', but got '{content}'"

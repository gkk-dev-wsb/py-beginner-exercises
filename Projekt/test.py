import subprocess
from time import sleep

# Run the CLI app using subprocess
process = subprocess.Popen(['python3', 'main.py'],
                           stdin=subprocess.PIPE, stdout=subprocess.PIPE)
try:
    # Provide the user input programmatically using the communicate() method
    output, error = process.communicate(
        input=b'1\n451 Stopni Fahrenheita\nRay Bradbury\n1953\n')
    # Print the output from the CLI app
    print(output.decode('utf-8'))
except Exception as e:
    # Print the error message
    print(f"Error: {e}")

# Add book 1
# for i in [b'1\n', b'451 Stopni Fahrenheita\n', "Ray Bradbury\n", "1953\n"]:
#     process.stdin.write(i)
#     output = process.communicate()[0]

# # Add book 2
# for i in [b'1\n', b"Zmierzch\n", b"Stephenie Meyer\n", b"2005\n"]:
#     process.stdin.write(i)
#     output = process.communicate()[0]

# # Add czytacze
# for cz in [[b"Janusz\n", b"Kowalski\n"], [b"Michal\n", b"Staszewski\n"],
#            [b"Jadwiga\n", b"Mroczek\n"], [b"Paulina\n", b"Borsuk\n"]]:
#     for i in [b'5\n', cz[0], cz[1]]:
#         process.stdin.write(i)
#         output = process.communicate()[0]

# # Wypozycz ksiazke
# for i in [b'2\n', b'2\n', b'1\n', b'1\n', b'Janusz\n', b'Kowalski\n', b'2002-02-21\n',
#           b'3\n', b'2\n', b'1\n', b'2002-02-22\n', b'1\n',
#           b'2\n', b'1\n', b'451 Stopni Fahrenheita\n', b'2\n', b"Michal\n", b"Staszewski\n", b"2002-02-23\n",
#           b'3\n', b'1\n', b'451 Stopni Fahrenheita\n', b"2005-02-23\n", b'2\n',
#           b'2\n', b'\n',  # Should be: NumerCzytacza, czyUdana
#           b'2\n', b'2\n', b'1\n', b'4\n', b"Paulina\n", b"Borsuk\n", b"2010-04-01\n"]:
#     process.stdin.write(i)
#     output = process.communicate()[0]

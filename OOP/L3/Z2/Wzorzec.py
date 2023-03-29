# Wzorzec 2: Polecenie
#
# Polecenie to wzorzec projektowy, który pozwala na enkapsulację żądania jako
# obiekt. Dzięki temu można parametryzować obiekty na podstawie żądań, kolejek,
# logów operacji i można je także cofać.
# Przykład: Prosty system sterowania odtwarzaczem

from abc import ABC, abstractmethod


class Command(ABC):
    """Interfejs polecenia"""
    @abstractmethod
    def execute(self):
        pass


class PlayCommand(Command):
    """Polecenie 1: Odtwarzanie"""

    def __init__(self, player):
        self.player = player

    def execute(self):
        self.player.play()


class StopCommand(Command):
    """Polecenie 2: Zatrzymanie"""

    def __init__(self, player):
        self.player = player

    def execute(self):
        self.player.stop()


class MusicPlayer:
    """Odbiorca"""

    def play(self):
        print("Granie muzyki...")

    def stop(self):
        print("Zatrzymywanie muzyki...")


class RemoteControl:
    """Wywołujący"""

    def __init__(self, command: Command):
        self.command = command

    def press_button(self):
        self.command.execute()


# Przykład użycia
if __name__ == '__main__':
    player = MusicPlayer()

    play_command = PlayCommand(player)
    stop_command = StopCommand(player)

    remote = RemoteControl(play_command)
    remote.press_button()

    remote = RemoteControl(stop_command)
    remote.press_button()

    for cmd in [play_command, stop_command, play_command, stop_command, play_command]:
        RemoteControl(cmd).press_button()

from entities.song import Song
from entities.listener import Listener
from services.service_listener import ServiceListener
from services.service_song import ServiceSong
from services.statistics_services import StatisticsServices


class ConsoleUi:

    def __init__(self, service_song: ServiceSong, service_listener: ServiceListener,
                 service_statistics: StatisticsServices):
        self.service_song = service_song
        self.service_listener = service_listener
        self.__service_statistics = service_statistics
        self.options = {
            1: self.__add_song,
            2: self.__delete_song,
            3: self.__update_song,
            4: self.service_song.print_songs,
            5: self.__average_duration,
            6: self.__most_popular_artist,
            7: self.service_listener.print_listeners,
            8: self.__add_listener,
            9: self.__update_listener,
            10: self.__delete_listener,
            11: self.__average_age,
            12: self.__unlistened_songs,
            13: self.exit_app
        }

    @staticmethod
    def __print_menu():
        print("Optiuniile pe care le aveti:")
        print("1. Adaugati o melodie in playlist")
        print("2. Stergeti o melodie din playlist")
        print("3. Actualizati datele unei melodii din playlist")
        print("4. Vedeti toate melodiile din playlist")
        print("5. Vedeti durata medie a melodiilor din playlist")
        print("6. Vedeti care este cel mai popular artist din playlist\n")
        print("7. Vedeti toti ascultatorii playlist-ului")
        print("8. Adaugati noi ascultatori")
        print("9. Actualizati datele unui ascultator")
        print("10. Stergeti un ascultator")
        print("11. Vedeti varsta medie a ascultatoriilor")
        print("12. Meloddiile neascultate de nimeni")
        print("13. Iesi din aplicatie")

    def __user_choice(self):

        while True:
            try:
                choice = int(input("Alegerea ta: "))
                if choice < 1 or choice > 13:
                    raise ValueError
                break

            except ValueError:
                print("Valoarea introdusa nu este ok.")
            except():
                print("A aparut o eroare.")

        self.options[choice]()

    def __add_song(self):
        print(self.service_song.add_songs(self.__get_song()))

    def __add_listener(self):
        print(self.service_listener.add_listener(self.__get_listener()))

    def __get_song(self):
        name = input("Nume melodie: ")
        artist = input("Artist melodie: ")
        genre = input("Gen melodie: ")
        while True:
            try:
                duration = int(input("Durata in secunde: "))
                break
            except ValueError:
                print("Introduceti un numar")

        return Song(name, artist, genre, duration)

    def __get_listener(self):
        name = input("Nume: ")
        while True:
            try:
                age = int(input("Varsta: "))
                if age < 0:
                    raise ValueError
                break
            except ValueError:
                print("Varsta este invalida")

        return Listener(name, age, self.__get_song())

    def __get_id_song(self):
        while True:
            try:
                id_song = int(input("Id:"))
                if not (id_song in [song.id for song in self.service_song.repo_song.songs]):
                    raise ValueError
                break
            except ValueError:
                print("ID este inexistent.")

        return id_song

    def __get_id_listener(self):
        while True:
            try:
                id_listener = int(input("Id:"))
                if not (id_listener in [listener.id for listener in self.service_listener.repo_listener.listeners]):
                    raise ValueError
                break
            except ValueError:
                print("ID este inexistent.")

        return id_listener

    def __delete_song(self):
        self.service_song.print_songs()
        print(self.service_song.delete_songs(self.__get_id_song()))

    def __delete_listener(self):
        self.service_listener.print_listeners()
        print(self.service_listener.delete_listeners(self.__get_id_listener()))

    def run(self):
        while True:
            self.__print_menu()
            self.__user_choice()

    def __update_song(self):
        print(self.service_song.update_songs(self.__get_id_song(), self.__get_song()))

    def __update_listener(self):
        print(self.service_listener.update_listeners(self.__get_id_listener(), self.__get_listener()))

    def __average_duration(self):
        print("Durata medie este de: " + str(self.__service_statistics.average_duration_songs()) + " secunde")

    def __most_popular_artist(self):
        print("Cel mai popular artist este: " + self.__service_statistics.most_popular_artist_playlist())

    def __average_age(self):
        print("Varsta medie este de: " + str(self.__service_statistics.average_age_listeners()) + " ani")

    def __unlistened_songs(self):
        print("Melodiile neasculatate de nimeni sunt: ")
        for song in self.__service_statistics.unlistened_songs():
            print(repr(song))

    def exit_app(self):
        self.service_song.repo_song.write_to_file()
        self.service_listener.repo_listener.write_to_file()
        exit(0)

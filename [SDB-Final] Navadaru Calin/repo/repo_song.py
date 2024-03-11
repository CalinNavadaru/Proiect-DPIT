import os

from entities.song import Song


class RepoSong:
    def __init__(self):
        self.songs = []
        self.__read_from_file()

    def __read_from_file(self):
        file = open("songs.txt", "r")

        if os.stat("songs.txt").st_size == 0:
            raise EOFError

        while True:
            try:
                line = file.readline().split(",")
                line[3] = int(line[3])
                self.add_song(Song(*line))
                if os.stat("songs.txt").st_size == 0 or len(line) == 0:
                    raise EOFError

            except(IndexError, EOFError):
                break

    def write_to_file(self):
        file = open("songs.txt", "w")

        for song in self.songs:
            song_details = song.name + ',' + song.artist + ',' + song.genre + ',' + str(song.length)
            file.write(song_details)
            file.write("\n")

    def add_song(self, new_song: Song):
        if not (new_song in self.songs):
            self.songs.append(new_song)
            return "\nMelodia a fost adaugata"

        return "\nMelodia exista deja"

    def print_songs(self):
        for song in self.songs:
            print(repr(song), end=";\n")

    def delete_songs(self, id_song):
        for i in range(len(self.songs)):
            if self.songs[i].id == id_song:
                self.songs.pop(i)
                return "\nMelodia a fost stearsa"

        return "\nMelodia nu exista"

    def update_songs(self, id_song, new_song: Song):
        for i in range(len(self.songs)):
            if self.songs[i].id == id_song:
                self.songs[i] = new_song
                return "\nMelodia a fost actualizata."

        return "\nA aparut o problema."


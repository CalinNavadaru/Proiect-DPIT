from collections import Counter
from entities.listener import Listener


class StatisticsServices:

    def __init__(self, repo_song, repo_listener):
        '''
        Constructor clasa.
        :param repo_song: Lista care contine melodiile in memorie
        :param repo_listener: Lista care contine ascultatorii in memorie
        '''
        self.repo_song = repo_song
        self.repo_listener = repo_listener

    def average_duration_songs(self):
        '''
        O functie ce calculeaza durata medie a melodiilor
        :return: durata medie de tip int
        '''
        if len(self.repo_song.songs) == 0:
            return "Nu aveti melodii in playlist"
        total_duration = 0
        for song in self.repo_song.songs:
            total_duration += song.get_length()

        return total_duration // len(self.repo_song.songs)

    def average_age_listeners(self):
        '''
        O functie ce calculeaza varsta medie a ascultatoriilor
        :return: varsta medie a ascultatoriilor ca si int
        '''
        if len(self.repo_listener.listeners) == 0:
            return "Nu aveti melodii in playlist"

        sum_ages = 0
        for listener in self.repo_listener.listeners:
            sum_ages += listener.get_age()

        return sum_ages // len(self.repo_listener.listeners)

    def most_popular_artist_playlist(self):
        '''
        O functie ce determina cel mai popular artist
        :return: Cel mai popular artist ca si string
        '''
        if len(self.repo_song.songs) == 0:
            return "Nu aveti melodii in playlist"

        dict_artists = Counter(song.artist for song in self.repo_song.songs)

        max_appearances = -1
        most_popular_artist = ''

        for artist in dict_artists.items():
            if artist[1] > max_appearances:
                most_popular_artist = artist[0]

        return most_popular_artist

    def unlistened_songs(self):
        '''
        O functie ce determina melodiile neascultate
        :return: O lista cu melodiile neascultate
        '''
        if len(self.repo_song.songs) == 0:
            return "Nu aveti melodii in playlist"

        list_unlistened_songs = []

        for song in self.repo_song.songs:
            listener : Listener
            listened = False
            for listener in self.repo_listener.listeners:
                if listener.song == song:
                    listened = True
                    break
            if not listened:
                list_unlistened_songs.append(song)

        return list_unlistened_songs

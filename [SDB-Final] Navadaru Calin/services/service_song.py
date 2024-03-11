from repo.repo_song import RepoSong


class ServiceSong:

    def __init__(self, repo_song: RepoSong):
        self.repo_song = repo_song

    def add_songs(self, new_song):
        return self.repo_song.add_song(new_song)

    def print_songs(self):
        self.repo_song.print_songs()

    def delete_songs(self, id_song):
        return self.repo_song.delete_songs(id_song)

    def update_songs(self, id_song, new_song):
        return self.repo_song.update_songs(id_song, new_song)

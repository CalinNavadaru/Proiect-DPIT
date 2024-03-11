class Song:
    id_integer = 0

    def __init__(self, new_name: str, new_artist: str, new_genre: str, new_length: int):
        self.name = new_name
        self.artist = new_artist
        self.genre = new_genre
        self.length = new_length
        self.id = Song.id_integer
        Song.id_integer += 1

    def get_name(self):
        return self.name

    def get_artist(self):
        return self.artist

    def get_genre(self):
        return self.genre

    def get_length(self):
        return self.length

    def get_id(self):
        return self.id

    def set_name(self, new_name: str):
        self.name = new_name

    def set_artist(self, new_artist: str):
        self.artist = new_artist

    def set_genre(self, new_genre: str):
        self.genre = new_genre

    def set_length(self, new_length: int):
        self.length = new_length

    def set_id(self, new_id: int):
        self.id = new_id

    def __repr__(self):
        return "Title: {0}, Artist: {1}, Genre: {2}, Duration(in seconds): {3}  ID: {4}".format(self.name,
                                                                                                self.artist,
                                                                                                self.genre,
                                                                                                self.length,
                                                                                                self.id)

    def __str__(self):
        return "{0},{1},{2},{3}".format(self.name,
                                        self.artist,
                                        self.genre,
                                        self.length)

    def __eq__(self, other):
        return (self.name.lower().split(" ") == other.name.lower().split(" ")
                and self.artist.lower().split(" ") == other.artist.lower().split(" ")
                and self.genre.lower() == other.genre.lower()
                and self.length == other.length)

from entities.song import Song


class Listener:
    id_integer = 0

    def __init__(self, new_name: str, new_age: int, new_song: Song):
        self.name = new_name
        self.age = new_age
        self.song = new_song
        self.id = Listener.id_integer
        Listener.id_integer += 1

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_song(self):
        return self.song

    def get_id(self):
        return self.id

    def set_name(self, new_name: str):
        self.name = new_name

    def set_age(self, new_age: int):
        self.age = new_age

    def set_song(self, new_song: Song):
        self.song = new_song

    def set_id(self, new_id: int):
        self.id = new_id

    def __repr__(self):
        return "Name: {0}, Age: {1}, ID: {2}, Listened song:\n\t{3}".format(self.name, self.age, self.id, self.song)

    def __str__(self):
        return "Name: {0}, Age: {1}, ID: {2}, Listened song:\n\t{3}".format(self.name, self.age, self.id, str(self.song))

    def __eq__(self, other):
        return (self.name.lower().split(" ") == other.name.lower().split(" ")
                and self.age == other.age
                and self.song == other.song)

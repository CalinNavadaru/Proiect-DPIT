import os
from entities.listener import Listener
from entities.song import Song


class RepoListener:

    def __init__(self):
        self.listeners = []
        self.__read_from_file()

    def __read_from_file(self):
        file = open("listeners.txt", "r")

        if os.stat("listeners.txt").st_size == 0:
            raise EOFError

        while True:
            try:
                line = file.readline().split(",")
                line[1] = int(line[1])
                line[2] = Song(*line[2:])
                self.add_listener(Listener(*line[:3]))
                if os.stat("listeners.txt").st_size == 0 or len(line) == 0:
                    raise EOFError

            except(IndexError, EOFError):
                break

    def write_to_file(self):

        file = open("listeners.txt", "w")

        listeners: Listener
        for listeners in self.listeners:
            listeners_details = listeners.name + ',' + str(listeners.age) + ',' + str(listeners.song)
            file.write(listeners_details)

    def add_listener(self, new_listener: Listener):
        if not (new_listener in self.listeners):
            self.listeners.append(new_listener)
            return "\nAscultatorul a fost adaugat"

        return "\nAscultatorul exista deja"

    def delete_listener(self, id_listener):
        for i in range(len(self.listeners)):
            if self.listeners[i].id == id_listener:
                self.listeners.pop(i)
                return "\nAscultatorul a fost sters"

        return "\nAscultatorul nu exista"

    def update_listener(self, id_listener, new_listener):
        for i in range(len(self.listeners)):
            if self.listeners[i].id == id_listener:
                self.listeners[i] = new_listener
                return "\nAscultatorul a fost actualizat."

        return "\nA aparut o problema."

    def print_listeners(self):
        for listener in self.listeners:
            print(listener, end=";\n\n")


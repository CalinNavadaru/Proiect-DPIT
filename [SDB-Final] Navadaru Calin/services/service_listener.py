from repo.repo_listener import RepoListener


class ServiceListener:

    def __init__(self, repo_listener: RepoListener):
        self.repo_listener = repo_listener

    def add_listener(self, new_listener):
        return self.repo_listener.add_listener(new_listener)

    def print_listeners(self):
        self.repo_listener.print_listeners()

    def delete_listeners(self, id_listener):
        return self.repo_listener.delete_listener(id_listener)

    def update_listeners(self, id_listener, new_listener):
        return self.repo_listener.update_listener(id_listener, new_listener)

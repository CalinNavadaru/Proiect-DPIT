import os

from repo.repo_listener import RepoListener
from repo.repo_song import RepoSong
from services.service_listener import ServiceListener
from services.service_song import ServiceSong
from services.statistics_services import StatisticsServices
from ui.console_ui import ConsoleUi

if __name__ == "__main__":
    os.chdir(os.getcwd() + r'\repo')
    repo_listener = RepoListener()
    repo_song = RepoSong()
    service_song = ServiceSong(repo_song)
    service_listener = ServiceListener(repo_listener)
    statistics_service = StatisticsServices(repo_song, repo_listener)
    console_ui = ConsoleUi(service_song, service_listener, statistics_service)

    console_ui.run()

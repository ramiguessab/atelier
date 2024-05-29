from abc import ABC, abstractmethod
import socket


class EventHandler(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def handle(self, socket: socket.socket, data): ...

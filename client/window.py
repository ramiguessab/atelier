from customtkinter import CTk, CTkToplevel
from socket import socket
from abc import ABC, abstractmethod


# 350x + 500
class Window(ABC):
    def __init__(self, title: str) -> None:
        super().__init__()
        self.socket = socket
        self.title = title

    @abstractmethod
    def build(self, app: CTk | CTkToplevel): ...

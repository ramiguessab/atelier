from customtkinter import CTk, CTkToplevel
from socket import socket
from abc import ABC, abstractmethod


class Window(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.socket = socket

    @abstractmethod
    def build(self, app: CTk | CTkToplevel): ...
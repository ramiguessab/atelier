from socket import socket
import json


class Message:
    def __init__(self, eventName: str, data, socket: socket) -> None:
        self.eventName = eventName
        self.data = data
        self.socket = socket

    def send(self):
        eventName = self.eventName
        data = json.dumps(self.data)
        socket = self.socket
        message = f"{eventName}|;{data}"
        socket.sendall(message.encode())

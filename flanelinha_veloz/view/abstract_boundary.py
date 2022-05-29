from abc import ABC
import PySimpleGUI as sg


class AbstractBoundary(ABC):
    sg.theme('DarkGray5')

    def show_message(self, message: str):
        sg.popup_ok(message)
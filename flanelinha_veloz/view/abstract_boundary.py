from abc import ABC
import PySimpleGUI as sg


class AbstractBoundary(ABC):
    sg.theme('DarkTanBlue')

    def show_message(self, message: str):
        sg.popup_ok(message)
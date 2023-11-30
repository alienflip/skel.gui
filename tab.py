import PySimpleGUI as sg

class tab:
    def __init__(self):
        self.tab = []

    def get(self):
        return [self.tab, self.target]

    def add_button(self, _name, _key):
        self.tab.append(sg.Button(_name, key=_key))

    def add_slider(self, _range, _orientation, _size, _default_value, _key):
        self.tab.append(sg.Slider(range=_range, orientation=_orientation, size=_size, default_value=_default_value, key=_key))

    def add_taget(self, _key):
        self.target= [sg.Text('set path:'), sg.Input('<target file path>', key=_key)]
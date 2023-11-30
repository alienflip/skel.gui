import PySimpleGUI as sg

class tabs:
    def __init__(self):
        self.tabs = [] 

    def get(self):
        return [sg.TabGroup([self.tabs])]

    def add_tab(self, _name, _tab):
        self.tabs.append(sg.Tab(_name, _tab))
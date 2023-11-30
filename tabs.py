import PySimpleGUI as sg

class tabs:
    def __init__(self):
        self.tabs = [] 

    def get(self):
        return sg.TabGroup([self.tabs], enable_events=True)

    def add_tab(self, _name, _tab, _key):
        self.tabs.append(sg.Tab(_name, _tab, _key))
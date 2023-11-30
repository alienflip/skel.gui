import PySimpleGUI as sg
from UI.tabs import tabs

class layout:
    def __init__(self, menu, radio):
        self.layout = [[sg.Menu(menu)]]
        top_level_radio_element = [
            sg.Text(radio[0]),
            sg.Radio(radio[1], "gen", key='set_0', default=True),
        ]
        for i in range(2, len(radio)):
            top_level_radio_element.append(sg.Radio(radio[i], "gen", key='set_'+str(i), default=False))
        self.add_element(top_level_radio_element)

    def add_element(self, element):
        self.layout.append(element)

    def add_tabs(self, tab_group):
        self.layout.append(tab_group)
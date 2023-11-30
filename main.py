import os
from os.path import join, dirname
from dotenv import load_dotenv
import PySimpleGUI as sg
from utils.utils import utils_class
from operation.operation import operations_class
from tests.test import test_class
from tab import tab
from tabs import tabs
from layout import layout

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TAB_COUNT = int(os.environ.get("TAB_COUNT"))

# import helper classes
_utils = utils_class()
_ops = operations_class()
_test = test_class()

# create top level UI
top_level_menu = [
    ['file', 
        ['save', 'load']
    ], 
    ['operation', 
        ['exec_op']
    ],  
    ['test', 
        ['exec_test']
    ], 
]

top_level_radio_element = ["option id:", "option 0", "option 1", "option 2"]

# create top level layout
_layout = layout(top_level_menu, top_level_radio_element)

# create individual tabs
i_tabs = []
for i in range(TAB_COUNT):
    new_tab = tab()
    new_tab.add_button(_name='press', _key='press_' + str(i))
    new_tab.add_slider(_range=(0, 100), _orientation='h', _size=(20, 20), _default_value=0, _key='slide_' + str(i))
    new_tab.add_taget(_key='target_' + str(i))
    i_tabs.append(new_tab)

# add tabs to tab group layout
_tabs = tabs()
for i in range(TAB_COUNT):
    _tabs.add_tab('tab ' + str(i), i_tabs[i].get())

# add tab group to top level layout
_layout.add_tabs(_tabs.get())

# add layout to window
window = sg.Window('py.exec', _layout.layout, size=(1000, 700))

# event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'exec_op':
        output = _ops.test_op([1,2,3])
        print("operation output: ", output)
    if event == 'exec_test':
        output = _ops.test_op([1,2,3])
        _test.test_op(output)
    if event == "save":
        _utils.save('save_load/'+"test_file.txt", "test text corpus")
        print("file saved to: save_load/"+"test_file.txt")
    if event == "load":
        _utils.load('save_load/'+"test_file.txt")
    
window.close()
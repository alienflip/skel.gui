import os, base64
from os.path import join, dirname
from dotenv import load_dotenv
import PySimpleGUI as sg
from utils.utils import utils_class
from operation.operation import operations_class
from tests.test import test_class
from UI.tab import tab
from UI.tabs import tabs
from UI.layout import layout

dotenv_path = join(dirname(__file__), '.secret.env')
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
    _tabs.add_tab('tab ' + str(i), i_tabs[i].get(), 'tab_' + str(i))

# add tab group to top level layout
to = [_tabs.get()]
_layout.add_tabs(to)

taskbar_icon = base64.b64encode(open(r'cog.png', 'rb').read())
window = sg.Window('skel.gui', _layout.layout, resizable=True, size=(1000, 700), icon=taskbar_icon, finalize=True)

# event loop
current_tab = 0
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if values:
        current_tab = int(values[1][4:])
    if event == 'exec_op':
        output = _ops.test_op([1,2,3])
        print("operation output: ", output)
    if event == 'exec_test':
        output = _ops.test_op([1,2,3])
        _test.test_op(output)
    if event == "save":
        path = 'save_load/' + str(values['target_' + str(current_tab)])
        _utils.save(path , str(values['slide_' + str(current_tab)]))
        print("file saved to: " + path)
    if event == "load":
        path = 'save_load/' + values['target_' + str(current_tab)]
        _utils.load(path)
        print("file loaded from: " + path)
        
window.close()
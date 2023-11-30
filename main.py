import PySimpleGUI as sg
from utils.utils import utils_class
from operation.operation import operations_class
from tests.test import test_class
from tab import tab
from tabs import tabs
from layout import layout

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

# create tab UI
tab_0 = tab()
tab_1 = tab()
tab_0.add_button(_name='press', _key='press_0')
tab_1.add_button(_name='press', _key='press_1')
tab_0.add_slider(_range=(0, 100), _orientation='h', _size=(20, 20), _default_value=0)
tab_1.add_slider(_range=(0, 100), _orientation='h', _size=(20, 20), _default_value=0)

# add tabs to tab group layout
_tabs = tabs()
_tabs.add_tab('tab 0', tab_0.get())
_tabs.add_tab('tab 1', tab_1.get())

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
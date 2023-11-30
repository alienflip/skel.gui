import PySimpleGUI as sg
from utils.utils import utils_class
from operation.operation import operations_class
from tests.test import test_class
from tab import tab
from tabs import tabs
from layout import layout

_utils = utils_class()
_ops = operations_class()
_test = test_class()

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

tab_0 = tab()
tab_1 = tab()
tab_0.add_button(_name='press', _key='press_0')
tab_1.add_button(_name='press', _key='press_1')
tab_0.add_slider(_range=(0, 100), _orientation='h', _size=(20, 20), _default_value=0)
tab_1.add_slider(_range=(0, 100), _orientation='h', _size=(20, 20), _default_value=0)

tab_group = tabs()
tab_group.add_tab(_name='tab 0', _tab=tab_0.get())
tab_group.add_tab(_name='tab 1', _tab=tab_1.get())

_layout = layout(top_level_menu, top_level_radio_element)
_layout.add_tabs(tab_group)

window = sg.Window('py.exec', _layout.layout, size=(1000, 700))

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
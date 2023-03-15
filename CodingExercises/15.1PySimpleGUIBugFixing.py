# import PySimpleGUI as sg
#
#
# def km_to_miles(km):
#     return float(km) / 1.6
#
#
# label = sg.Text("Kilometers: ")
# input_box = sg.InputText(tooltip="Enter todo", key="kms")
# miles_button = sg.Button("Convert")
#
# output = sg.Text(key="output")
#
# window = sg.Window('Km to Miles Converter',
#                    layout=[[label, input_box], [miles_button, output]],
#                    font=('Helvetica', 20))
#
# while True:
#     event, values = window.read()
#     match event:
#         case "Convert":
#             km = values["kms"]
#             result = km_to_miles(km)
#             window['output'].update(value=result)
#         case sg.WIN_CLOSED:
#             break
#
# window.close()


import PySimpleGUI as sg

# Prepare the widgets for the left column
left_column_content = [[sg.Text('Left 1')],
                       [sg.Text('Left 2')]]

# Prepare the widgets for the right column
right_column_content = [[sg.Text('Right 1')],
                        [sg.Text('Right 2')]]

# Construct the Column widgets
left_column = sg.Column(left_column_content)
right_column = sg.Column(right_column_content)

# Construct the layout
layout = [[left_column, right_column]]

# Construct and display the window
window = sg.Window('Columns', layout)
window.read()
window.close()
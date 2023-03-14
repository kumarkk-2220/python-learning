import PySimpleGUI as sg
import tometers as tm

feet_label = sg.Text("Enter Feet: ")
feet_text = sg.InputText(tooltip="Enter Height in Feet", key="feet")
inch_label = sg.Text("Enter Inches: ")
inch_text = sg.InputText(tooltip="Enter the height in inches", key="inch")
convert_button = sg.Button("Convert")
output_label = sg.Text(key="output")

layout = [[feet_label, feet_text], [inch_label, inch_text], [convert_button, output_label]]

window = sg.Window("Height Conversion", layout=layout)

while True:
    event, values = window.read()
    # print(event)
    # print(values)
    feets = values['feet']
    inches = values['inch']
    meters = tm.feet_to_meters(feet=feets, inch=inches)
    window["output"].update(value=f"{meters} m")


window.close()
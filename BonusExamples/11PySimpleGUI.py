# File compression program

import PySimpleGUI as sg

label_compress = sg.Text("Select files sto compress")
label_compress_path = sg.Input()
button_compress_choose = sg.FilesBrowse("Choose")


label_destination = sg.Text("Select destination folder")
label_destination_path = sg.Input()
button_destination_choose = sg.FolderBrowse("Choose")

button_compress = sg.Button("Compress")

window = sg.Window("File Zipper", layout=[[label_compress, label_compress_path, button_compress_choose],
                                          [label_destination, label_destination_path, button_destination_choose],
                                          [button_compress]])
window.read()
window.close()

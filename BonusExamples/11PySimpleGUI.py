# File compression program

import PySimpleGUI as sg
from zipper import make_archive

label_compress = sg.Text("Select files sto compress")
label_compress_path = sg.Input()
button_files_choose = sg.FilesBrowse("Choose", key="files")


label_destination = sg.Text("Select destination folder")
label_destination_path = sg.Input()
button_folder_choose = sg.FolderBrowse("Choose", key="folder")

button_compress = sg.Button("Compress")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("File Zipper", layout=[[label_compress, label_compress_path, button_files_choose],
                                          [label_destination, label_destination_path, button_folder_choose],
                                          [button_compress, output_label]])

while True:
    event, values = window.read()
    print(event)
    print(values)
    filepaths = values['files'].split(";")
    folder = values['folder']
    make_archive(filepaths=filepaths, dest_dir=folder)
    window["output"].update(value="Compression Completed!")
    # print(f"Filepaths: {filepaths}")
    # print(f"Folder: {folder}")


window.close()

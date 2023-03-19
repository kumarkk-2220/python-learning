import PySimpleGUI as sg
import zipextractorfunction

# archive_label = sg.Text("Select Archive:")
# archive_box = sg.Input(key="source_path")
# select_archive_button = sg.FilesBrowse("Browse", key="source_button")
#
# destination_label = sg.Text("Select Destination:")
# destination_box = sg.Input(key="destination_path")
# select_destination_button = sg.FolderBrowse("Browse", key="destination_button")
#
# extract_button = sg.Button("Extract Now!", key="extract")
# extracting_status = sg.Text(key="output", text_color="white")
#
# # column_labels = sg.Column([[archive_label], [destination_label]])
# # column_boxes = sg.Column([[archive_box], [destination_box]])
# # column_browse = sg.Column([[select_archive_button], [select_destination_button]])
#
# layout = [[archive_label, archive_box, select_archive_button],
#           [destination_label, destination_box, select_destination_button],
#           [extract_button, extracting_status]]
# window = sg.Window("Archive Extractor", layout=layout)
# # window['source_path'].update('source_button')
# # window['destination_path'].update('destination_button')
# while True:
#     try:
#         event, values = window.read()
#         window['source_path'].update(values['source_button'])
#         window['destination_path'].update(values['destination_button'])
#         zipextractorfunction.extract_zip(values['source_path'], values['destination_path'])
#         window['output'].update(value="Extraction Completed")
#     except TypeError:
#         break
#
# window.close()

import PySimpleGUI as sg

# from zip_extractor import extract_archive

sg.theme("Black")

label1 = sg.Text("Select archive:")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select destination directory:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

col1 = sg.Column([[label1], [label2]])
col2 = sg.Column([[input1], [input2]])
col3 = sg.Column([[choose_button1], [choose_button2]])

window = sg.Window("Archive Extractor",
                   layout=[[col1, col2, col3], [extract_button]])
while True:
    event, values = window.read()
    print(event, values)
    archivepath = values["archive"]
    dest_dir = values["folder"]
    zipextractorfunction.extract_zip(archivepath, dest_dir)
    window["output"].update(value="Extraction Completed!")

window.close()
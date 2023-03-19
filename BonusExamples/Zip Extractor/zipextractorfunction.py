from zipfile import ZipFile as zf


def extract_zip(source, destination):
    if ';' in source:
        source = source.split(";")
        for zip_file in source:
            zip_file = zf(zip_file)
            zip_file.extractall(path=destination)
    else:
        zip_file = zf(source)
        zip_file.extractall(path=destination)


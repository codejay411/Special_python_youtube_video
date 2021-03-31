from zipfile import ZipFile

file = "unzip folder/josh.zip"
with ZipFile(file, 'r') as zip:
    zip.printdir()
    print("---- Extracting all files -----")
    zip.extractall()
    print("Done")
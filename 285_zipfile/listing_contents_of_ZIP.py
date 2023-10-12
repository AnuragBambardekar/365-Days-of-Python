import zipfile

with zipfile.ZipFile('285_zipfile/example.zip', 'r') as myzip:
    file_list = myzip.namelist()
    print(file_list)

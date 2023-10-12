import zipfile

# Extract specified file
with zipfile.ZipFile('285_zipfile/example.zip', 'r') as myzip:
    myzip.extract('285_zipfile/file.txt', path='285_zipfile/extracted_files/')

# Extract all files
with zipfile.ZipFile('285_zipfile/example.zip', 'r') as myzip:
    myzip.extractall(path='285_zipfile/extracted_all_files/')

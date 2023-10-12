import zipfile

with zipfile.ZipFile('285_zipfile/example.zip', 'a') as myzip:
    myzip.write('285_zipfile/another_file.txt')

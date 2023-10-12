import zipfile

with zipfile.ZipFile('example.zip', 'w') as myzip:
    myzip.write('285_zipfile/file.txt')
    # myzip.writestr('data.txt', 'This is some text data.')
    myzip.writestr('285_zipfile/data.txt', 'This is some text data.')

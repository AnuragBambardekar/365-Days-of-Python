import tarfile

# open file
file = tarfile.open('265_Uncompress_targz/gfg.tar.gz')

# print file names
print(file.getnames())

# extract files
file.extractall('265_Uncompress_targz/uncompressed')

# extract specific file
# file.extract('sample.txt', '265_Uncompress_targz/uncompressed')

# close file
file.close()

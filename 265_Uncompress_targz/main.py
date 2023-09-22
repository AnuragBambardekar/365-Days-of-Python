import tarfile

# open file
file = tarfile.open('265_Uncompress_targz/gfg.tar.gz')

# extracting file
file.extractall('./uncompressed')

file.close()

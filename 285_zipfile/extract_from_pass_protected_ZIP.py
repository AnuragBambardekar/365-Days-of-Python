import zipfile

# The module can’t handle the creation of encrypted ZIP files.

# with zipfile.ZipFile('285_zipfile/secure.zip', 'w', zipfile.ZIP_DEFLATED) as myzip:
#     myzip.setpassword(b'mypassword')
#     myzip.write('285_zipfile/file.txt', arcname='file.txt', compress_type=zipfile.ZIP_DEFLATED)

# extract password-protected file
# with zipfile.ZipFile('285_zipfile/secure.zip', 'r') as myzip:
#     # myzip.setpassword(b'mypassword')
#     myzip.extract('file.txt', path='extracted_pass_prot_files/')

with zipfile.ZipFile("285_zipfile/secure.zip", mode="r") as archive:
    # for line in archive.read("file.txt", pwd=b"mypassword").split(b"\n"):
    #     print(line)

    for line in archive.read("file.txt").split(b"\n"):
        print(line)
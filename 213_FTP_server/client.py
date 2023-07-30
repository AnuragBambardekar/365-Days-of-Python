import ftplib

# connection parameters

ftpHost = 'localhost'
ftpPort = 21
ftpUname = 'bamba1'
ftpPass = '12345'

# creating a FTP Client instance
ftp = ftplib.FTP(timeout=30)
# ftp = ftplib.FTP_TLS(timeout=30) #if using FTP over TLS

# connect to FTP server
ftp.connect(ftpHost, ftpPort)

# login to FTP server
ftp.login(ftpUname, ftpPass)

# setup secure data connection
# ftp.prot_p() #if using FTP over TLS

#================================================================================================================#
# Change Working Directory
# ftp.cwd("folder1/abcd")

#================================================================================================================#
# List of filenames
fnames = ftp.nlst("/")
print(fnames)

#================================================================================================================#
# uploading a file to FTP folder
# ftp.cwd("folder1/abcd")
# localFilePath = "./uploadME.txt"
# with open(localFilePath, 'rb') as file:
#     retCode = ftp.storbinary("STOR uploadME_1", file, blocksize=1024*1024) # blocksize=1MB

#================================================================================================================#
# Downloading a file from FTP folder
# ftp.cwd("folder1/abcd")
# targetFileName = "uploadME_1.txt"
# localFilePath = targetFileName

# with open(localFilePath, 'wb') as file:
#     retCode = ftp.retrbinary(f"RETR {targetFileName}", file.write)

#================================================================================================================#
# Renaming a file in FTP folder
# ftp.cwd("folder1/abcd")
# fnames = ftp.nlst("/folder1/abcd")
# print(fnames)
# targetFileName = "uploadME_1.txt"
# ftp.rename(targetFileName,"downloadME.txt")
# fnames = ftp.nlst("/folder1/abcd")
# print(fnames)

#================================================================================================================#
# Deleting a file from FTP folder
# ftp.cwd("folder1/abcd")
# ftp.delete("downloadME.txt")
# fnames = ftp.nlst("/folder1/abcd")
# print(fnames)

#================================================================================================================#
# Making a folder in FTP folder
# ftp.cwd("folder1/abcd")
# ftp.mkd("TEST")
# fnames = ftp.nlst("/")
# print(fnames)

#================================================================================================================#
# Removing a folder in FTP folder
# ftp.cwd("/")
# ftp.rmd("TEST")
# fnames = ftp.nlst("/")
# print(fnames)

#================================================================================================================#
# Close the connection
ftp.quit()


#================================================================================================================#
# Checking if file was uploaded successfully to FTP folder
# if retCode.startswith("226"):
#     print("upload successful")
# else:
#     print("Upload not successful!")
#================================================================================================================#

# Checking if file was downloaded successfully from FTP folder
# if retCode.startswith("226"):
#     print("upload successful")
# else:
#     print("Upload not successful!")
#================================================================================================================#

print("Done")
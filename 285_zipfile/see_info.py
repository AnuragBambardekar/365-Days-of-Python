import datetime
import zipfile

with zipfile.ZipFile("285_zipfile/example.zip", mode="r") as archive:
    for info in archive.infolist():
        print(f"Filename: {info.filename}")
        print(f"Modified: {datetime.datetime(*info.date_time)}")
        print(f"Normal size: {info.file_size} bytes")
        print(f"Compressed size: {info.compress_size} bytes")
        print("-" * 20)
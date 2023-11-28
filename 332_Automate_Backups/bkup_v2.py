import shutil
from datetime import date
import os
import sys

os.chdir(sys.path[0])

def perform_backup(src_file_name,
                   dst_file_name=None,
                   src_dir='',
                   dst_dir=''):
    try:
        today = date.today()
        date_format = today.strftime("%d_%b_%Y_")

        src_dir = src_dir + src_file_name

        if not src_file_name:
            print("Source File name required!")
            exit()
        
        try:
            if src_file_name and dst_file_name and src_dir and dst_dir:
                src_dir = src_dir + src_file_name
                dst_dir = dst_dir + dst_file_name

            elif dst_file_name is None or not dst_file_name:
                dst_file_name = src_file_name
                dst_dir = dst_dir + date_format + dst_file_name

            elif dst_file_name.isspace():
                dst_file_name = src_file_name
                dst_dir = dst_dir + date_format + dst_file_name

            else:
                dst_dir = dst_dir + date_format + dst_file_name

            shutil.copy2(src_dir, dst_dir)

            print("Backup Successful!")
        except FileNotFoundError:
            print("File does not exist!, Please give the complete path.")

    except PermissionError:
        dst_dir = dst_dir + date_format + dst_file_name

        shutil.copytree(src_file_name, dst_dir)

perform_backup("bkupThis.txt")

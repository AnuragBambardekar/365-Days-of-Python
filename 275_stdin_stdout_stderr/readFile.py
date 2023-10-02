"""
Get-Content newfile.txt | python .\main.py   
"""
import sys

file_contents = sys.stdin.read()

# Print the contents
print(file_contents)
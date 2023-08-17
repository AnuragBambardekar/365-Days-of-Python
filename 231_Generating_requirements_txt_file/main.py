import requests
import cv2

r = requests
cv = cv2

# pip freeze > requirements.txt
# pip install -r requirements.txt

"""
While pip freeze is a convenient way to generate a list of installed packages and their versions, it does have some drawbacks and 
limitations:

Including Unneeded Packages: pip freeze lists all installed packages and their versions, including those that might not be necessary 
for your project. This can lead to a cluttered and unnecessarily large requirements.txt file.
"""

# So install:
# pip install pipreqs
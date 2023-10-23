"""
Back button, forward button and reload button
"""

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
import sys

app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()

# Create the web view
view = QWebEngineView()
layout.addWidget(view)

# Create a navigation bar with back, forward, and reload buttons
nav_bar = QHBoxLayout()
back_button = QPushButton("Back")
forward_button = QPushButton("Forward")
reload_button = QPushButton("Reload")

nav_bar.addWidget(back_button)
nav_bar.addWidget(forward_button)
nav_bar.addWidget(reload_button)

# Create an address bar
address_bar = QLineEdit()
address_bar.setPlaceholderText("Enter URL and press Enter")

# Function to handle URL input from the address bar
def load_url():
    url = address_bar.text()
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    view.setUrl(QUrl(url))

address_bar.returnPressed.connect(load_url)

# Connect the buttons to their respective actions
back_button.clicked.connect(view.back)
forward_button.clicked.connect(view.forward)
reload_button.clicked.connect(view.reload)

layout.addLayout(nav_bar)
layout.addWidget(address_bar)

view.setUrl(QUrl("https://www.google.com/"))

window.setLayout(layout)
window.show()

app.exec()

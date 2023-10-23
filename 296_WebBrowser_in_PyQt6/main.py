from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
import sys
 
app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()
 
view = QWebEngineView()
layout.addWidget(view)
 
view.setUrl(QUrl("https://www.google.com/"))
 
window.setLayout(layout)
window.show()
 
app.exec()
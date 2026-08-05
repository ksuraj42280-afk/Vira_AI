from PySide6.QtWidgets import QApplication, QLabel
import sys

app = QApplication(sys.argv)

label = QLabel("JARVIS OS")
label.resize(400, 150)
label.show()

sys.exit(app.exec())
import sys

from PySide6.QtWidgets import QApplication
from ui.widgets import AICoreWidget

app = QApplication(sys.argv)

window = AICoreWidget()
window.setWindowTitle("AI Core Test")
window.resize(400, 400)
window.show()

sys.exit(app.exec())
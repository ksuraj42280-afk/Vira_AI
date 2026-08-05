import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
)

from PySide6.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # -----------------------------
        # Window
        # -----------------------------
        self.setWindowTitle("JARVIS OS")
        self.resize(1400, 800)

        # -----------------------------
        # Style
        # -----------------------------
        self.setStyleSheet("""
        QMainWindow{
            background-color:#090909;
        }

        QLabel{
            color:white;
            font-size:30px;
            font-weight:bold;
        }

        QFrame{
            background-color:#151515;
            border:1px solid #2d2d2d;
            border-radius:12px;
        }
        """)

        # -----------------------------
        # Central Widget
        # -----------------------------
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(15)

        # -----------------------------
        # Title
        # -----------------------------
        title = QLabel("JARVIS OS")
        title.setAlignment(Qt.AlignCenter)

        main_layout.addWidget(title)

        # -----------------------------
        # Dashboard Layout
        # -----------------------------
        dashboard = QHBoxLayout()
        dashboard.setSpacing(15)

        # Left Panel
        left_panel = QFrame()
        left_panel.setMinimumWidth(250)

        left_layout = QVBoxLayout()
        left_layout.addWidget(QLabel("CPU"))
        left_layout.addWidget(QLabel("Battery"))
        left_layout.addWidget(QLabel("Weather"))
        left_layout.addStretch()
        left_panel.setLayout(left_layout)

        # Center Panel
        center_panel = QFrame()

        center_layout = QVBoxLayout()

        ai_title = QLabel("AI CORE")
        ai_title.setAlignment(Qt.AlignCenter)

        center_layout.addStretch()
        center_layout.addWidget(ai_title)
        center_layout.addStretch()

        center_panel.setLayout(center_layout)

        # Right Panel
        right_panel = QFrame()
        right_panel.setMinimumWidth(250)

        right_layout = QVBoxLayout()
        right_layout.addWidget(QLabel("RAM"))
        right_layout.addWidget(QLabel("Network"))
        right_layout.addWidget(QLabel("Clock"))
        right_layout.addStretch()
        right_panel.setLayout(right_layout)

        dashboard.addWidget(left_panel)
        dashboard.addWidget(center_panel, 1)
        dashboard.addWidget(right_panel)

        main_layout.addLayout(dashboard)

        # -----------------------------
        # Bottom Chat Panel
        # -----------------------------
        chat_panel = QFrame()
        chat_panel.setFixedHeight(170)

        chat_layout = QVBoxLayout()

        chat_title = QLabel("Conversation")
        chat_title.setAlignment(Qt.AlignCenter)

        chat_layout.addWidget(chat_title)

        chat_panel.setLayout(chat_layout)

        main_layout.addWidget(chat_panel)

        central.setLayout(main_layout)


def run():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import (
    QPainter,
    QColor,
    QPen,
    QBrush,
)
from PySide6.QtCore import Qt, QTimer


class AICoreWidget(QWidget):
    """
    JARVIS AI Core Widget

    Features:
    - Animation Engine
    - Future Rotating Rings
    - Voice Pulse
    - Neon Glow
    """

    def __init__(self):
        super().__init__()

        self.setMinimumSize(320, 320)

        # Animation
        self.angle = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(16)   # ~60 FPS

    def animate(self):
        """Update animation"""

        self.angle += 2

        if self.angle >= 360:
            self.angle = 0

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        width = self.width()
        height = self.height()

        center_x = width / 2
        center_y = height / 2

        # Transparent Background
        painter.fillRect(self.rect(), Qt.transparent)

        # Save painter state
        painter.save()

        # Move origin to center
        painter.translate(center_x, center_y)

        # Rotate
        painter.rotate(self.angle)

        # --------------------------
        # Outer Ring
        # --------------------------
        pen = QPen(QColor(0, 180, 255))
        pen.setWidth(5)

        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)

        painter.drawEllipse(-120, -120, 240, 240)

        # --------------------------
        # Middle Ring
        # --------------------------
        pen.setWidth(3)

        painter.setPen(pen)

        painter.drawEllipse(-90, -90, 180, 180)

        # --------------------------
        # Inner Ring
        # --------------------------
        pen.setWidth(2)

        painter.setPen(pen)

        painter.drawEllipse(-60, -60, 120, 120)

        # Restore rotation
        painter.restore()

        # --------------------------
        # AI Core
        # --------------------------
        painter.setPen(Qt.NoPen)

        painter.setBrush(QBrush(QColor(0, 180, 255)))

        painter.drawEllipse(
            int(center_x - 22),
            int(center_y - 22),
            44,
            44,
        )

        # --------------------------
        # Center Dot
        # --------------------------
        painter.setBrush(QBrush(QColor(255, 255, 255)))

        painter.drawEllipse(
            int(center_x - 5),
            int(center_y - 5),
            10,
            10,
        )
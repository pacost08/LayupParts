import sys
import math
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QSlider, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt, QTimer, QPoint
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor, QPolygonF, QPixmap, QFont

class AirplaneSimulator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Airplane Control Simulator")
        self.setGeometry(100, 100, 800, 600)

        #Airplane state
        self.airplane_x, self.airplane_y = 0, 0
        self.angle = 0
        self.speed = 10
        self.camera_x, self.camera_y = 0, 0

        self.initUI()

        #Load image
        self.airplane_image = QPixmap("airplane.png")
        if self.airplane_image.isNull():
            print("Error: Airplane image not found, using a triangle instead.")

        #Update Loop
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_position)
        self.timer.start(100)

        self.trajectory = []

        self.setFocus()
        self.installEventFilter(self)

    def initUI(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        controls_layout = QVBoxLayout()

        #Title
        self.title_label = QLabel("Airplane Control Simulator")
        self.title_label.setFont(QFont("Courier New", 40, QFont.Weight.Bold))
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.title_label.setStyleSheet("""
            color: white;
            background-color: #0061ff;
            padding: 10px;
            font-size: 40px;
            font-weight: bold;
            text-transform: uppercase;
        """)

        #Controls
        self.yaw_label = QLabel("Yaw: 0°")
        self.yaw_slider = QSlider(Qt.Orientation.Horizontal)
        self.yaw_slider.setMinimum(-180)
        self.yaw_slider.setMaximum(180)
        self.yaw_slider.setValue(0)
        self.yaw_slider.valueChanged.connect(self.change_yaw)

        self.speed_label = QLabel("Speed: 10 knots")
        self.speed_slider = QSlider(Qt.Orientation.Horizontal)
        self.speed_slider.setMinimum(5)
        self.speed_slider.setMaximum(50)
        self.speed_slider.setValue(10)
        self.speed_slider.valueChanged.connect(self.change_speed)

        self.status_label = QLabel("Airspeed: 10 knots | Heading: 0°")

        controls_layout.addWidget(self.yaw_label)
        controls_layout.addWidget(self.yaw_slider)
        controls_layout.addWidget(self.speed_label)
        controls_layout.addWidget(self.speed_slider)
        controls_layout.addWidget(self.status_label)

        controls_layout.addStretch(1)

        controls_layout.setContentsMargins(0, 0, 0, 0)
        controls_layout.setSpacing(5)

        #Simulation Instructions
        self.shortcut_note = QLabel(
            "<b>Instructions:</b><br>Use Sliders above to adjust Yaw and Speed.<br> Or use Kebyoard Shortcuts listed below.<br><br><b>Keyboard Shortcuts:</b><br>Left/Right Arrow: Change Yaw<br>Up/Down Arrow: Change Speed")
        self.shortcut_note.setFont(QFont("Arial", 10))
        self.shortcut_note.setStyleSheet("border: 2px solid #4CAF50; padding: 10px; background-color: #f0f0f0;")
        self.shortcut_note.setTextFormat(Qt.TextFormat.RichText)
        self.shortcut_note.setMaximumWidth(300)

        self.yaw_slider.setToolTip("Adjust the yaw angle of the airplane.")
        self.speed_slider.setToolTip("Adjust the speed of the airplane.")

        layout.addWidget(self.title_label)
        layout.addLayout(controls_layout)
        layout.addWidget(self.shortcut_note)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def change_yaw(self, value):
        self.angle = value
        self.yaw_label.setText(f"Yaw: {value}°")
        self.update_status()

    def change_speed(self, value):
        self.speed = value
        self.speed_label.setText(f"Speed: {value} knots")
        self.update_status()

    def update_status(self):
        self.status_label.setText(f"Airspeed: {self.speed} knots | Heading: {self.angle}°")

    def update_position(self):
        #move given speed and yaw
        rad = math.radians(self.angle)
        dx = self.speed * math.cos(rad)
        dy = self.speed * math.sin(rad)

        self.airplane_x += dx
        self.airplane_y += dy

        #center view
        self.camera_x = self.airplane_x - 400
        self.camera_y = self.airplane_y - 300

        #save trajectory
        self.trajectory.append((self.airplane_x, self.airplane_y))
        if len(self.trajectory) > 1000:
            self.trajectory.pop(0)

        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setRenderHint(QPainter.RenderHint.Antialiasing)

        qp.translate(-self.camera_x, -self.camera_y)
        #draw trajectory
        pen = QPen(QColor(0, 0, 255), 2)
        qp.setPen(pen)
        for i in range(1, len(self.trajectory)):
            qp.drawLine(
                int(self.trajectory[i - 1][0]), int(self.trajectory[i - 1][1]),
                int(self.trajectory[i][0]), int(self.trajectory[i][1])
            )

        #Draw plane
        if not self.airplane_image.isNull():
            airplane_rect = self.airplane_image.rect()
            airplane_rect.moveCenter(QPoint(int(self.airplane_x), int(self.airplane_y)))
            qp.drawPixmap(airplane_rect, self.airplane_image)

    def keyPressEvent(self, event):
        #keyboard shortcuts
        if event.key() == Qt.Key.Key_Left:
            self.angle -= 5
            self.yaw_slider.setValue(self.angle)
        elif event.key() == Qt.Key.Key_Right:
            self.angle += 5
            self.yaw_slider.setValue(self.angle)
        elif event.key() == Qt.Key.Key_Up:
            self.speed = min(self.speed + 2, 50)
            self.speed_slider.setValue(self.speed)
        elif event.key() == Qt.Key.Key_Down:
            self.speed = max(self.speed - 2, 5)
            self.speed_slider.setValue(self.speed)

    def eventFilter(self, source, event):
        return super().eventFilter(source, event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    simulator = AirplaneSimulator()
    simulator.show()
    sys.exit(app.exec())
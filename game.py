import random
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QFont
from PySide6.QtCore import Qt, QTimer, QRect

WIDTH = 800
HEIGHT = 400
GRAVITY = 1
JUMP_STRENGTH = -18
HOLD_FORCE = -0.6
MAX_HOLD_TIME = 23


class Platformer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dog Platformer")
        self.setFixedSize(WIDTH, HEIGHT)
        self.setFocusPolicy(Qt.StrongFocus)

        self.timer = QTimer()
        self.timer.timeout.connect(self.game_loop)
        self.timer.start(30)

        self.reset_game()

    def reset_game(self):
        self.player = QRect(50, HEIGHT - 60, 40, 40)
        self.velocity_y = 0
        self.on_ground = True
        self.holding_jump = False
        self.hold_time = 0
        self.obstacles = []
        self.spawn_obstacle()
        self.score = 0
        self.game_over = False

    def spawn_obstacle(self):
        h = random.randint(40, 80)
        self.obstacles.append(QRect(WIDTH, HEIGHT - h, 30, h))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            if self.on_ground:
                self.velocity_y = JUMP_STRENGTH
                self.on_ground = False
                self.holding_jump = True
                self.hold_time = 0
            else:
                self.holding_jump = True
        elif event.key() == Qt.Key_R and self.game_over:
            self.reset_game()

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.holding_jump = False

    def game_loop(self):
        if self.game_over:
            return

        self.velocity_y += GRAVITY

        if self.holding_jump and self.hold_time < MAX_HOLD_TIME:
            self.velocity_y += HOLD_FORCE
            self.hold_time += 1

        self.player.translate(0, self.velocity_y)

        if self.player.bottom() >= HEIGHT:
            self.player.moveBottom(HEIGHT)
            self.on_ground = True
            self.velocity_y = 0
            self.hold_time = 0

        for obs in self.obstacles:
            obs.translate(-6, 0)

        self.obstacles = [o for o in self.obstacles if o.right() > 0]

        if random.random() < 0.025:
            self.spawn_obstacle()

        for obs in self.obstacles:
            if self.player.intersects(obs):
                self.game_over = True

        self.score += 1
        self.update()

    def draw_dog(self, painter):
        x = self.player.x()
        y = self.player.y()

        # Body
        painter.setBrush(QColor(160, 82, 45))
        painter.drawRect(x, y + 10, 40, 20)

        # Head
        painter.setBrush(QColor(139, 69, 19))
        painter.drawRect(x + 25, y, 15, 15)

        # Ear
        painter.setBrush(QColor(90, 40, 10))
        painter.drawRect(x + 30, y - 5, 5, 8)

        # Eye
        painter.setBrush(QColor(0, 0, 0))
        painter.drawEllipse(x + 32, y + 4, 3, 3)

        # Legs
        painter.setBrush(QColor(120, 60, 30))
        painter.drawRect(x + 5, y + 30, 5, 10)
        painter.drawRect(x + 25, y + 30, 5, 10)

    def draw_obstacle(self, painter, obs):
        # Нижня частина
        painter.setBrush(QColor(139, 69, 19))
        painter.drawRect(obs.x(), obs.y() + obs.height()//2, obs.width(), obs.height()//2)

        # Верхня частина
        painter.setBrush(QColor(34, 139, 34))
        painter.drawRect(obs.x(), obs.y(), obs.width(), obs.height()//2)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(20, 20, 40))
        self.draw_dog(painter)

        for obs in self.obstacles:
            self.draw_obstacle(painter, obs)

        painter.setPen(QColor(255, 255, 255))
        painter.setFont(QFont("Arial", 14))
        painter.drawText(10, 20, f"Score: {self.score}")

        if self.game_over:
            painter.setFont(QFont("Arial", 24))
            painter.drawText(self.rect(), Qt.AlignCenter, "GAME OVER\nPress R to Restart")
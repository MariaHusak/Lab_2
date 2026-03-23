import sys
from PySide6.QtWidgets import QApplication
from game import Platformer


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = Platformer()
    game.show()
    sys.exit(app.exec())
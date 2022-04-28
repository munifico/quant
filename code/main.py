from core.agent import *
from core.exchange import *
from core.strategy import *
from api.dart import *
from api.kospi import *
from ui.widgets import *

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = QMainWindow()
    window = MainWindow()
    root.setCentralWidget(window)
    root.show()
    sys.exit(app.exec_())

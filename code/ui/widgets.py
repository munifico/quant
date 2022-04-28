from PyQt5.QtWidgets import QMainWindow, QWidget, QLineEdit, QLabel, QPushButton, QFrame, QTableWidget
from PyQt5.Qt import QGridLayout, QHBoxLayout, QVBoxLayout

from core.agent import *
from core.exchange import *
from core.strategy import *
from api.dart import *
from api.kospi import *

class MainWindow(QFrame):
    def __init__(self):
        '''
        모든 모듈 여기에 load
        거래소 모듈
        api 모듈
        전략 모듈
        agent 모듈
        widget 띄우기
        레이아웃 만들기
        '''

        #
        super(MainWindow, self).__init__()
        self.InitUI()
        self.Initialize()

    def InitUI(self):
        self.__layout = QVBoxLayout()
        self.__upperRegion = UpperRegion()
        self.__lowerRegion = LowerRegion()

        self.__layout.addWidget(self.__upperRegion)
        self.__layout.addWidget(self.__lowerRegion)

        self.setLayout(self.__layout)

    def Initialize(self):
        pass


class UpperRegion(QWidget):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.__layout = QHBoxLayout()
        self.__statusDashboard = StatusDashboard()
        self.__portDashboard = PortfolioDashboard()
        self.__controlPanel = ControlPanel()

        self.__layout.addWidget(self.__statusDashboard)
        self.__layout.addWidget(self.__portDashboard)
        self.__layout.addWidget(self.__controlPanel)
        self.setLayout(self.__layout)


class LowerRegion(QWidget):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.__layout = QGridLayout()
        self.__infos = QLabel('infos')
        self.__strategy = QLabel('strategy')
        self.__table = RankTable()

        self.__layout.addWidget(self.__infos, 0, 0)
        self.__layout.addWidget(self.__strategy, 0, 1)
        self.__layout.addWidget(self.__table, 1, 0)
        self.setLayout(self.__layout)


class StatusDashboard(QFrame):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.__layout = QVBoxLayout()
        self.__layout.addWidget(QLabel('dashboard'))
        self.setLayout(self.__layout)


class PortfolioDashboard(QFrame):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.__layout = QVBoxLayout()
        self.__layout.addWidget(QLabel('diff'))
        self.setLayout(self.__layout)


class ControlPanel(QFrame):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.__layout = QVBoxLayout()
        self.__calcButton = QPushButton('calc')
        self.__execButton = QPushButton('exec')

        self.__layout.addWidget(self.__calcButton)
        self.__layout.addWidget(self.__execButton)

        self.setLayout(self.__layout)


class RankTable(QFrame):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.__layout = QVBoxLayout()
        self.__table = QTableWidget()

        self.__layout.addWidget(self.__table)

        self.setLayout(self.__layout)
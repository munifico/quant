from PyQt5.QtWidgets import QMainWindow

from core.agent import *
from core.exchange import *
from core.strategy import *
from api.dart import *
from api.kospi import *

class MainWindow(QMainWindow):
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
        self.Initialize()


    def Initialize(self):
        pass



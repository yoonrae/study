#사이사이 print() : console 로직 진행사항 확인용
#미완성 계산기
#python : 3.9
#pyqt : 5

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    _translate = QtCore.QCoreApplication.translate
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 600)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 79, 381, 511))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonsOnGrid(Form)
        self.display(Form)
        Form.setWindowTitle(Ui_Form._translate("Form", "Form"))
        QtCore.QMetaObject.connectSlotsByName(Form)

    def buttonsOnGrid(self, Form):
        self.buttonInstance(Form, 'C', 0, 2)
        self.buttonInstance(Form, '=', 0, 3)
        
        self.buttonInstance(Form, '7', 1, 0)
        self.buttonInstance(Form, '8', 1, 1)
        self.buttonInstance(Form, '9', 1, 2)
        self.buttonInstance(Form, '/', 1, 3)
        
        self.buttonInstance(Form, '4', 2, 0)
        self.buttonInstance(Form, '5', 2, 1)
        self.buttonInstance(Form, '6', 2, 2)
        self.buttonInstance(Form, '*', 2, 3)

        self.buttonInstance(Form, '1', 3, 0)
        self.buttonInstance(Form, '2', 3, 1)
        self.buttonInstance(Form, '3', 3, 2)
        self.buttonInstance(Form, '-', 3, 3)

        self.buttonInstance(Form, 'Del', 4, 0)
        self.buttonInstance(Form, '0', 4, 1)
        self.buttonInstance(Form, '.', 4, 2)
        self.buttonInstance(Form, '+', 4, 3)


    def buttonInstance(self, Form, txt, n0, n1):
        self.toolButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.toolButton.setMinimumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.toolButton.setFont(font)
        self.toolButton.setText(Ui_Form._translate("Form", txt))
        self.toolButton.setObjectName(txt)
        self.gridLayout.addWidget(self.toolButton, n0, n1, 1, 1)
        self.toolButton.clicked.connect(lambda: self.through_txt(txt))


    def through_txt(self, txt):
        print('press'+txt)        
        self.ch_Main(txt)
        #.sender()를 써서 받아오려고 했는데 계속 종료되어 아예 텍스트를 받아옴


    temp = ''
    operator = ['+','-','*','/','=']
    def ch_Main(self, txt):
        #입력한 텍스트 받기
        if txt != '=' and txt != 'Del':
            self.temp += txt
        
        #문자열 가장 앞에 0이 오면 지움
        if len(self.temp)>1:
            self.temp = self.temp.lstrip('0')

        #문자열이 0인 경우 0 입력해도 0추가 안되게
        if self.temp=='0' and txt=='0':
            self.temp='0'        

        #Del 기능
        if txt=='Del':
            self.temp = self.temp[:-1]
        else:
            print('here is an Error - ch_Main Del')

        #Clear 기능
        if txt=='C':
            self.temp = '0'



        self.cal(txt)

    def cal(self, txt):    
        #'='누르면 계산
        if txt=='=':
            try:
                ans = eval(self.temp)
            except ZeroDivisionError:
                print("do not divide by zero")
                #에러는 받았는데 종료되는 문제
        
            self.answer = str(ans)
            print(self.answer)
            ansTemp = self.checkLastDotZero(self.answer)
            self.lineEdit.setText(ansTemp)
            self.temp = ansTemp
        else:
            self.lineEdit.setText(self.temp)

        #정답 나눗셈 할 때 나오는 .0 소수점 지우기
    def checkLastDotZero(self, ans):
        ans = ans.strip(".0")
        return ans

    def display(self, Form):
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setText(QtCore.QCoreApplication.translate("Form", u"0", None))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
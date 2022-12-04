from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):   
    def __init__(self, Form):
        self._translate = QtCore.QCoreApplication.translate
        Form.setObjectName("Form")
        Form.resize(400, 600)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 79, 381, 511))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonsOnGrid()
        self.display(Form)
        Form.setWindowTitle(self._translate("Form", "Custom Calc"))
        QtCore.QMetaObject.connectSlotsByName(Form)

    def buttonsOnGrid(self):
        buttons = ['C','=','7','8','9','/','4','5','6','*','1','2','3','-','Del','0','.','+']
        x = 0
        for i in range(5):  
            for j in range(4):
                if i == 0:
                    j = j + 2
                    if j == 4:
                        break
                self.buttonInstance(buttons[x], i, j)
                x = x + 1

    def buttonInstance(self, txt, n0, n1):
        self.toolButton = QtWidgets.QToolButton(self.gridLayoutWidget)
        self.toolButton.setMinimumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.toolButton.setFont(font)
        self.toolButton.setText(self._translate("Form", txt))
        self.toolButton.setObjectName(txt)
        self.gridLayout.addWidget(self.toolButton, n0, n1, 1, 1)
        self.toolButton.clicked.connect(lambda: self.throw_txt(txt))
        
    def throw_txt(self, txt):
        calc = Calc()
        temp = self.lineEdit.text()
        answer = calc.ch_Main(txt, temp)
        self.lineEdit.setText(answer)
        
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

class Calc():
    txtlist = ''   

    def __init__(self):
        self.operator = ['+','-','*','/','.','=']

    def ch_Main(self, txt, answer):
        answer = self.resetAnswerTryAgain(txt, answer)
        if txt == 'Del':
            answer = self.delete(answer)
        elif txt == 'C':
            answer = self.clear(answer)
        elif txt == '=':
            if answer == '0':
                answer = '0'
            elif len(answer) == 1 and answer not in self.operator:
                answer = answer
            elif answer[-1] in self.operator:
                answer = self.delete(answer)                
            else:
                answer = self.calculator(txt, answer)
        else:
            answer += txt
            answer = self.removeTwiceOperator(txt, answer)
            answer = self.removeFirstZero(answer)
            answer = self.zeroZero(txt, answer)
        return answer

    def removeTwiceOperator(self, txt, answer):
        if len(answer)>1:
            if answer[-2] in self.operator and answer[-1] in self.operator:
                answer = answer[:-2] + txt
        return answer

    def delete(self, temp):
        temp = temp[:-1]
        if temp == '':
            temp = '0'
        return temp        

    def clear(self, temp):
        temp = '0'
        return temp

    def resetAnswerTryAgain(self, txt, answer):
        Calc.txtlist += txt
        if len(Calc.txtlist)>1:
            if Calc.txtlist[-2] == '=' and Calc.txtlist[-1] not in self.operator:
                answer = '0'
                Calc.txtlist = ''
        return answer

    def zeroDivisionError(self, answer):
        if answer[-2] == '/' and answer[-1] =='0':
            answer = '0'
        return answer

    def zeroZero(self, txt, answer):
        if txt == '0' and answer == '0':
            answer = '0'
        elif txt == '0' and answer == '':
            answer = '0'
        elif answer == '':
            answer = '0'
        return answer
    
    def removeFirstZero(self, answer):
        if len(answer)>0 and answer[0] == '0':
            if answer[1] == '.':
                pass
            else:
                answer = answer.lstrip('0')
        return answer

    def calculator(self, txt, answer):
        answer = self.zeroDivisionError(answer)
        answer = self.removeFirstZero(answer)        
        answer = eval(answer)
        answer = str(answer)
        answer = self.checkLastDotZero(answer)
        answer = self.zeroZero(txt, answer)
        return answer

    def checkLastDotZero(self, ans):
        ans = ans.rstrip(".0")
        return ans

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form(Form)
    Form.show()
    sys.exit(app.exec_())
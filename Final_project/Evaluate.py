from PyQt5 import QtCore, QtGui, QtWidgets
import score


class Ui_Evaluate(object):


    def __init__(self,itemsList):
        self.itemsTextList = itemsList
        self.p_list = score.Score_calculator((self.itemsTextList))
        # self.total_points = [total+=i for i in self.p_list]
        # print(total_points)

    def calculate(self):
        total = 0
        # print(self.itemsTextList)
        self.p_list = map(int, self.p_list)
        for i in self.p_list:
            total = total+i
        self.total_points = total
        # print(self.total_points)
        self.label_4.setText(str(self.total_points))


    def setupUi(self, Evaluate):
        Evaluate.setObjectName("Evaluate")
        Evaluate.resize(615, 499)
        self.label = QtWidgets.QLabel(Evaluate)
        self.label.setGeometry(QtCore.QRect(100, 0, 421, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.cb_1 = QtWidgets.QComboBox(Evaluate)
        self.cb_1.setGeometry(QtCore.QRect(60, 60, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cb_1.setFont(font)
        self.cb_1.setObjectName("cb_1")
        self.cb_1.addItem("")
        self.cb_1.addItem("")
        self.cb_1.addItem("")
        self.cb_1.addItem("")
        self.cb_1.addItem("")
        self.cb_1.setItemText(4, "")
        self.cb_2 = QtWidgets.QComboBox(Evaluate)
        self.cb_2.setGeometry(QtCore.QRect(360, 60, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cb_2.setFont(font)
        self.cb_2.setObjectName("cb_2")
        self.cb_2.addItem("")
        self.cb_2.addItem("")
        self.cb_2.addItem("")
        self.cb_2.addItem("")
        self.cb_2.addItem("")
        self.cb_2.addItem("")
        self.cb_2.setItemText(5, "")
        self.line = QtWidgets.QFrame(Evaluate)
        self.line.setGeometry(QtCore.QRect(50, 40, 531, 20))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.list_1 = QtWidgets.QListWidget(Evaluate)
        self.list_1.setGeometry(QtCore.QRect(40, 140, 251, 281))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.list_1.setFont(font)
        self.list_1.setObjectName("list_1")
        item = QtWidgets.QListWidgetItem()

        self.list_1.addItems(self.itemsTextList)

        self.list_2 = QtWidgets.QListWidget(Evaluate)
        self.list_2.setGeometry(QtCore.QRect(340, 140, 241, 281))
        font = QtGui.QFont()
        font.setFamily("URW Gothic L")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.list_2.setFont(font)
        self.list_2.setObjectName("list_2")

        self.list_2.addItems(self.p_list)

        self.pb = QtWidgets.QPushButton(Evaluate)
        self.pb.setGeometry(QtCore.QRect(250, 440, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pb.setFont(font)
        self.pb.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.311316, y1:0.375, x2:0.658, y2:0.693, stop:0.603448 rgba(255, 92, 18, 221));\n"
"color: rgb(238, 238, 236);")
        self.pb.setObjectName("pb")
        self.line_2 = QtWidgets.QFrame(Evaluate)
        self.line_2.setGeometry(QtCore.QRect(40, 420, 541, 20))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.line_2.setFont(font)
        self.line_2.setStyleSheet("color: qlineargradient(spread:reflect, x1:0.311316, y1:0.375, x2:0.658, y2:0.693, stop:0.603448 rgba(0, 0, 0, 221));")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_2 = QtWidgets.QLabel(Evaluate)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Evaluate)
        self.label_3.setGeometry(QtCore.QRect(340, 110, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Evaluate)
        self.label_4.setGeometry(QtCore.QRect(420, 110, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.pb.clicked.connect(self.calculate)


        self.retranslateUi(Evaluate)
        QtCore.QMetaObject.connectSlotsByName(Evaluate)

    def retranslateUi(self, Evaluate):
        _translate = QtCore.QCoreApplication.translate
        Evaluate.setWindowTitle(_translate("Evaluate", "Form"))
        self.label.setText(_translate("Evaluate", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#c17d11;\">Evaluate the score of your team</span></p></body></html>"))
        self.cb_1.setItemText(0, _translate("Evaluate", "Select Team"))
        self.cb_1.setItemText(1, _translate("Evaluate", "Pegasis"))
        self.cb_1.setItemText(2, _translate("Evaluate", "Tigers"))
        self.cb_1.setItemText(3, _translate("Evaluate", "Rnagers"))
        self.cb_2.setItemText(0, _translate("Evaluate", "Select match"))
        self.cb_2.setItemText(1, _translate("Evaluate", "Match-1"))
        self.cb_2.setItemText(2, _translate("Evaluate", "Match-2"))
        self.cb_2.setItemText(3, _translate("Evaluate", "Match-3"))
        self.cb_2.setItemText(4, _translate("Evaluate", "Match-4"))
        self.pb.setText(_translate("Evaluate", "Calculate Score"))
        self.label_2.setText(_translate("Evaluate", "<html><head/><body><p align=\"center\">Players</p></body></html>"))
        self.label_3.setText(_translate("Evaluate", "<html><head/><body><p align=\"center\">Points   :</p></body></html>"))
        self.label_4.setText(_translate("Evaluate", "<html><head/><body><p align=\"center\">Nil</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Evaluate = QtWidgets.QWidget()
    ui = Ui_Evaluate()
    ui.setupUi(Evaluate)
    Evaluate.show()
    sys.exit(app.exec_())

# Import librarys
import sys
from csv import reader

from PyQt5 import QtCore, QtGui, QtWidgets
from problog import get_evaluatable
from problog.learning import lfi
from problog.logic import Term
from problog.program import PrologString


# Ui framework PyQt5
class Ui_Dialog(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 480, 113, 32))
        self.pushButton.setObjectName("pushButton")

        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 120, 711, 341))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)

        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)

        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)

        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)

        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)

        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)

        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)

        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_8)

        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_9)

        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_10)

        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_11)

        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)

        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)

        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)

        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)

        self.lineEdit_7 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)

        self.lineEdit_8 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)

        self.lineEdit_9 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)

        self.lineEdit_10 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_10)

        self.lineEdit_11 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.lineEdit_11)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 540, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")

        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(350, 510, 91, 31))
        self.lcdNumber.setObjectName("lcdNumber")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(340, 540, 118, 23))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(290, 60, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setItalic(False)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_2.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.clickMethod)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "SUBMIT"))
        self.label.setText(_translate("MainWindow", "Fixed acidity"))
        self.label_2.setText(_translate("MainWindow", "Volatile acidity"))
        self.label_3.setText(_translate("MainWindow", "Citric acid"))
        self.label_4.setText(_translate("MainWindow", "Residual sugar"))
        self.label_5.setText(_translate("MainWindow", "Chlorides"))
        self.label_6.setText(_translate("MainWindow", "Free Sulfur Dioxide"))
        self.label_7.setText(_translate("MainWindow", "Total Sulfur Dioxide"))
        self.label_8.setText(_translate("MainWindow", "Density"))
        self.label_9.setText(_translate("MainWindow", "pH"))
        self.label_10.setText(_translate("MainWindow", "Sulphates"))
        self.label_11.setText(_translate("MainWindow", "Alcohol"))
        self.pushButton_2.setText(_translate("MainWindow", "exit"))
        self.label_12.setText(_translate("MainWindow", "Wine Quality Predictor"))

    def clickMethod(self):
        global trainedModel
        inEvidence = []
        inData = ""

        # fixed Acidity input

        fixAc = float(self.lineEdit.text())

        if 8 < fixAc < 13:
            inEvidence.append((Term("fixAcidity"), True))
            inData = inData + "evidence(fixAcidity,true)."
        else:
            inEvidence.append((Term("fixAcidity"), False))
            inData = inData + "evidence(fixAcidity,false)."

        # volatile Acidity input

        volAc = float(self.lineEdit_2.text())
        if 0.3 < volAc < 0.5:
            inEvidence.append((Term("volAcidity"), True))
            inData = inData + "\nevidence(volAcidity,true)."
        else:
            inEvidence.append((Term("volAcidity"), False))
            inData = inData + "\nevidence(volAcidity,false)."

        # citric Acid input

        citr = float(self.lineEdit_3.text())
        if 0.3 < citr < 0.6:
            inEvidence.append((Term("citrAcid"), True))
            inData = inData + "\nevidence(citrAcid,true)."
        else:
            inEvidence.append((Term("citrAcid"), False))
            inData = inData + "\nevidence(citrAcid,false)."

        # residual Sugar input

        rs = float(self.lineEdit_4.text())
        if rs < 2.5:
            inEvidence.append((Term("resSugar"), True))
            inData = inData + "\nevidence(resSugar,true)."
        else:
            inEvidence.append((Term("resSugar"), False))
            inData = inData + "\nevidence(resSugar,false)."

        # chloridies input

        chl = float(self.lineEdit_5.text())
        if 0.07 < chl < 0.086:
            inEvidence.append((Term("chloridies"), True))
            inData = inData + "\nevidence(chloridies,true)."
        else:
            inEvidence.append((Term("chloridies"), False))
            inData = inData + "\nevidence(chloridies,false)."

        # freeSulfurDioxide input

        fsd = float(self.lineEdit_6.text())
        if 6 < fsd < 20:
            inEvidence.append((Term("freeSulfurDioxide"), True))
            inData = inData + "\nevidence(freeSulfurDioxide,true)."
        else:
            inEvidence.append((Term("freeSulfurDioxide"), False))
            inData = inData + "\nevidence(freeSulfurDioxide,false)."

        # totalSulfurDeoxide input

        tsf = float(self.lineEdit_7.text())
        if tsf > 35:
            inEvidence.append((Term("totalSulfurDeoxide"), True))
            inData = inData + "\nevidence(totalSulfurDeoxide,true)."
        else:
            inEvidence.append((Term("totalSulfurDeoxide"), False))
            inData = inData + "\nevidence(totalSulfurDeoxide,false)."

        # density input

        den = float(self.lineEdit_8.text())
        if den < 0.996435:
            inEvidence.append((Term("density"), True))
            inData = inData + "\nevidence(density,true)."
        else:
            inEvidence.append((Term("density"), False))
            inData = inData + "\nevidence(density,false)."

        # ph input

        ph = float(self.lineEdit_9.text())
        if 3.2 < ph < 3.4:
            inEvidence.append((Term("ph"), True))
            inData = inData + "\nevidence(ph,true)."
        else:
            inEvidence.append((Term("ph"), False))
            inData = inData + "\nevidence(ph,false)."

        # sulphates input

        sul = float(self.lineEdit_10.text())
        if sul > 0.65:
            inEvidence.append((Term("sulphates"), True))
            inData = inData + "\nevidence(sulphates,true)."
        else:
            inEvidence.append((Term("sulphates"), False))
            inData = inData + "\nevidence(sulphates,false)."

        # alcohol input

        alc = float(self.lineEdit_11.text())
        if alc > 11.4:
            inEvidence.append((Term("alcohol"), True))
            inData = inData + "\nevidence(alcohol,true)."
        else:
            inEvidence.append((Term("alcohol"), False))
            inData = inData + "\nevidence(alcohol,false)."

        inEvidence.append((Term("quality"), True))
        inData = inData + "\nevidence(quality,true)."

        # Final query to find the wine quality prediction
        inData = inData + "\nquery(good)."

        # User model is the evidences from the user inputs above
        inData = trainedModel + inData
        # print(inData)

        # Evaluate the new model with the evidences with Problog
        p_usermodel = PrologString(inData)
        result = get_evaluatable().create_from(p_usermodel).evaluate()

        cnt = 0
        for query, value in result.items():
            if cnt == 0:
                probMessage = "Probability to be a good wine: " + format(value, ".0%") + "\n"
                cnt = cnt + 1
            else:
                probMessage = probMessage + "Error " + format(value, ".0%") + "\n"
                cnt = 0
        print(probMessage)
        self.lcdNumber.display(format(int(value * 100)) + "%")
        self.progressBar.setValue(int(value * 100))


def readDatasetFile():
    global quality
    global evidence
    global trainedModel

    with open('winequality-red.csv', 'r') as read_obj:
        csvScanner = reader(read_obj)
        header = next(csvScanner)

        if header != None:

            for row in csvScanner:
                evidenceList = []

                finalModel = "quality:-"

                # fixed Acidity column
                if row[0] == '':
                    fixAc = 0
                else:
                    fixAc = float(row[0])
                if 8 < fixAc < 13:
                    finalModel = finalModel + "fixAcidity,"
                    evidenceList.append((Term("fixAcidity"), True, None))
                else:
                    finalModel = finalModel + "\+fixAcidity,"
                    evidenceList.append((Term("fixAcidity"), False, None))

                # volatile Acidity column
                if row[1] == '':
                    volAc = 0
                else:
                    volAc = float(row[1])

                if 0.3 < volAc < 0.5:
                    finalModel = finalModel + "volAcidity,"
                    evidenceList.append((Term("volAcidity"), True, None))
                else:
                    finalModel = finalModel + "\+volAcidity,"
                    evidenceList.append((Term("volAcidity"), False, None))

                # citric Acid column
                if row[2] == '':
                    citr = 0
                else:
                    citr = float(row[2])

                if 0.3 < citr < 0.6:
                    finalModel = finalModel + "citrAcid,"
                    evidenceList.append((Term("citrAcid"), True, None))
                else:
                    finalModel = finalModel + "\+citrAcid,"
                    evidenceList.append((Term("citrAcid"), False, None))

                # residual Sugar column
                if row[3] == '':
                    res = 0
                else:
                    res = float(row[3])

                if res < 2.5:
                    finalModel = finalModel + "resSugar,"
                    evidenceList.append((Term("resSugar"), True, None))
                else:
                    finalModel = finalModel + "\+resSugar,"
                    evidenceList.append((Term("resSugar"), False, None))

                # chlorides column
                if row[4] == '':
                    chlo = 0
                else:
                    chlo = float(row[4])

                if 0.07 < chlo < 0.086:
                    finalModel = finalModel + "chloridies,"
                    evidenceList.append((Term("chloridies"), True, None))
                else:
                    finalModel = finalModel + "\+chloridies,"
                    evidenceList.append((Term("chloridies"), False, None))

                # free sulfur dioxide column
                if row[5] == '':
                    fsd = 0
                else:
                    fsd = float(row[5])

                if 6 < fsd < 20:
                    finalModel = finalModel + "freeSulfurDioxide,"
                    evidenceList.append((Term("freeSulfurDioxide"), True, None))
                else:
                    finalModel = finalModel + "\+freeSulfurDioxide,"
                    evidenceList.append((Term("freeSulfurDioxide"), False, None))

                # total sulfur deoxide column
                if row[6] == '':
                    tsd = 0
                else:
                    tsd = float(row[6])

                if tsd > 35:
                    finalModel = finalModel + "totalSulfurDeoxide,"
                    evidenceList.append((Term("totalSulfurDeoxide"), True, None))
                else:
                    finalModel = finalModel + "\+totalSulfurDeoxide,"
                    evidenceList.append((Term("totalSulfurDeoxide"), False, None))

                # density column
                if row[7] == '':
                    den = 0
                else:
                    den = float(row[7])

                if den < 0.996435:
                    finalModel = finalModel + "density,"
                    evidenceList.append((Term("density"), True, None))
                else:
                    finalModel = finalModel + "\+density,"
                    evidenceList.append((Term("density"), False, None))

                # ph column
                if row[8] == '':
                    pH = 0
                else:
                    pH = float(row[8])

                if 3.2 < pH < 3.4:
                    finalModel = finalModel + "ph,"
                    evidenceList.append((Term("ph"), True, None))
                else:
                    finalModel = finalModel + "\+ph,"
                    evidenceList.append((Term("ph"), False, None))

                # sulphates column
                if row[9] == '':
                    sul = 0
                else:
                    sul = float(row[9])

                if sul > 0.65:
                    finalModel = finalModel + "sulphates,"
                    evidenceList.append((Term("sulphates"), True, None))
                else:
                    finalModel = finalModel + "\+sulphates,"
                    evidenceList.append((Term("sulphates"), False, None))

                # alcohol column
                if row[10] == '':
                    alc = 0
                else:
                    alc = float(row[10])

                if alc > 11.4:
                    finalModel = finalModel + "alcohol,"
                    evidenceList.append((Term("alcohol"), True, None))
                else:
                    finalModel = finalModel + "\+alcohol,"
                    evidenceList.append((Term("alcohol"), False, None))

                if float(row[11]) == '':
                    pred = 0
                else:
                    pred = float(row[11])

                if pred >= 6:
                    finalModel = finalModel + "good."
                    evidenceList.append((Term("good"), True, None))
                else:
                    finalModel = finalModel + "\+good."
                    evidenceList.append((Term("good"), False, None))

                finalModel = finalModel.replace(",.", ".")

                quality.add(finalModel)
                evidence.append(evidenceList)


class MainWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)


if __name__ == "__main__":

    quality = set()
    evidence = list()

    readDatasetFile()

    termList = list(quality)
    termList.sort()

    # Creating the Learning Model
    model = """"""
    model = model + "t(_)::fixAcidity.\n"
    model = model + "t(_)::volAcidity.\n"
    model = model + "t(_)::citrAcid.\n"
    model = model + "t(_)::resSugar.\n"
    model = model + "t(_)::chloridies.\n"
    model = model + "t(_)::freeSulfurDioxide.\n"
    model = model + "t(_)::totalSulfurDeoxide.\n"
    model = model + "t(_)::density.\n"
    model = model + "t(_)::ph.\n"
    model = model + "t(_)::sulphates.\n"
    model = model + "t(_)::alcohol.\n"
    model = model + "t(_)::good.\n"

    for y in range(len(termList)):
        if y != (len(termList) - 1):
            model = model + termList[y] + "\n"
        else:
            model = model + termList[y]

    # Evaluate the learning model
    score, weights, atoms, iteration, lfi_problem = lfi.run_lfi(PrologString(model), evidence)
    trainedModel = lfi_problem.get_model()

    app = QtWidgets.QApplication(sys.argv)

    # Run the main window function for UI
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

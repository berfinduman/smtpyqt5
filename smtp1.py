# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\berfi\OneDrive\Masaüstü\pyqt5ödev\smtp1.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(970, 648)
        Form.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Form.setAcceptDrops(False)
        Form.setToolTipDuration(2)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 40, 871, 571))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setTabletTracking(False)
        self.label_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_6.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_6.setStyleSheet("font: 28pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setClearButtonEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5, 0, QtCore.Qt.AlignTop)
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 810, 295))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_5.setGeometry(QtCore.QRect(0, 0, 811, 361))
        self.lineEdit_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_5.setTabletTracking(True)
        self.lineEdit_5.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lineEdit_5.setToolTipDuration(2)
        self.lineEdit_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_5.setAutoFillBackground(False)
        self.lineEdit_5.setStyleSheet("font: 18pt \"MS PGothic\";")
        self.lineEdit_5.setFrame(True)
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_5.setDragEnabled(False)
        self.lineEdit_5.setReadOnly(False)
        self.lineEdit_5.setClearButtonEnabled(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.addWidget(self.scrollArea)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_2.addWidget(self.lineEdit_4)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form",
                                        "<html><head/><body><p align=\"center\"><span style=\" vertical-align:sub;\">Mail Yollama</span></p></body></html>"))
        self.label.setText(_translate("Form", "From:   "))
        self.lineEdit.setPlaceholderText(_translate("Form", "asdasf@gmail.com"))
        self.label_2.setText(_translate("Form", " To:      "))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "asdasfto@gmail.com"))
        self.label_4.setText(_translate("Form", "Subject:"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Subject"))
        self.label_5.setText(_translate("Form", "Main:    "))
        self.lineEdit_5.setAccessibleDescription(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "İçerik"))
        self.pushButton_3.setText(_translate("Form", "+"))
        self.pushButton.setText(_translate("Form", "Taslak olarak kaydet"))
        self.pushButton_2.setText(_translate("Form", "Dosya Aç"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "password"))
        self.pushButton_4.setText(_translate("Form", "GÖNDER"))
        self.pushButton.clicked.connect(self.savethefile)
        self.pushButton_2.clicked.connect(self.openthefile)
        self.pushButton_4.clicked.connect(self.send)
        self.pushButton_3.clicked.connect(self.tol)
        self.list = []
    def savethefile(self):

        if len(self.list)==0:

            dosya_ismi = QtWidgets.QFileDialog()

            dosya_ismi0 = dosya_ismi.getSaveFileName(os.getenv("HOME"))

            with open(dosya_ismi0[0], "w") as self.file1:
                self.a = f"""
                {self.label.text()} : {self.lineEdit.text()}\n
                {self.label_2.text()} : {self.lineEdit_2.text()}\n
                {self.label_4.text()} : {self.lineEdit_3.text()}\n
                {self.label_5.text()} : {self.lineEdit_5.text()}\n
                """
                self.file1.write(self.a)
        else:
            self.list.append(self.lineEdit_2.text())
            dosya_ismi = QtWidgets.QFileDialog()

            dosya_ismi0 = dosya_ismi.getSaveFileName(os.getenv("HOME"))

            with open(dosya_ismi0[0], "w") as self.file1:
                self.a = f"""
                {self.label.text()} : {self.lineEdit.text()}\n
                {self.label_2.text()} : {self.list}\n
                {self.label_4.text()} : {self.lineEdit_3.text()}\n
                {self.label_5.text()} : {self.lineEdit_5.text()}\n
                """
                self.file1.write(self.a)


    def openthefile(self):

        self.dosya_ismi1 = QtWidgets.QFileDialog.getOpenFileName(os.getenv("HOME"))
        with open(self.dosya_ismi1[0], "r") as self.file2:
            self.b = self.file2.read()
            self.lineEdit_5.setText(self.b)
    def tol(self):

        a=self.lineEdit_2.text()

        self.list.append(a)

        self.lineEdit_2.clear()


    def send(self):


        if len(self.list)==0:

            self.mesaj: MIMEMultipart = MIMEMultipart()
            if len(self.lineEdit.text())==0:
                self.lineEdit.setPlaceholderText("Mailinizi Giriniz!")

            else:
                self.mesaj["From"] = self.lineEdit.text()
            if len(self.lineEdit_2.text()) == 0:
                self.lineEdit_2.setPlaceholderText("Yollamak istediğiniz maili giriniz!")
            else:

                self.mesaj["To"] = self.lineEdit_2.text()
            if len(self.lineEdit_3.text()) == 0:
                self.lineEdit_3.setPlaceholderText("Konu Giriniz!")
            else:
                self.mesaj["Subject"] = self.lineEdit_3.text()

            self.a = self.lineEdit_5.text()
            if len(self.a)==0:
                self.lineEdit_5.setPlaceholderText("Mesajını yazınız!")
            self.mesaj_govdesi = MIMEText(self.a, "plain")
            if len(self.lineEdit_4.text())==0:
                self.lineEdit_4.setPlaceholderText("Enter Password!")
            self.mesaj.attach(self.mesaj_govdesi)

            try:

                self.mail = smtplib.SMTP("smtp.gmail.com", 587)

                self.mail.ehlo()

                self.mail.starttls()

                self.mail.login(self.mesaj["From"], self.lineEdit_4.text())

                self.mail.sendmail(self.mesaj["From"], self.mesaj["To"], self.mesaj.as_string())
                print("Mail başarıyla gönderildi")
                self.mail.close()
            except:
                sys.stderr.write("Bir sorun oluştu!")
                sys.stderr.flush()

        else:

            self.list.append(self.lineEdit_2.text())
            print(self.list)
            self.mesaj: MIMEMultipart = MIMEMultipart()
            if len(self.lineEdit.text()) == 0:
                self.lineEdit.setPlaceholderText("Mailinizi Giriniz!")

            else:
                self.mesaj["From"] = self.lineEdit.text()
            if len(self.lineEdit_3.text()) == 0:
                self.lineEdit_3.setPlaceholderText("Konu Giriniz!")
            else:
                self.mesaj["Subject"] = self.lineEdit_3.text()

            self.a = self.lineEdit_5.text()
            if len(self.a) == 0:
                self.lineEdit_5.setPlaceholderText("Mesajını yazınız!")
            self.mesaj_govdesi = MIMEText(self.a, "plain")
            if len(self.lineEdit_4.text()) == 0:
                self.lineEdit_4.setPlaceholderText("Enter Password!")
            self.mesaj.attach(self.mesaj_govdesi)

            self.tolist=self.list
            try:


                self.mail = smtplib.SMTP("smtp.gmail.com", 587)

                self.mail.ehlo()

                self.mail.starttls()

                self.mail.login(self.mesaj["From"], self.lineEdit_4.text())

                self.mail.sendmail(self.mesaj["From"], self.tolist, self.mesaj.as_string())
                print("Mailler başarıyla gönderildi")
                self.mail.close()
            except:
                sys.stderr.write("Bir sorun oluştu!")
                sys.stderr.flush()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
# #######################################################################
# ################### Modules ###########################################
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import bcrypt
import uuid
import validator_collection
from PyQt5.QtWidgets import QMainWindow, QMessageBox
# ########################################################################
# ########################################################################


class Signup(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(832, 602)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 832, 571))
        self.frame.setStyleSheet("#frame{\n" "background-color:#7A3AF8;\n" "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Signup = QtWidgets.QWidget(self.frame)
        self.Signup.setGeometry(QtCore.QRect(0, 0, 411, 571))
        self.Signup.setStyleSheet(
            "#createBtn {\n"
            "background-color: #7A3AF8;\n"
            "color: white;\n"
            "border: none;\n"
            "padding: 8px 16px;\n"
            "border-radius:5px;\n"
            "}\n"
            "QPushButton#createBtn:hover {\n"
            "    background-color: #9D63FF;\n"
            "}\n"
            "\n"
            "#Signup{\n"
            "background-color:white;\n"
            "}\n"
            "QLineEdit#Name,\n"
            "QLineEdit#Password,\n"
            "QLineEdit#Email,\n"
            "QLineEdit#Phone{\n"
            "border: 1px solid #7B7878;\n"
            "border-radius:5px;\n"
            "padding: 8px;\n"
            "font-size:14px;\n"
            "}\n"
            "QLineEdit#Name:focus,\n"
            "QLineEdit#Password:focus,\n"
            "QLineEdit#Email:focus,\n"
            "QLineEdit#Phone:focus{\n"
            "border-color:#570BED;\n"
            "}\n"
            "QLineEdit#Phone{\n"
            "    QValidator::error {\n"
            "            border: 1px solid red; /* Border color for invalid input */\n"
            "      }\n"
            "}\n"
            ""
        )
        self.Signup.setObjectName("Signup")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.Signup)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 130, 331, 335))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.verticalLayout.addWidget(self.name_label)
        self.Name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        self.verticalLayout.addWidget(self.Name)
        self.email_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.email_label.setFont(font)
        self.email_label.setObjectName("email_label")
        self.verticalLayout.addWidget(self.email_label)
        self.Email = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.Email.setFont(font)
        self.Email.setObjectName("Email")
        self.verticalLayout.addWidget(self.Email)
        self.psswd_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.psswd_label.setFont(font)
        self.psswd_label.setObjectName("psswd_label")
        self.verticalLayout.addWidget(self.psswd_label)
        self.Password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.Password.setFont(font)
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.verticalLayout.addWidget(self.Password)
        self.phone_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.phone_label.setFont(font)
        self.phone_label.setObjectName("phone_label")
        self.verticalLayout.addWidget(self.phone_label)
        self.Phone = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.Phone.setFont(font)
        self.Phone.setCursorPosition(0)
        self.Phone.setObjectName("Phone")
        self.verticalLayout.addWidget(self.Phone)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.verticalLayout.addItem(spacerItem)
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("#checkBox{\n" "font-size:13px;\n" "}")
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.label_6 = QtWidgets.QLabel(self.Signup)
        self.label_6.setGeometry(QtCore.QRect(40, 50, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.createBtn = QtWidgets.QPushButton(self.Signup)
        self.createBtn.setGeometry(QtCore.QRect(40, 490, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.createBtn.setFont(font)
        self.createBtn.setStyleSheet("")
        self.createBtn.setObjectName("createBtn")
        self.label_7 = QtWidgets.QLabel(self.Signup)
        self.label_7.setGeometry(QtCore.QRect(40, 80, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.Login = QtWidgets.QPushButton(self.Signup)
        self.Login.setGeometry(QtCore.QRect(90, 537, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.Login.setFont(font)
        self.Login.setStyleSheet(
            "#Login{\n"
            "border:none;\n"
            "}\n"
            "#Login:hover{\n"
            "text-decoration: underline;\n"
            "}"
        )
        self.Login.setObjectName("Login")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(450, 40, 361, 351))
        self.label.setStyleSheet("image:url(:/vector/healthcare.png)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(480, 420, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(520, 485, 221, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(600, 500, 81, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.name_label.setText(_translate("MainWindow", "Your name"))
        self.Name.setPlaceholderText(_translate("MainWindow", "Your name"))
        self.email_label.setText(_translate("MainWindow", "Your e-mail"))
        self.Email.setPlaceholderText(_translate("MainWindow", "name@gmail.com"))
        self.psswd_label.setText(_translate("MainWindow", "Password"))
        self.Password.setPlaceholderText(
            _translate("MainWindow", "at least 8 characters")
        )
        self.phone_label.setText(_translate("MainWindow", "Phone Number"))
        self.Phone.setInputMask(_translate("MainWindow", "(000) 000-0000"))
        self.checkBox.setText(
            _translate(
                "MainWindow", "By creating an account you agree our terms of use"
            )
        )
        self.label_6.setText(_translate("MainWindow", "Sign up."))
        self.createBtn.setText(_translate("MainWindow", "Create account"))
        self.label_7.setText(
            _translate(
                "MainWindow",
                "Give us some of your information to free\n" "access to fieldly.",
            )
        )
        self.Login.setText(_translate("MainWindow", "Already have an account? Log in"))
        self.label_2.setText(
            _translate(
                "MainWindow",
                '<html><head/><body><p><span style=" color:#ffffff;">SYNCING HEALTH. BETTER LIFE.</span></p></body></html>',
            )
        )


# Define the stylesheet
STYLESHEET = """
    QMessageBox {
        background-color: #f0f0f0;
        color: #333;
    }
    QMessageBox QLabel {
        color: #333;
    }
    QMessageBox QPushButton {
        background-color: #ccc;
        color: #333;
        padding: 5px;
        border-radius: 3px;
    }
"""


class User(Signup, QMainWindow):
    def __init__(self):
        super().__init__()
        self.window = QtWidgets.QMainWindow()
        self.setupUi(self.window)
        self.setWindowTitle('LifeSync')
        # slots
        self.createBtn.clicked.connect(self.perform_signup)

        # Database
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()

        self.users_Table = "CREATE TABLE IF NOT EXISTS users(" \
                           "id INTEGER PRIMARY KEY AUTOINCREMENT," \
                           "name TEXT NOT NULL," \
                           "email TEXT NOT NULL UNIQUE," \
                           "password TEXT NOT NULL," \
                           "phone TEXT NOT NULL," \
                           "session_id TEXT)"
        self.cursor.execute(self.users_Table)
        self.conn.commit()
        #

    # function to generate unique Id for User
    @staticmethod
    def generate_unique_id():
        return str(uuid.uuid4())

    # function to hash the user's password
    @staticmethod
    def hash_password(password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    # Function to signup new user
    def perform_signup(self):
        password = self.Password.text()
        name = self.Name.text()
        email = self.Email.text()
        phone = self.Phone.text().replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
        user_id = self.generate_unique_id()
        hashed_password = self.hash_password(password)

        msg_box = QMessageBox()
        msg_box.setStyleSheet(STYLESHEET)

        if len(password) >= 8 and name and validator_collection.is_email(email) and phone:
            try:
                self.cursor.execute("INSERT INTO users (name, email, password, phone, session_id) VALUES (?,?,?,?,?)",
                                    (name, email, hashed_password, phone, user_id))
                self.conn.commit()
                msg_box.setWindowTitle('Notice')
                msg_box.setText("Amazing! You are now registered!")
            except sqlite3.IntegrityError:
                msg_box.setWindowTitle('Email Error')
                msg_box.setText("Email already exists. Please use a different email.")
            except Exception as e:
                print("An error occurred:", e)
        else:
            msg_box.setWindowTitle('Error')
            msg_box.setText("Please fill in all fields and your email must be valid\nSame that your password at least 8")

        msg_box.addButton(QMessageBox.Ok)
        msg_box.exec_()

        # Close the database connection
        self.conn.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = User()
    ui.window.show()
    sys.exit(app.exec_())

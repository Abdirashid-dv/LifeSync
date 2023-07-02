# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1565, 935)
        MainWindow.setMinimumSize(QtCore.QSize(1565, 935))
        MainWindow.setMaximumSize(QtCore.QSize(1565, 935))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.menu_widget = QtWidgets.QWidget(self.centralwidget)
        self.menu_widget.setGeometry(QtCore.QRect(-30, 0, 271, 941))
        self.menu_widget.setStyleSheet("#menu_widget{\n"
                                       "background-color:#3E4862;\n"
                                       "border-radius: 30px;\n"
                                       "}\n"
                                       "#Reminders,\n"
                                       "#Nearest_h,\n"
                                       "#LifeSync,\n"
                                       "#Exit{\n"
                                       "background-color:#3E4862;\n"
                                       "color:#A4B0C3;\n"
                                       "border:none;\n"
                                       "}\n"
                                       "#Reminders:hover,\n"
                                       "#Nearest_h:hover,\n"
                                       "#LifeSync:hover,\n"
                                       "#Exit:hover{\n"
                                       "background-color:#2F3850;\n"
                                       "color:#FFF;\n"
                                       "border-radius:15px;\n"
                                       "}\n"
                                       "QPushButton:focus {\n"
                                       "    outline: none;\n"
                                       "}\n"
                                       "")
        self.menu_widget.setObjectName("menu_widget")
        self.Reminders = QtWidgets.QPushButton(self.menu_widget)
        self.Reminders.setGeometry(QtCore.QRect(54, 200, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.Reminders.setFont(font)
        self.Reminders.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Reminders.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Reminders.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/bell.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Reminders.setIcon(icon)
        self.Reminders.setIconSize(QtCore.QSize(20, 17))
        self.Reminders.setObjectName("Reminders")
        self.Nearest_h = QtWidgets.QPushButton(self.menu_widget)
        self.Nearest_h.setGeometry(QtCore.QRect(54, 300, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.Nearest_h.setFont(font)
        self.Nearest_h.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Nearest_h.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/navigation.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Nearest_h.setIcon(icon1)
        self.Nearest_h.setIconSize(QtCore.QSize(20, 17))
        self.Nearest_h.setAutoDefault(False)
        self.Nearest_h.setDefault(False)
        self.Nearest_h.setFlat(False)
        self.Nearest_h.setObjectName("Nearest_h")
        self.yasli_amclar = QtWidgets.QLabel(self.menu_widget)
        self.yasli_amclar.setGeometry(QtCore.QRect(20, 700, 251, 291))
        self.yasli_amclar.setStyleSheet("image: url(:/icons/icons/person.svg);")
        self.yasli_amclar.setText("")
        self.yasli_amclar.setObjectName("yasli_amclar")
        self.logo_frame = QtWidgets.QFrame(self.menu_widget)
        self.logo_frame.setGeometry(QtCore.QRect(50, 20, 201, 81))
        self.logo_frame.setStyleSheet("#logo_frame{\n"
                                      "background-color: rgba(79, 99, 215,0.9);\n"
                                      "border-radius:15px;\n"
                                      "}")
        self.logo_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo_frame.setObjectName("logo_frame")
        self.label_13 = QtWidgets.QLabel(self.logo_frame)
        self.label_13.setGeometry(QtCore.QRect(5, 2, 91, 76))
        self.label_13.setStyleSheet("image: url(:/icons/icons/logo.svg);")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.logo_frame)
        self.label_14.setGeometry(QtCore.QRect(160, 5, 31, 71))
        self.label_14.setStyleSheet("\n"
                                    "#label_14{\n"
                                    "image: url(:/icons/icons/menu-vertical.png);\n"
                                    "background-color: #9CC2F4;\n"
                                    "border-radius: 10px;\n"
                                    "}")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.LifeSync = QtWidgets.QPushButton(self.menu_widget)
        self.LifeSync.setGeometry(QtCore.QRect(54, 250, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.LifeSync.setFont(font)
        self.LifeSync.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LifeSync.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/message-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LifeSync.setIcon(icon2)
        self.LifeSync.setIconSize(QtCore.QSize(20, 17))
        self.LifeSync.setFlat(False)
        self.LifeSync.setObjectName("LifeSync")
        self.Exit = QtWidgets.QPushButton(self.menu_widget)
        self.Exit.setGeometry(QtCore.QRect(54, 630, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.Exit.setFont(font)
        self.Exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Exit.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/log-out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Exit.setIcon(icon3)
        self.Exit.setIconSize(QtCore.QSize(20, 17))
        self.Exit.setAutoDefault(False)
        self.Exit.setDefault(False)
        self.Exit.setFlat(False)
        self.Exit.setObjectName("Exit")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(220, 0, 1351, 941))
        self.stackedWidget.setStyleSheet("QPushButton:focus {\n"
                                         "    outline: none;\n"
                                         "}\n"
                                         "")
        self.stackedWidget.setObjectName("stackedWidget")
        self.Reminder = QtWidgets.QWidget()
        self.Reminder.setStyleSheet("#Reminder{\n"
                                    "background-color: #DCE1EB;\n"
                                    "}\n"
                                    "#UserData{\n"
                                    "background-color: rgba(79, 99, 215,0.5);\n"
                                    "border-radius: 10px;\n"
                                    "}\n"
                                    "")
        self.Reminder.setObjectName("Reminder")
        self.UserData = QtWidgets.QWidget(self.Reminder)
        self.UserData.setGeometry(QtCore.QRect(40, 20, 761, 361))
        self.UserData.setStyleSheet("/* DateTime - QDateTimeEdit */\n"
                                    "QDateTimeEdit{\n"
                                    "  border: 1px solid #ccc;\n"
                                    "  border-radius: 4px;\n"
                                    "  padding: 8px 4px;\n"
                                    "  background-color: #fff;\n"
                                    "  color: #000;\n"
                                    "}\n"
                                    "\n"
                                    "QDateTimeEdit::drop-down {\n"
                                    "  subcontrol-origin: padding;\n"
                                    "  subcontrol-position: right;\n"
                                    "  width: 25px;\n"
                                    "  border-left-width: 1px;\n"
                                    "  border-left-color: #ccc;\n"
                                    "  border-left-style: solid;\n"
                                    "  background-color: #f5f5f5;\n"
                                    "  selection-color: #fff;\n"
                                    "  selection-background-color: #333;\n"
                                    "    image: url(:/icons/icons/calendar.svg);\n"
                                    "padding-left:3px;\n"
                                    "}\n"
                                    "\n"
                                    "/* Dosage, Duration, Frequency, MedicationName - QLineEdit */\n"
                                    "#Dosage,\n"
                                    "#Duration,\n"
                                    "#Duration,\n"
                                    "#MedicationName,\n"
                                    "#Search_input{\n"
                                    "  border: 1px solid #ccc;\n"
                                    "  border-radius: 5px;\n"
                                    "  padding: 8px 4px;\n"
                                    "  background-color: #fff;\n"
                                    "  color: #000;\n"
                                    "}\n"
                                    "#Priority,\n"
                                    "#Frequency{\n"
                                    "padding:8px 4px\n"
                                    "}\n"
                                    "\n"
                                    "QLineEdit:focus {\n"
                                    "  border-color: #555;\n"
                                    "}\n"
                                    "#Dosage::hover,\n"
                                    "#Search_input:hover,\n"
                                    "#Duration::hover,\n"
                                    "#Frequency::hover,\n"
                                    "#Duration::hover,\n"
                                    "#MedicationName::hover {\n"
                                    "border-color: #7A3AF8;\n"
                                    "}\n"
                                    "QPushButton {\n"
                                    "    background-color:#6B66EB ; /* Green */\n"
                                    "    border: none;\n"
                                    "    color: white;\n"
                                    "    padding: 10px 24px;\n"
                                    "    text-align: center;\n"
                                    "    text-decoration: none;\n"
                                    "    display: inline-block;\n"
                                    "    font-size: 16px;\n"
                                    "    margin: 4px 2px;\n"
                                    "    border-radius: 5px;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "    background-color:#4942E4; /* Darker green */\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed {\n"
                                    "    background-color: #11009E; /* Even darker green */\n"
                                    "}\n"
                                    "QComboBox QAbstractItemView {\n"
                                    "    background-color: #FFFFFF; /* White */\n"
                                    "    border: 1px solid #CCCCCC; /* Light gray */\n"
                                    "    selection-background-color: #6B66EB; /* Light gray for the selected item */\n"
                                    "    outline: none;\n"
                                    "}\n"
                                    "")
        self.UserData.setObjectName("UserData")
        self.formLayoutWidget = QtWidgets.QWidget(self.UserData)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 10, 471, 339))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#27374D")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.MedicationName = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.MedicationName.setObjectName("MedicationName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.MedicationName)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:#27374D")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.Dosage = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Dosage.setObjectName("Dosage")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Dosage)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:#27374D")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:#27374D")
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.Duration = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Duration.setClearButtonEnabled(True)
        self.Duration.setObjectName("Duration")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Duration)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:#27374D")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.Priority = QtWidgets.QComboBox(self.formLayoutWidget)
        self.Priority.setObjectName("Priority")
        self.Priority.addItem("")
        self.Priority.addItem("")
        self.Priority.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.Priority)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:#27374D")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:#27374D")
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.Refill = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.Refill.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 6, 3), QtCore.QTime(0, 0, 0)))
        self.Refill.setCalendarPopup(True)
        self.Refill.setObjectName("Refill")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.Refill)
        self.Frequency = QtWidgets.QComboBox(self.formLayoutWidget)
        self.Frequency.setStyleSheet("")
        self.Frequency.setObjectName("Frequency")
        self.Frequency.addItem("")
        self.Frequency.addItem("")
        self.Frequency.addItem("")
        self.Frequency.addItem("")
        self.Frequency.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Frequency)
        self.Time = QtWidgets.QTimeEdit(self.formLayoutWidget)
        self.Time.setStyleSheet("QTimeEdit::up-button {\n"
                                "    subcontrol-origin: border;\n"
                                "    subcontrol-position: top right;\n"
                                "    image: url(:/icons/icons/chevron-up.svg);\n"
                                "    width: 25px;\n"
                                "    height: 22px;\n"
                                "\n"
                                "}\n"
                                "\n"
                                "QTimeEdit::down-button {\n"
                                "    subcontrol-origin: border;\n"
                                "    subcontrol-position: bottom right;\n"
                                "    image: url(:/icons/icons/chevron-down.svg);\n"
                                "    width: 25px;\n"
                                "    height: 22px;\n"
                                "}\n"
                                "")
        self.Time.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 6, 3), QtCore.QTime(0, 0, 0)))
        self.Time.setCalendarPopup(True)
        self.Time.setObjectName("Time")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.Time)
        self.Search_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Search_input.setObjectName("Search_input")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.Search_input)
        self.Add = QtWidgets.QPushButton(self.UserData)
        self.Add.setGeometry(QtCore.QRect(550, 10, 181, 47))
        self.Add.setStyleSheet("")
        self.Add.setObjectName("Add")
        self.Update = QtWidgets.QPushButton(self.UserData)
        self.Update.setGeometry(QtCore.QRect(550, 60, 181, 47))
        self.Update.setCheckable(False)
        self.Update.setObjectName("Update")
        self.Delete = QtWidgets.QPushButton(self.UserData)
        self.Delete.setGeometry(QtCore.QRect(550, 110, 181, 47))
        self.Delete.setObjectName("Delete")
        self.List = QtWidgets.QPushButton(self.UserData)
        self.List.setGeometry(QtCore.QRect(550, 160, 181, 47))
        self.List.setObjectName("List")
        self.Search = QtWidgets.QPushButton(self.UserData)
        self.Search.setGeometry(QtCore.QRect(550, 210, 181, 47))
        self.Search.setObjectName("Search")
        self.label_18 = QtWidgets.QLabel(self.UserData)
        self.label_18.setGeometry(QtCore.QRect(30, 313, 113, 36))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color:#27374D")
        self.label_18.setObjectName("label_18")
        self.tableWidget = QtWidgets.QTableWidget(self.Reminder)
        self.tableWidget.setGeometry(QtCore.QRect(40, 400, 1281, 521))
        self.tableWidget.setStyleSheet("QTableWidget::item:selected {\n"
                                       "    background-color: rgba(79, 99, 215,0.5);\n"
                                       "    color: #FFFFFF; /* Change this color to the desired text color */\n"
                                       "}\n"
                                       "")
        self.tableWidget.setRowCount(13)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(178)
        self.Calendar = QtWidgets.QWidget(self.Reminder)
        self.Calendar.setGeometry(QtCore.QRect(820, 20, 501, 361))
        self.Calendar.setStyleSheet("#Calendar{\n"
                                    "background-color: rgba(79, 99, 215,0.5);\n"
                                    "border-radius: 10px;\n"
                                    "}")
        self.Calendar.setObjectName("Calendar")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.Calendar)
        self.calendarWidget.setGeometry(QtCore.QRect(11, 15, 481, 331))
        self.calendarWidget.setStyleSheet("/* Calendar Widget Styles */\n"
                                          "QCalendarWidget {\n"
                                          "  background-color: #F8F6F4;\n"
                                          "  font-family: Arial, sans-serif;\n"
                                          "  font-size: 14px;\n"
                                          "  border-radius: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "QCalendarWidget QHeaderView {\n"
                                          "  background-color: #F8F6F4;\n"
                                          "  font-weight: bold;\n"
                                          "}\n"
                                          "\n"
                                          "QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
                                          "  background-color: #F8F6F4;\n"
                                          "    border: 2px solid  #F8F6F4;\n"
                                          "    border-bottom: 0px;\n"
                                          "    border-top-left-radius: 10px;\n"
                                          "    border-top-right-radius: 10px;\n"
                                          "}\n"
                                          "\n"
                                          "QCalendarWidget QToolButton {\n"
                                          "  background-color: transparent;\n"
                                          "}\n"
                                          "\n"
                                          "QCalendarWidget QTableView {\n"
                                          "  selection-background-color: #A0B9E3;\n"
                                          "  alternate-background-color: #E3E4F3;\n"
                                          "outline: 0px;\n"
                                          "    border: 2px solid #F8F6F4;\n"
                                          "    border-top: 0px;\n"
                                          "    border-bottom-left-radius: 10px;\n"
                                          "    border-bottom-right-radius: 10px;\n"
                                          "}\n"
                                          "QCalendarWidget QTableView::item:selected {\n"
                                          "  color: #fff;\n"
                                          "}\n"
                                          "QCalendarWidget QTableView QTableCornerButton::section {\n"
                                          "  background-color: #F8F6F4;\n"
                                          "}\n"
                                          "\n"
                                          "QCalendarWidget QTableView QHeaderView::section {\n"
                                          "  background-color: #F8F6F4;\n"
                                          "}\n"
                                          "\n"
                                          "QCalendarWidget QSpinBox {\n"
                                          "  border: 1px solid #9BA3EB;\n"
                                          "  padding: 1px;\n"
                                          "  border-radius: 10px;\n"
                                          "}\n"
                                          "\n"
                                          "QCalendarWidget QSpinBox:hover {\n"
                                          "  border-color: #A0B9E3;\n"
                                          "}\n"
                                          "\n"
                                          "QCalendarWidget QSpinBox::up-button, QCalendarWidget QSpinBox::down-button {\n"
                                          "  subcontrol-origin: border;\n"
                                          "  subcontrol-position: top right;\n"
                                          "  width: 15px;\n"
                                          "  border-left-width: 1px;\n"
                                          "}\n"
                                          "\n"
                                          "QCalendarWidget QSpinBox::up-arrow, QCalendarWidget QSpinBox::down-arrow {\n"
                                          "  image: url(up_down_arrow.png);\n"
                                          "}\n"
                                          "QCalendarWidget QToolButton#qt_calendar_prevmonth {\n"
                                          "/* delete default icons */\n"
                                          "  qproperty-icon: none; \n"
                                          "margin-left:2px;\n"
                                          "border-radius: 5px;\n"
                                          "width: 50px;\n"
                                          "min-height: 20px;\n"
                                          "max-height:20px;\n"
                                          "image: url(:/icons/icons/arrow-left-circle.svg);\n"
                                          "}\n"
                                          "\n"
                                          "QCalendarWidget QToolButton#qt_calendar_nextmonth {\n"
                                          "qproperty-icon: none; \n"
                                          "margin-right:2px;\n"
                                          "border-radius: 5px;\n"
                                          "width: 50px;\n"
                                          "min-height: 20px;\n"
                                          "max-height:20px;\n"
                                          "image:url(:/icons/icons/arrow-right-circle.svg);\n"
                                          "}\n"
                                          "\n"
                                          "QCalendarWidget QToolButton#qt_calendar_prevyear {\n"
                                          "qproperty-icon: none;\n"
                                          "image: url(:/icons/icons/chevrons-right.svg);\n"
                                          "}\n"
                                          "\n"
                                          "QCalendarWidget QToolButton#qt_calendar_nextyear {\n"
                                          "qproperty-icon: none;\n"
                                          " image: url(:/icons/icons/chevrons-left.svg);\n"
                                          "}\n"
                                          "\n"
                                          "QCalendarWidget QMenu {\n"
                                          "  background-color: #F8F6F4;\n"
                                          "}\n"
                                          "\n"
                                          "QCalendarWidget QMenu::item {\n"
                                          "  padding: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "QCalendarWidget QMenu::item:selected {\n"
                                          "  background-color: #A0B9E3;\n"
                                          "\n"
                                          "}\n"
                                          "\n"
                                          "QCalendarWidget QMenu::icon {\n"
                                          "  width: 12px;\n"
                                          "  height: 12px;\n"
                                          "  margin-right: 5px;\n"
                                          "}\n"
                                          "/* Style for month and yeat buttons #################################### */\n"
                                          "\n"
                                          "#qt_calendar_yearbutton {\n"
                                          "    color: #000;\n"
                                          "    margin:5px;\n"
                                          "    border-radius: 4px;\n"
                                          "    font-size: 13px;\n"
                                          "    padding:4px 6px;\n"
                                          "}\n"
                                          "\n"
                                          " #qt_calendar_monthbutton {\n"
                                          "    width: 110px;\n"
                                          "    color: #000;\n"
                                          "    font-size: 13px;\n"
                                          "    margin:5px 15px;\n"
                                          "    border-radius: 5px;\n"
                                          "    padding:4px 2px;\n"
                                          "}\n"
                                          "\n"
                                          "\n"
                                          "\n"
                                          "/* Style for year input lineEdit ######################################*/\n"
                                          "#qt_calendar_yearedit {\n"
                                          "    min-width:56px;\n"
                                          "    color: #000;\n"
                                          "    background: transparent;\n"
                                          "    font-size: 13px;\n"
                                          "    padding:0px 8px;\n"
                                          "}\n"
                                          "\n"
                                          "\n"
                                          "/* Style for year change buttons ######################################*/\n"
                                          "\n"
                                          "#qt_calendar_yearedit::up-button { \n"
                                          "    image: url(:/icons/icons/chevrons-right.svg);\n"
                                          "    subcontrol-position: right;\n"
                                          "}\n"
                                          "\n"
                                          "#qt_calendar_yearedit::down-button { \n"
                                          "    image: url(:/icons/icons/chevrons-left.svg);\n"
                                          "    subcontrol-position: left; \n"
                                          "}\n"
                                          "\n"
                                          "#qt_calendar_yearedit::down-button, \n"
                                          "#qt_calendar_yearedit::up-button {\n"
                                          "    width:15px;\n"
                                          "    padding: 0px 5px;\n"
                                          "    border-radius:3px;\n"
                                          "}\n"
                                          "\n"
                                          "\n"
                                          "\n"
                                          "")
        self.calendarWidget.setObjectName("calendarWidget")
        self.stackedWidget.addWidget(self.Reminder)
        self.Chatbot = QtWidgets.QWidget()
        self.Chatbot.setStyleSheet("#Chatbot{\n"
                                   "background-color:#DCE1EB;\n"
                                   "}")
        self.Chatbot.setObjectName("Chatbot")
        self.frame = QtWidgets.QFrame(self.Chatbot)
        self.frame.setGeometry(QtCore.QRect(20, 0, 1321, 921))
        self.frame.setStyleSheet("#frame{\n"
                                 "image: url(:/icons/icons/WorldMap.svg);\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.chat_layout = QtWidgets.QWidget(self.frame)
        self.chat_layout.setGeometry(QtCore.QRect(150, 70, 1031, 841))
        self.chat_layout.setStyleSheet("#chat_layout{\n"
                                       "background-color:rgba(62, 72, 98,0.7);\n"
                                       "border-radius:20px;\n"
                                       "}")
        self.chat_layout.setObjectName("chat_layout")
        self.option = QtWidgets.QFrame(self.chat_layout)
        self.option.setGeometry(QtCore.QRect(210, 50, 651, 141))
        self.option.setStyleSheet("#option{\n"
                                  "background-color:rgba(62, 72, 98,0.9);\n"
                                  "border-radius:15px;\n"
                                  "}")
        self.option.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.option.setFrameShadow(QtWidgets.QFrame.Raised)
        self.option.setObjectName("option")
        self.label_16 = QtWidgets.QLabel(self.option)
        self.label_16.setGeometry(QtCore.QRect(220, 20, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: #DCE1EB;")
        self.label_16.setObjectName("label_16")
        self.Useroption = QtWidgets.QComboBox(self.option)
        self.Useroption.setGeometry(QtCore.QRect(80, 60, 491, 31))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.Useroption.setFont(font)
        self.Useroption.setStyleSheet("QComboBox QAbstractItemView {\n"
                                      "    background-color: #FFFFFF; /* White */\n"
                                      "    border: 1px solid #CCCCCC; /* Light gray */\n"
                                      "       selection-background-color: #6B66EB; /* Light gray for the selected item */\n"
                                      "    outline: none;\n"
                                      "\n"
                                      "}\n"
                                      "#Useroption{\n"
                                      "padding: 4px 8px;\n"
                                      "background-color:#A4B0C3;\n"
                                      "color: rgb(62, 72, 98);\n"
                                      "border-radius:4px;\n"
                                      "\n"
                                      "}\n"
                                      "QComboBox::down-arrow {\n"
                                      "    image: url(:/icons/icons/chevrons-down.svg);\n"
                                      "    width: 25px;\n"
                                      "    height: 25px;\n"
                                      "}\n"
                                      "QComboBox::drop-down {\n"
                                      "    subcontrol-origin: padding;\n"
                                      "    subcontrol-position: top right;\n"
                                      "    width: 30px;\n"
                                      "\n"
                                      "    border-left-width: 1px;\n"
                                      "    border-left-color: darkgray;\n"
                                      "    border-left-style: solid;\n"
                                      "    border-top-right-radius: 3px;\n"
                                      "    border-bottom-right-radius: 3px;\n"
                                      "\n"
                                      "    padding-left: 2px;\n"
                                      " outline: none;\n"
                                      "}")
        self.Useroption.setObjectName("Useroption")
        self.Useroption.addItem("")
        self.Useroption.addItem("")
        self.Useroption.addItem("")
        self.Useroption.addItem("")
        self.Useroption.addItem("")
        self.Useroption.addItem("")
        self.Useroption.addItem("")
        self.Useroption.addItem("")
        self.Useroption.addItem("")
        self.Question = QtWidgets.QWidget(self.chat_layout)
        self.Question.setGeometry(QtCore.QRect(210, 210, 651, 201))
        self.Question.setStyleSheet("#Question{\n"
                                    "background-color:rgba(62, 72, 98,0.9);\n"
                                    "border-radius:15px;\n"
                                    "}")
        self.Question.setObjectName("Question")
        self.usermsg = QtWidgets.QPlainTextEdit(self.Question)
        self.usermsg.setGeometry(QtCore.QRect(20, 20, 611, 131))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(9)
        self.usermsg.setFont(font)
        self.usermsg.setStyleSheet("#usermsg{\n"
                                   "background-color:#A4B0C3;\n"
                                   "border-radius:14px;\n"
                                   "padding: 4px 8px;\n"
                                   "}\n"
                                   "#usermsg:hover{\n"
                                   "color:rgb(62, 72, 98);\n"
                                   "}\n"
                                   "#usermsg QScrollBar {\n"
                                   "    background-color: #f2f2f2;\n"
                                   "    width: 8px;\n"
                                   "}")
        self.usermsg.setObjectName("usermsg")
        self.send = QtWidgets.QPushButton(self.Question)
        self.send.setGeometry(QtCore.QRect(490, 156, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        self.send.setFont(font)
        self.send.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.send.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.send.setStyleSheet("#send{\n"
                                "background-color:rgba(62, 72, 98,0.8);\n"
                                "color:#A4B0C3;\n"
                                "border:none;\n"
                                "border-radius:15px;\n"
                                "}\n"
                                "#send:hover{\n"
                                "background-color:#2F3850;\n"
                                "color:#FFF;\n"
                                "border-radius:15px;\n"
                                "}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/send.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send.setIcon(icon4)
        self.send.setIconSize(QtCore.QSize(20, 17))
        self.send.setObjectName("send")
        self.Result = QtWidgets.QWidget(self.chat_layout)
        self.Result.setGeometry(QtCore.QRect(209, 430, 651, 391))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Result.setFont(font)
        self.Result.setStyleSheet("#Result{\n"
                                  "background-color:rgba(62, 72, 98,0.9);\n"
                                  "border-radius:15px;\n"
                                  "}")
        self.Result.setObjectName("Result")
        self.BotAnswer = QtWidgets.QTextBrowser(self.Result)
        self.BotAnswer.setGeometry(QtCore.QRect(20, 20, 611, 351))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.BotAnswer.setFont(font)
        self.BotAnswer.setStyleSheet("#BotAnswer{\n"
                                     "background-color:#A4B0C3;\n"
                                     "border-radius:14px;\n"
                                     "}\n"
                                     "#BotAnswer QScrollBar {\n"
                                     "    background-color: #f2f2f2;\n"
                                     "    width: 8px;\n"
                                     "}\n"
                                     "QTextBrowser::verticalScrollBar {\n"
                                     "    background-color: rgba(62, 72, 98,0.9);\n"
                                     "    width: 12px; /* Set the width of the scrollbar */\n"
                                     "}\n"
                                     "\n"
                                     "QTextBrowser::horizontalScrollBar {\n"
                                     "    background-color: rgba(62, 72, 98,0.9);\n"
                                     "    height: 12px; /* Set the height of the scrollbar */\n"
                                     "}\n"
                                     "\n"
                                     "QTextBrowser::verticalScrollBar:hover,\n"
                                     "QTextBrowser::horizontalScrollBar:hover {\n"
                                     "    background-color: #4F63D7; /* Set the background color when hovering */\n"
                                     "}\n"
                                     "\n"
                                     "QTextBrowser::verticalScrollBar::handle,\n"
                                     "QTextBrowser::horizontalScrollBar::handle {\n"
                                     "    background-color: #4F63D7; /* Set the color of the scrollbar handle */\n"
                                     "    border-radius: 6px; /* Set the border radius of the scrollbar handle */\n"
                                     "}\n"
                                     "\n"
                                     "QTextBrowser::verticalScrollBar::handle:hover,\n"
                                     "QTextBrowser::horizontalScrollBar::handle:hover {\n"
                                     "    background-color: #4F63D7; /* Set the color of the scrollbar handle when hovering */\n"
                                     "}\n"
                                     "\n"
                                     "QTextBrowser::verticalScrollBar::sub-page,\n"
                                     "QTextBrowser::horizontalScrollBar::sub-page {\n"
                                     "    background-color: none; /* Set the background color of the scrollable area */\n"
                                     "}\n"
                                     "\n"
                                     "QTextBrowser::verticalScrollBar::add-page,\n"
                                     "QTextBrowser::horizontalScrollBar::add-page {\n"
                                     "    background-color: none; /* Set the background color of the non-scrollable area */\n"
                                     "}\n"
                                     "")
        self.BotAnswer.setObjectName("BotAnswer")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(330, 20, 681, 41))
        font = QtGui.QFont()
        font.setFamily("Dosis SemiBold")
        font.setPointSize(15)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color:#0A0C18;")
        self.label_15.setObjectName("label_15")
        self.stackedWidget.addWidget(self.Chatbot)
        self.Nhospital = QtWidgets.QWidget()
        self.Nhospital.setStyleSheet("#Nhospital{\n"
                                     "background-color:#DCE1EB;\n"
                                     "}\n"
                                     "#UserForm{\n"
                                     "background-color: rgba(79, 99, 215,0.5);\n"
                                     "border-radius: 10px;\n"
                                     "}")
        self.Nhospital.setObjectName("Nhospital")
        self.UserForm = QtWidgets.QGroupBox(self.Nhospital)
        self.UserForm.setGeometry(QtCore.QRect(79, 47, 531, 381))
        font = QtGui.QFont()
        font.setFamily("Oswald")
        font.setPointSize(10)
        self.UserForm.setFont(font)
        self.UserForm.setStyleSheet("QGroupBox#UserForm{\n"
                                    "    border-radius: 20px;\n"
                                    "    padding: 5px;\n"
                                    "}\n"
                                    "\n"
                                    "QGroupBox:title {\n"
                                    "    subcontrol-origin: margin;\n"
                                    "    subcontrol-position: top left;\n"
                                    "    padding: 0 4px;\n"
                                    "    margin-left:13px;\n"
                                    "    color:#27374D;\n"
                                    "    margin-top:20px;\n"
                                    "}\n"
                                    "#Latitude,\n"
                                    "#Longitude{\n"
                                    "  border: 1px solid #ccc;\n"
                                    "  border-radius: 5px;\n"
                                    "  padding: 8px 4px;\n"
                                    "  background-color: #fff;\n"
                                    "  color: #000;\n"
                                    "}\n"
                                    "#Latitude:hover,\n"
                                    "#Longitude:hover{\n"
                                    "border-color: #7A3AF8;\n"
                                    "}\n"
                                    "")
        self.UserForm.setObjectName("UserForm")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.UserForm)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 70, 331, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(11)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:#27374D")
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.UserAddress = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.UserAddress.setMinimumSize(QtCore.QSize(0, 46))
        self.UserAddress.setStyleSheet("#UserAddress{\n"
                                       "  border: 1px solid #ccc;\n"
                                       "  border-radius: 5px;\n"
                                       "  padding: 8px 4px;\n"
                                       "  background-color: #fff;\n"
                                       "  color: #000;\n"
                                       "}\n"
                                       "#UserAddress:hover{\n"
                                       "border-color: #7A3AF8;\n"
                                       "}")
        self.UserAddress.setObjectName("UserAddress")
        self.verticalLayout.addWidget(self.UserAddress)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color:#27374D")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout.addWidget(self.label_17)
        self.GetData = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.GetData.setMinimumSize(QtCore.QSize(55, 59))
        self.GetData.setStyleSheet("QPushButton {\n"
                                   "    background-color:#6B66EB ; /* Green */\n"
                                   "    border: none;\n"
                                   "    color: white;\n"
                                   "    padding: 10px 24px;\n"
                                   "    text-align: center;\n"
                                   "    text-decoration: none;\n"
                                   "    display: inline-block;\n"
                                   "    font-size: 16px;\n"
                                   "    margin: 4px 2px;\n"
                                   "    border-radius: 5px;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover {\n"
                                   "    background-color:#4942E4; /* Darker green */\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:pressed {\n"
                                   "    background-color: #11009E; /* Even darker green */\n"
                                   "}\n"
                                   "QComboBox QAbstractItemView {\n"
                                   "    background-color: #FFFFFF; /* White */\n"
                                   "    border: 1px solid #CCCCCC; /* Light gray */\n"
                                   "    selection-background-color: #6B66EB; /* Light gray for the selected item */\n"
                                   "    outline: none;\n"
                                   "}")
        self.GetData.setObjectName("GetData")
        self.verticalLayout.addWidget(self.GetData)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Condensed")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:#27374D")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.Find = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Find.setMinimumSize(QtCore.QSize(0, 59))
        self.Find.setStyleSheet("QPushButton {\n"
                                "    background-color:#6B66EB ; /* Green */\n"
                                "    border: none;\n"
                                "    color: white;\n"
                                "    padding: 10px 24px;\n"
                                "    text-align: center;\n"
                                "    text-decoration: none;\n"
                                "    display: inline-block;\n"
                                "    font-size: 16px;\n"
                                "    margin: 4px 2px;\n"
                                "    border-radius: 5px;\n"
                                "}\n"
                                "\n"
                                "QPushButton:hover {\n"
                                "    background-color:#4942E4; /* Darker green */\n"
                                "}\n"
                                "\n"
                                "QPushButton:pressed {\n"
                                "    background-color: #11009E; /* Even darker green */\n"
                                "}\n"
                                "QComboBox QAbstractItemView {\n"
                                "    background-color: #FFFFFF; /* White */\n"
                                "    border: 1px solid #CCCCCC; /* Light gray */\n"
                                "    selection-background-color: #6B66EB; /* Light gray for the selected item */\n"
                                "    outline: none;\n"
                                "}")
        self.Find.setObjectName("Find")
        self.verticalLayout.addWidget(self.Find)
        self.result = QtWidgets.QWidget(self.Nhospital)
        self.result.setGeometry(QtCore.QRect(710, 390, 601, 401))
        self.result.setStyleSheet("#result{\n"
                                  "background-color:rgba(79, 99, 215,0.5);\n"
                                  "border-radius: 20px;\n"
                                  "}")
        self.result.setObjectName("result")
        self.textBrowser = QtWidgets.QTextBrowser(self.result)
        self.textBrowser.setGeometry(QtCore.QRect(30, 90, 531, 191))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.label_10 = QtWidgets.QLabel(self.result)
        self.label_10.setGeometry(QtCore.QRect(30, 40, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Oswald")
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:#27374D")
        self.label_10.setObjectName("label_10")
        self.OpenLocation = QtWidgets.QPushButton(self.result)
        self.OpenLocation.setGeometry(QtCore.QRect(30, 290, 161, 61))
        self.OpenLocation.setStyleSheet("QPushButton {\n"
                                        "    background-color:#6B66EB ; /* Green */\n"
                                        "    border: none;\n"
                                        "    color: white;\n"
                                        "    padding: 10px 24px;\n"
                                        "    text-align: center;\n"
                                        "    text-decoration: none;\n"
                                        "    display: inline-block;\n"
                                        "    font-size: 16px;\n"
                                        "    margin: 4px 2px;\n"
                                        "    border-radius: 5px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    background-color:#4942E4; /* Darker green */\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: #11009E; /* Even darker green */\n"
                                        "}\n"
                                        "QComboBox QAbstractItemView {\n"
                                        "    background-color: #FFFFFF; /* White */\n"
                                        "    border: 1px solid #CCCCCC; /* Light gray */\n"
                                        "    selection-background-color: #6B66EB; /* Light gray for the selected item */\n"
                                        "    outline: none;\n"
                                        "}")
        self.OpenLocation.setObjectName("OpenLocation")
        self.label_11 = QtWidgets.QLabel(self.Nhospital)
        self.label_11.setGeometry(QtCore.QRect(526, 153, 311, 251))
        self.label_11.setStyleSheet("image: url(:/icons/icons/location.svg);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.guide = QtWidgets.QWidget(self.Nhospital)
        self.guide.setGeometry(QtCore.QRect(80, 480, 531, 401))
        self.guide.setStyleSheet("#guide{\n"
                                 "background-color:rgba(79, 99, 215,0.5);\n"
                                 "border-radius: 20px;\n"
                                 "}")
        self.guide.setObjectName("guide")
        self.Guide_text = QtWidgets.QTextEdit(self.guide)
        self.Guide_text.setGeometry(QtCore.QRect(20, 110, 491, 241))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(8)
        self.Guide_text.setFont(font)
        self.Guide_text.setStyleSheet("#Guide_text{\n"
                                      "background-color:rgba(79, 99, 215,0.2);\n"
                                      "border-radius:10px;\n"
                                      "padding:4px 5px;\n"
                                      "color:#0A0C18;\n"
                                      "}")
        self.Guide_text.setReadOnly(True)
        self.Guide_text.setOverwriteMode(True)
        self.Guide_text.setObjectName("Guide_text")
        self.label_12 = QtWidgets.QLabel(self.guide)
        self.label_12.setGeometry(QtCore.QRect(20, 20, 491, 71))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.label_11.raise_()
        self.UserForm.raise_()
        self.result.raise_()
        self.guide.raise_()
        self.stackedWidget.addWidget(self.Nhospital)
        self.stackedWidget.raise_()
        self.menu_widget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Reminders.setText(_translate("MainWindow", "  Reminders"))
        self.Nearest_h.setText(_translate("MainWindow", " Nearest Hospital"))
        self.LifeSync.setText(_translate("MainWindow", "   LifeSync Bot"))
        self.Exit.setText(_translate("MainWindow", " EXIT"))
        self.label.setText(_translate("MainWindow", "Medication Name"))
        self.MedicationName.setPlaceholderText(_translate("MainWindow", "Enter Medication Name"))
        self.label_2.setText(_translate("MainWindow", "Dosage"))
        self.Dosage.setPlaceholderText(_translate("MainWindow", "Dosage (e.g., 10 mg)"))
        self.label_3.setText(_translate("MainWindow", "Frequency"))
        self.label_4.setText(_translate("MainWindow", "Duration"))
        self.Duration.setPlaceholderText(_translate("MainWindow", "Duration (e.g., 7 days)"))
        self.label_5.setText(_translate("MainWindow", "Priority"))
        self.Priority.setItemText(0, _translate("MainWindow", "High"))
        self.Priority.setItemText(1, _translate("MainWindow", "Medium"))
        self.Priority.setItemText(2, _translate("MainWindow", "Low"))
        self.label_6.setText(_translate("MainWindow", "Time"))
        self.label_7.setText(_translate("MainWindow", "Refill Reminder"))
        self.Frequency.setItemText(0, _translate("MainWindow", "Once daily"))
        self.Frequency.setItemText(1, _translate("MainWindow", "Twice daily"))
        self.Frequency.setItemText(2, _translate("MainWindow", "Three times daily"))
        self.Frequency.setItemText(3, _translate("MainWindow", "Once every two days"))
        self.Frequency.setItemText(4, _translate("MainWindow", "Once weekly"))
        self.Search_input.setPlaceholderText(_translate("MainWindow", "Enter Medication Name"))
        self.Add.setText(_translate("MainWindow", "ADD"))
        self.Update.setText(_translate("MainWindow", "UPDATE"))
        self.Delete.setText(_translate("MainWindow", "DELETE"))
        self.List.setText(_translate("MainWindow", "LIST"))
        self.Search.setText(_translate("MainWindow", "SEARCH"))
        self.label_18.setText(_translate("MainWindow", "Search"))
        self.label_16.setText(_translate("MainWindow", "Please select an option:"))
        self.Useroption.setItemText(0, _translate("MainWindow", "Ask for Information"))
        self.Useroption.setItemText(1, _translate("MainWindow", "Request Medication Advice"))
        self.Useroption.setItemText(2, _translate("MainWindow", "Ask about Medication Side Effects"))
        self.Useroption.setItemText(3, _translate("MainWindow", "Ask for Dosage Instructions"))
        self.Useroption.setItemText(4, _translate("MainWindow", "Ask for Medication Storage Recommendations"))
        self.Useroption.setItemText(5, _translate("MainWindow", "Inquire about Medication Precautions or Warnings"))
        self.Useroption.setItemText(6, _translate("MainWindow", "Request Medication Formulations or Alternatives"))
        self.Useroption.setItemText(7, _translate("MainWindow", "Report Medication Adverse Reactions"))
        self.Useroption.setItemText(8, _translate("MainWindow", "Report Medication Effectiveness or Lack Thereof"))
        self.usermsg.setPlaceholderText(_translate("MainWindow", "Send a massege."))
        self.send.setText(_translate("MainWindow", "  Send"))
        self.label_15.setText(
            _translate("MainWindow", "Welcome to Your Virtual Health Assistant! How can I assist you today?"))
        self.UserForm.setTitle(_translate("MainWindow", "Nearest Health Centers"))
        self.label_8.setText(_translate("MainWindow", "Enter Your Address"))
        self.UserAddress.setPlaceholderText(_translate("MainWindow", "Enter your location address"))
        self.label_17.setText(_translate("MainWindow", "To Find Nearest Pharmacy"))
        self.GetData.setText(_translate("MainWindow", "Find Nearest Pharmacy"))
        self.label_9.setText(_translate("MainWindow", "To Find Nearest Hospital"))
        self.Find.setText(_translate("MainWindow", "Find Nearest Hospital"))
        self.label_10.setText(_translate("MainWindow", "Here Is Your Nearest Hospital/Pharmacy Data:"))
        self.OpenLocation.setText(_translate("MainWindow", "Open Location"))
        self.Guide_text.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Open Sans\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">1. Enter the address of your location in the input bar.</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">2. Two buttons will be displayed: &quot;Find Nearest Pharmacy&quot; and &quot;Find Nearest Hospital.&quot; Click on the appropriate button based on the data you need.</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">If you choose &quot;Find Nearest Pharmacy&quot;: </span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">4. The TextBrowser will process your location and display the nearest pharmacies based on your address. </span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">5. You can view the names, addresses, and distances of the nearby pharmacies.</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">If you choose &quot;Find Nearest Hospital&quot;:</span></p>\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">6. The TextBrowser will process your location and display the nearest hospitals based on your address. <br />7.You can view the names, addresses, and distances of the nearby hospitals.</span></p></body></html>"))
        self.label_12.setText(
            _translate("MainWindow", "User Guide: Finding Nearest Pharmacy or Hospital Based on Address"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

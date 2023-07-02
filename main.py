#################################################################
from Login.login import Login
from Signup.signup import User
from home_pg.reminders_main import ReminderDb
from Nearesthealthcenter.nearesthc_finder import HospitalFinder
import config
import openai
import sqlite3
import sys
import bcrypt
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from geopy.geocoders import GoogleV3
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from home_pg import resource_rc
from Login import source_rc
from Signup import logo_rc

#########################################################################
# Api Keys                                                              #
openai.api_key = config.API_KEYS.get("API_KEY1")  #
google_api_key = config.API_KEYS.get("API_KEY2")  #
#########################################################################

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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.msg_box = QMessageBox()
        self.msg_box.setStyleSheet(STYLESHEET)

        self.session_id = None

        # Database 'Login/Signup'
        self.conn = sqlite3.connect("users.db")
        self.cursor = self.conn.cursor()

        # MAIN CLASSES OR MODULES
        self.main_wn = QMainWindow()
        self.ui_login = Login()
        self.ui_signup = User()
        self.ui_main = ReminderDb()
        self.timer = QTimer()
        self.ui_login.setupUi(self.main_wn)

        # FIST SLOTS
        self.ui_login.SignupBtn.clicked.connect(self.showSignup)
        self.ui_login.SigninBtn.clicked.connect(self.perform_login)

        # User Data
        self.name = None
        self.email = None
        self.latitude = None
        self.longitude = None

    def show(self):
        self.main_wn.show()

    def showLogin(self):
        self.ui_login.setupUi(self.main_wn)
        self.ui_login.SignupBtn.clicked.connect(self.showSignup)
        self.ui_login.SigninBtn.clicked.connect(self.perform_login)

    def showSignup(self):
        self.ui_signup.setupUi(self.main_wn)
        self.ui_signup.createBtn.clicked.connect(self.ui_signup.perform_signup)
        self.ui_signup.Login.clicked.connect(self.showLogin)

    @staticmethod
    def verify_password(password, hashed_password):
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))

    def perform_login(self):
        email = self.ui_login.Username.text()
        password = self.ui_login.Password.text()

        self.cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = self.cursor.fetchone()

        self.msg_box = QMessageBox()
        self.msg_box.setStyleSheet(STYLESHEET)

        if user:
            hashed_password = user[3]
            if self.verify_password(password, hashed_password):
                self.session_id = self.ui_signup.generate_unique_id()
                self.update_session_id(user[0], self.session_id)
                self.ui_login.statusbar.showMessage(
                    "Session ID:" + str(self.session_id)
                )
                self.name = user[1]
                self.email = user[2]
                message = "Login successful!\nSession ID: {}".format(self.session_id)
                self.msg_box.setWindowTitle("Login Status")
                self.msg_box.setText(message)
                self.is_login_in(self.session_id)
            else:
                self.msg_box.setWindowTitle("Login Error")
                self.msg_box.setText("Invalid email or password.")
        else:
            self.msg_box.setWindowTitle("Login Error")
            self.msg_box.setText("Invalid email or password.")

        self.msg_box.addButton(QMessageBox.Ok)
        self.msg_box.exec_()

    # Function to update the session ID for a user
    def update_session_id(self, user_id, session_id):
        self.cursor.execute(
            "UPDATE users SET session_id=? WHERE id=?", (session_id, user_id)
        )
        self.conn.commit()

    def is_login_in(self, session_id):
        self.cursor.execute("SELECT * FROM users WHERE session_id=?", (session_id,))
        user = self.cursor.fetchone()
        if user:
            self.main_window()
        else:
            self.msg_box.setWindowTitle("Notice")
            self.msg_box.setText("User is not logged in.")

    def main_window(self):
        # MAIN WINDOW SIGNALS
        self.ui_main.setupUi(self.main_wn)
        self.ui_main.Reminders.clicked.connect(self.showReminders)
        self.ui_main.LifeSync.clicked.connect(self.showLifeSync)
        self.ui_main.Nearest_h.clicked.connect(self.showNearest_h)

        # Signals for Nearest Hospital Page
        self.ui_main.Find.clicked.connect(self.find_nearest_hospital)
        self.ui_main.GetData.clicked.connect(self.find_nearest_pharmacy)
        self.ui_main.OpenLocation.clicked.connect(
            lambda: self.open_location_in_browser(self.latitude, self.longitude)
        )

        # Signal for Chatbot Page
        self.ui_main.send.clicked.connect(self.chatbot)

        # Signals For Reminder Page
        self.ui_main.Add.clicked.connect(self.ui_main.Add_db)
        self.ui_main.List.clicked.connect(self.ui_main.list_it)
        self.ui_main.Delete.clicked.connect(self.ui_main.delete_it)
        self.ui_main.Search.clicked.connect(self.ui_main.search_it)
        self.ui_main.Update.clicked.connect(self.ui_main.update_it)

        self.ui_main.tableWidget.itemSelectionChanged.connect(self.ui_main.fill)

        # Notification checking every Second
        self.timer.timeout.connect(self.ui_main.check_medication_reminders)
        self.timer.start(1000)  # updating every second

        # Email Sending
        try:
            self.timer.timeout.connect(
                lambda: self.ui_main.send_reminder_email(self.email, self.name)
            )
            self.timer.start(2000)  # updating every second
        except Exception as e:
            print(f"The error is {e}")

        # exiting main
        self.ui_main.Exit.clicked.connect(self.main_exit)

    def showReminders(self):
        self.ui_main.stackedWidget.setCurrentWidget(self.ui_main.Reminder)

    def showLifeSync(self):
        self.ui_main.stackedWidget.setCurrentWidget(self.ui_main.Chatbot)

    def showNearest_h(self):
        self.ui_main.stackedWidget.setCurrentWidget(self.ui_main.Nhospital)

    def find_nearest_hospital(self):
        API = google_api_key
        geolocator = GoogleV3(api_key=API)
        address = self.ui_main.UserAddress.text()
        location = geolocator.geocode(address)
        latitude = float(location.latitude)
        longitude = float(location.longitude)
        finder = HospitalFinder()
        nearest_hospital_data = finder.find_nearest_open_hospital(latitude, longitude)
        if nearest_hospital_data:
            hospital_name = nearest_hospital_data[0]["name"]
            hospital_address = nearest_hospital_data[0]["address"]
            hospital_location = (
                f"https://www.google.com/maps?q={hospital_name.replace(' ', '+')}"
            )
            hospital_is_open = (
                "Open" if nearest_hospital_data[0]["open_24h"] else "Close"
            )
            self.ui_main.textBrowser.setText(
                f"Nearest Hospital: {hospital_name}\nAddress: {hospital_address}\nLocation: {hospital_location}\nOpen: {hospital_is_open}"
            )
            self.latitude = nearest_hospital_data[0]["location"]["lat"]
            self.longitude = nearest_hospital_data[0]["location"]["lng"]
        else:
            self.ui_main.textBrowser.setText("No nearest hospital found.")

    # For find nearest Pharmacy
    def find_nearest_pharmacy(self):
        API = google_api_key
        geolocator = GoogleV3(api_key=API)
        address = self.ui_main.UserAddress.text()
        location = geolocator.geocode(address)
        latitude = float(location.latitude)  # enlem
        longitude = float(location.longitude)  # boylam
        finder = HospitalFinder()
        nearest_pharmacy_data = finder.find_the_nearest_pharmacy(latitude, longitude)
        try:
            if nearest_pharmacy_data:
                pharmacy_name = nearest_pharmacy_data["name"]
                pharmacy_address = nearest_pharmacy_data["address"]
                pharmacy_location = (
                    f"https://www.google.com/maps?q={pharmacy_name.replace(' ', '+')}"
                )
                pharmacy_is_open = "Open"
                self.ui_main.textBrowser.setText(
                    f"Nearest Pharmacy: {pharmacy_name}\nAddress: {pharmacy_address}\nLocation: {pharmacy_location}\nOpen: {pharmacy_is_open}"
                )
                self.latitude = nearest_pharmacy_data["location"]["lat"]
                self.longitude = nearest_pharmacy_data["location"]["lng"]
            else:
                self.ui_main.textBrowser.setText("No nearest hospital found.")
        except Exception as e:
            print(f"Error is {e}")

    def chatbot(self):
        option = self.ui_main.Useroption.currentText()
        question = self.ui_main.usermsg.toPlainText()
        prompt = f"The Kind of the Question:{option}\nQuestion:{question}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You’re a kind helpful assistant since your health assistant "
                    "and your name is ALIZA, The person first he will give you want kind of "
                    "question he/she want to ask you like this : Request Medication Advice"
                    "then he/she asks you the question? if the question is not relate health"
                    "just tell politely what is your job. Also when you are giving answer "
                    "start with your name and the name of our Company LifeSync.",
                },
                {"role": "user", "content": prompt},
            ],
        )
        answer = response.choices[0].message.content
        self.ui_main.BotAnswer.setText(answer)

    @staticmethod
    def open_location_in_browser(latitude, longitude):
        url = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"
        # Open the URL in the default web browser
        QDesktopServices.openUrl(QUrl(url))

    @staticmethod
    def main_exit():
        sys.exit()

    def closeEvent(self, event):
        self.conn.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_wn = MainWindow()
    main_wn.show()
    sys.exit(app.exec_())

import sqlite3

from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QMainWindow

from home_pg.home import Ui_MainWindow
from PyQt5.QtCore import QTime, QDate, Qt
import winsound
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta

# Massage Button the stylesheet
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


class ReminderDb(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('LifeSync')
        # Database connection
        self.conn = sqlite3.connect(
            r"C:\Users\Abdirashid\Desktop\LifeSync\reminders.db"
        )
        self.curs = self.conn.cursor()

        self.table = (
            "CREATE TABLE IF NOT EXISTS reminders("
            "MedicationID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
            "MedicationName TEXT NOT NULL,"
            "Dosage TEXT NOT NULL,"
            "Frequency TEXT NOT NULL,"
            "Duration TEXT NOT NULL,"
            "Priority TEXT NOT NULL,"
            "Time TEXT NOT NULL,"
            "Date TEXT NOT NULL,"
            "RefillDate TEXT NOT NULL)"
        )
        self.conn.execute(self.table)
        self.conn.commit()

        # initializing the table
        # self.list_it()

    # Adding to database
    def Add_db(self):
        _Medication_name = self.MedicationName.text()
        _dosage = self.Dosage.text()
        _frequency = self.Frequency.currentText()
        _duration = self.Duration.text()
        _priority = self.Priority.currentText()
        _time = self.Time.time().toString("hh:mm AP")
        _date = self.calendarWidget.selectedDate().toString(Qt.ISODate)
        _RefillDate = self.Refill.date().toPyDate()

        if _Medication_name and _dosage and _frequency and _time:
            self.conn.execute(
                "INSERT INTO reminders (MedicationName, Dosage,"
                "Frequency, Duration, Priority, Time, Date, RefillDate)"
                "VALUES (?,?,?,?,?,?,?,?)",
                (
                    _Medication_name,
                    _dosage,
                    _frequency,
                    _duration,
                    _priority,
                    _time,
                    _date,
                    _RefillDate,
                ),
            )
            self.conn.commit()
            self.list_it()
        else:
            print("Something Missing")

    def list_it(self):
        self.tableWidget.clear()

        self.tableWidget.setHorizontalHeaderLabels(
            (
                "MedicationID",
                "MedicationName",
                "Dosage",
                "Frequency",
                "Duration",
                "Priority",
                "Time",
                "Date",
                "RefillDate",
            )
        )
        # From data
        self.curs.execute("SELECT * FROM reminders")
        for lineIndex, lineData in enumerate(self.curs):
            for cellIndex, cellData in enumerate(lineData):
                self.tableWidget.setItem(
                    lineIndex, cellIndex, QTableWidgetItem(str(cellData))
                )

        # Cleaning user inputs
        self.MedicationName.clear()
        self.Dosage.clear()
        self.Frequency.setCurrentIndex(0)
        self.Duration.clear()
        self.Priority.setCurrentIndex(0)

    def delete_it(self):
        msgs_box = QMessageBox()
        msgs_box.setStyleSheet(STYLESHEET)

        answer = QMessageBox.question(
            self,
            "DELETE ITEM",
            "Are you sure you want to delete this item? This action cannot be undone.",
            QMessageBox.Yes | QMessageBox.No,
        )
        if answer == QMessageBox.Yes:
            select_item = self.tableWidget.selectedItems()
            delete_item = select_item[0].text()
            try:
                self.curs.execute(
                    "DELETE FROM reminders WHERE MedicationID = ?", (delete_item,)
                )
                self.conn.commit()
                self.list_it()
                message = "Record deletion completed successfully"
                msgs_box.setWindowTitle("Notice")
                msgs_box.setText(message)
            except Exception as e:
                message = f"An error occurred with the following message:\n{e}"
                msgs_box.setWindowTitle("Error")
                msgs_box.setText(message)
        else:
            message = "You have successfully canceled it."
            msgs_box.setWindowTitle("Notice")
            msgs_box.setText(message)

        msgs_box.addButton(QMessageBox.Ok)
        msgs_box.exec_()

    def search_it(self):
        search_query = self.Search_input.text()
        dosage_query = self.Dosage.text()

        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(
            (
                "MedicationID",
                "MedicationName",
                "Dosage",
                "Frequency",
                "Duration",
                "Priority",
                "Time",
                "Date",
                "RefillDate",
            )
        )
        query = "SELECT * FROM reminders WHERE MedicationName LIKE ? AND Dosage LIKE ?"
        self.curs.execute(query, (f"%{search_query}%", f"%{dosage_query}%"))
        for lineIndex, lineData in enumerate(self.curs):
            for cellIndex, cellData in enumerate(lineData):
                self.tableWidget.setItem(
                    lineIndex, cellIndex, QTableWidgetItem(str(cellData))
                )

        # cleaning user input
        self.MedicationName.clear()

    def fill(self):
        selected = self.tableWidget.selectedItems()
        try:
            self.MedicationName.setText(selected[1].text())
            self.Dosage.setText(selected[2].text())
            self.Frequency.setCurrentText(selected[3].text())

            self.Duration.setText(selected[4].text())
            self.Priority.setCurrentText(selected[5].text())

            time = QTime.fromString(selected[6].text(), "hh:mm AP")
            self.Time.setTime(time)

            # Date Data
            date_str = selected[7].text()
            calendar_date = QDate.fromString(date_str, "yyyy-MM-dd")
            self.calendarWidget.setSelectedDate(calendar_date)

            # Refill Date
            date = QDate.fromString(selected[8].text(), "yyyy-MM-dd")
            self.Refill.setDate(date)

        except IndexError:
            pass

    def update_it(self):
        msgs_box = QMessageBox()
        msgs_box.setStyleSheet(STYLESHEET)

        answer = QMessageBox.question(
            self,
            "Update Confirmation",
            "This action will update the item. Proceed?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if answer == QMessageBox.Yes:
            try:
                select = self.tableWidget.selectedItems()
                id = int(select[0].text())
                _Medication_name = self.MedicationName.text()
                _dosage = self.Dosage.text()
                _frequency = self.Frequency.currentText()
                _duration = self.Duration.text()
                _priority = self.Priority.currentText()
                _time = self.Time.time().toString("hh:mm AP")
                _date = self.calendarWidget.selectedDate().toString(Qt.ISODate)
                _RefillDate = self.Refill.date().toPyDate()

                # to data
                self.curs.execute(
                    "UPDATE reminders SET MedicationName=?, Dosage=?, Frequency=?, Duration=?, Priority=?, Time=?, Date=?, RefillDate=? WHERE MedicationID=?",
                    (
                        _Medication_name,
                        _dosage,
                        _frequency,
                        _duration,
                        _priority,
                        _time,
                        _date,
                        _RefillDate,
                        id,
                    ),
                )
                self.conn.commit()
                self.list_it()
                message = "The record has been successfully updated."
                msgs_box.setWindowTitle("Update Successful")
                msgs_box.setText(message)
            except Exception as e:
                message = f"An error occurred with the following message:\n{e}"
                msgs_box.setWindowTitle("Error")
                msgs_box.setText(message)
        else:
            message = "You have successfully canceled it."
            msgs_box.setWindowTitle("Notice")
            msgs_box.setText(message)

        msgs_box.addButton(QMessageBox.Ok)
        msgs_box.exec_()

    # for checking reminders
    def check_medication_reminders(self):
        current_time = QTime.currentTime().toString('hh:mm AP')
        current_day = QDate.currentDate().toString(Qt.ISODate)

        self.curs.execute(
            "SELECT * FROM reminders WHERE Time=? AND Date=?", (current_time, current_day)
        )
        medications = self.curs.fetchall()
        if medications:
            self.play_notification_sound()
            QMessageBox.information(
                self, "Medication Reminder", "It's time to take your medication!")

    # Playing Sound
    @staticmethod
    def play_notification_sound():
        try:
            winsound.PlaySound(r"C:\Users\Abdirashid\Desktop\LifeSync\main\notification.wav", winsound.SND_FILENAME)
        except Exception as e:
            print(f"Error playing notification sound: {str(e)}")

    # SENDING EMAIL MSG ######
    def send_reminder_email(self, email, name):
        current_day = QDate.currentDate().toString(Qt.ISODate)
        current_date = datetime.now().date()
        # Get time from database
        self.curs.execute(
            "SELECT Time, MedicationName FROM reminders WHERE Date = ? AND Time >= '00:00 AM' AND Time <= '11:59 PM'",
            (current_day,))
        records = self.curs.fetchall()

        for record in records:
            db_time_str = record[0]
            db_time = datetime.strptime(db_time_str, "%I:%M %p").time()
            medication_name = record[1]

            # Combine the current date with the database time to create the scheduled datetime
            scheduled_datetime = datetime.combine(current_date, db_time)

            # Email configuration
            sender_email = 'your-email@example.com'
            sender_password = 'your-password'
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587

            # Calculate the reminder datetime (20 minutes before the scheduled datetime)
            reminder_datetime = scheduled_datetime - timedelta(minutes=20)

            # Compose the email message
            subject = 'Medication Reminder'
            message = f'Dear {name},\n\nThis is a reminder to take your medication "{medication_name}" on {scheduled_datetime.strftime("%Y-%m-%d %H:%M")}. Please remember to follow the prescribed dosage instructions.\n\nBest regards,\nYour Medication Reminder'
            email_message = MIMEText(message)
            email_message['Subject'] = subject
            email_message['From'] = sender_email
            email_message['To'] = email

            try:
                # Check if the reminder time has already passed
                if datetime.now() >= reminder_datetime:
                    continue
                current_time = datetime.now()
                # Calculate the time difference in seconds
                time_diff_seconds = (reminder_datetime - current_time).total_seconds()

                # Delay sending the email until the reminder time
                import time
                time.sleep(time_diff_seconds)

                # Connect to the SMTP server
                smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
                smtp_connection.starttls()
                smtp_connection.login(sender_email, sender_password)

                # Send the email
                smtp_connection.send_message(email_message)

                # Close the connection
                smtp_connection.quit()

                print('Reminder email sent successfully!')
            except Exception as e:
                print(f'Error sending reminder email: {str(e)}')

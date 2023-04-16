import sys
import datetime
import playsound
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore


class Alarm(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.alarm_sesi = "alarm.mp3"     #bu alana belirlediğiniz .mp3 veya .wav dosyasının adını yazmanız gerekmektedir.
        self.alarm_saati_label = QLabel("Alarm Saati (HH:MM): ")
        self.alarm_saati_input = QLineEdit()
        self.alarm_saati_input.setPlaceholderText("00:00")

        self.alarm_baslat_button = QPushButton("Alarmı Başlat")
        self.alarm_sustur_button = QPushButton("ALARMI SUSTUR")
        self.alarm_sustur_button.setEnabled(False)

        self.kalan_sure_label = QLabel()
        self.kalan_sure_label.setAlignment(QtCore.Qt.AlignCenter)
        self.kalan_sure_label.setStyleSheet("font-size: 20px; margin-top: 20px;")

        v_box = QVBoxLayout()
        v_box.addWidget(self.alarm_saati_label)
        v_box.addWidget(self.alarm_saati_input)
        v_box.addWidget(self.alarm_baslat_button)
        v_box.addWidget(self.alarm_sustur_button)
        v_box.addWidget(self.kalan_sure_label)

        self.setLayout(v_box)
        self.setWindowTitle("Alarm Uygulaması")
        self.show()

        self.alarm_baslat_button.clicked.connect(self.alarm_baslat)
        self.alarm_sustur_button.clicked.connect(self.alarm_sustur)

    def alarm_baslat(self):
        self.alarm_saati = self.alarm_saati_input.text()
        self.alarm_saati = datetime.datetime.strptime(self.alarm_saati, "%H:%M")

        self.timer = QTimer()
        self.timer.timeout.connect(self.check_alarm)
        self.timer.start(1000)

    def check_alarm(self):
        suanki_zaman = datetime.datetime.now().strftime("%H:%M")

        if suanki_zaman == self.alarm_saati.strftime("%H:%M"):
            print("Alarm çalıyor!")
            playsound.playsound(self.alarm_sesi)
            self.timer.stop()
            self.alarm_sustur_button.setEnabled(True)
            self.kalan_sure_label.setText("")

        else:
            kalan_sure = (self.alarm_saati - datetime.datetime.strptime(suanki_zaman, "%H:%M"))
            kalan_sure_str = str(kalan_sure).split(":")
            self.kalan_sure_label.setText(f"Kalan süre: {kalan_sure_str[0]}:{kalan_sure_str[1]}:{kalan_sure_str[2][:2]}")

    def alarm_sustur(self):
        self.alarm_sustur_button.setEnabled(False)
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    alarm = Alarm()
    sys.exit(app.exec_())

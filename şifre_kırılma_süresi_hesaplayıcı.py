import math
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton

class PasswordCracker(QWidget):
    def __init__(self):
        super().__init__()

        # Kullanılabilecek karakter seti
        self.characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+="

        # Şifre etiketi ve giriş kutusu
        self.password_label = QLabel("Şifre: ")
        self.password_input = QLineEdit()

        # Kırılma süresi sonucunu gösteren etiketler
        self.seconds_label = QLabel("Şifrenin kırılma süresi:")
        self.minutes_label = QLabel()
        self.hours_label = QLabel()
        self.days_label = QLabel()
        self.years_label = QLabel()

        # Hesapla düğmesi
        self.calculate_button = QPushButton("Hesapla")
        self.calculate_button.clicked.connect(self.calculate)

        # Düzenleyiciler
        password_layout = QHBoxLayout()
        password_layout.addWidget(self.password_label)
        password_layout.addWidget(self.password_input)

        result_layout = QVBoxLayout()
        result_layout.addWidget(self.seconds_label)
        result_layout.addWidget(self.minutes_label)
        result_layout.addWidget(self.hours_label)
        result_layout.addWidget(self.days_label)
        result_layout.addWidget(self.years_label)

        main_layout = QVBoxLayout()
        main_layout.addLayout(password_layout)
        main_layout.addWidget(self.calculate_button)
        main_layout.addLayout(result_layout)

        self.setLayout(main_layout)
        self.setWindowTitle("Şifre Kırma Süresi Hesaplayıcı")

        # Varsayılan kombinasyon sayısını ayarla
        self.combinations_per_second = int(10**9) # 1 milyar kombinasyon/saniye

    def calculate(self):
        password = self.password_input.text()

        possible_combinations = math.pow(len(self.characters), len(password))

        seconds = possible_combinations / self.combinations_per_second
        minutes = seconds / 60
        hours = minutes / 60
        days = hours / 24
        years = days / 365

        self.seconds_label.setText("Şifrenin kırılma süresi:")
        self.minutes_label.setText("Dakika: {:.3f}".format(minutes))
        self.hours_label.setText("Saat: {:.3f}".format(hours))
        self.days_label.setText("Gün: {:.3f}".format(days))
        self.years_label.setText("Yıl: {:.3f}".format(years))


if __name__ == "__main__":
    app = QApplication([])
    window = PasswordCracker()
    window.show()
    app.exec_()


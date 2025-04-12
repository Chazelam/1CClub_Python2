from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QLineEdit, QTextEdit
from PyQt6.QtWidgets import QCheckBox, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

def input_feedback():
    if check.isChecked():
        name.setText(name_input.text() + ", введите отзыв:")
        name_input.hide()
        check.hide()
        feedback.show()
        line.addWidget(feedback)
        button_next.setText("Отправить")

def send_feedback():
    win = QMessageBox()
    win.setWindowTitle("Отзыв")
    win.setWindowIcon(QIcon("l11/images/cart.png"))
    win.setText("Спасибо за отзыв!")
    win.exec()
    feedback.clear()

def next_step():
    if button_next.text() == "Регистрация":
        input_feedback()
    else:
        send_feedback()

app = QApplication([])
window = QWidget()
window.resize(150,200)
window.setWindowTitle("Авторизация")
window.setWindowIcon(QIcon("l11/images/cart.png"))
window.setStyleSheet("background-color: #AA67D5; "      # Фиолетовый цвет фона
                     "color: white;")                   # Белый цвет текста

name = QLabel("Имя:")
name.setStyleSheet("font-size: 24px;"                   # Размер шрифта - 24
                   "font-weight: bold;")                # Жирный текст
name_input = QLineEdit()
name_input.setStyleSheet("font-size: 18px;"             # Размер шрифта - 18
                         "font-weight: bold;"           # Жирный текст
                         "background-color: #F3F29A;"   # Желтый фон
                         "color: #000;"                 # Черный текст
                         "padding: 5px;")               # Внутренние отступы - 5 пикселей
check = QCheckBox("Согласие на обработку данных")
button_next = QPushButton("Регистрация")
button_next.setStyleSheet("font-size: 16px;"            # Размер шрифта - 16
                          "background-color: #6C0AAB;"  # Фиолетовый цвет фона
                          "width: 75px;")               # Фиксированная ширина кнопки - 75 пикселей
button_next.clicked.connect(next_step)

line = QVBoxLayout()
line.addWidget(name,       alignment=Qt.AlignmentFlag.AlignCenter)
line.addWidget(name_input, alignment=Qt.AlignmentFlag.AlignCenter)
line.addWidget(check,      alignment=Qt.AlignmentFlag.AlignCenter)
line.addWidget(button_next)
window.setLayout(line)

feedback = QTextEdit()
feedback.setStyleSheet("font-size: 18px;"               # Размер шрифта - 18
                       "font-weight: bold;"             # Жирный текст
                       "background-color: #F3F29A;"     # Желтый фон
                       "color: #000;")                  # Черный текст
line.addWidget(feedback)
feedback.hide()

window.show()
app.exec()

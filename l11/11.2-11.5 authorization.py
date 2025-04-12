from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QLineEdit, QTextEdit
from PyQt6.QtWidgets import QCheckBox, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

# Функция обработки данных первой формы
def input_feedback():
    if check.isChecked():
        # Персонализация приветствия
        name.setText(f"{name_input.text()}, введите отзыв:")  
        name_input.hide()                 # Скрываем поле ввода имени
        check.hide()                      # Скрываем чекбокс
        feedback.show()                   # Показываем поле для отзыва
        button_next.setText("Отправить")  # Меняем текст кнопки

# Функция отправки отзыва
def send_feedback():
    win = QMessageBox()
    win.setWindowTitle("Отзыв")
    win.setWindowIcon(QIcon("l11/images/cart.png"))
    win.setText("Спасибо за отзыв!")
    win.exec()
    feedback.clear()

# Общий обработчик кнопки с логикой переключения между состояниями
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

name = QLabel("Имя:")
name_input = QLineEdit()
check = QCheckBox("Согласие на обработку данных")
button_next = QPushButton("Регистрация")
# Подключение обработчика нажатия кнопки
button_next.clicked.connect(next_step) # Связываем клик с логикой переключения

line = QVBoxLayout()
line.addWidget(name,       alignment=Qt.AlignmentFlag.AlignCenter)
line.addWidget(name_input, alignment=Qt.AlignmentFlag.AlignCenter)
line.addWidget(check,      alignment=Qt.AlignmentFlag.AlignCenter)
line.addWidget(button_next)
window.setLayout(line)

# Инициализация нового элемента - многострочного текстового поля
feedback = QTextEdit()
line.addWidget(feedback) # Добавляем поле в layout при создании
feedback.hide()          # Сразу скрываем поле для отзыва


window.show()
app.exec()

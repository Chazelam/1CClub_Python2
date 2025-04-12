from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QLineEdit, QTextEdit
from PyQt6.QtWidgets import QCheckBox, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
# Новый импорт для работы с JSON
import json

# Загрузка существующих отзывов из файла при старте приложения
with open("l11/feedbacks.json", encoding="utf-8") as file:
    feedbacks = json.load(file)

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
    start_win() # Восстановление начального состояния интерфейса

# Функция для сброса интерфейса в начальное состояние
def start_win():
    write_feedback()        # Сохранение отзыва перед сбросом
    name.setText("Имя:")    # Изменение текста
    name_input.clear()      # Очистка поля имени
    feedback.clear()        # Очистка поля отзыва
    name_input.show()       # Показать поле для ввода имени
    check.setChecked(False) # Сброс состояния чекбокса
    check.show()            # Показать чекбокс
    feedback.hide()         # Скрыть поле для отзыва
    button_next.setText("Регистрация")  # Возврат исходного текста кнопки

def next_step():
    if button_next.text() == "Регистрация":
        input_feedback()
    else:
        send_feedback()

# Функция для записи отзыва в словарь
def write_feedback():
    # Если пользователь существует в базе
    if name_input.text() in feedbacks:
        # Добавляем отзыв к его списку отзывов
        feedbacks[name_input.text()].append(feedback.toPlainText())
    else:  # Иначе (пользователя нет в базе)
        # Создаем в базу поле с его именем и присвиваем ему список с новым отзывом
        feedbacks[name_input.text()] = [feedback.toPlainText()]

app = QApplication([])
window = QWidget()
window.resize(250,300)
window.setWindowTitle("Авторизация")
window.setWindowIcon(QIcon("l11/images/cart.png"))
window.setStyleSheet("background-color: #AA67D5;"
                     "color: white;")

name = QLabel("Имя:")
name.setStyleSheet("font-size: 24px;"
                   "font-weight: bold;")
name_input = QLineEdit()
name_input.setStyleSheet("font-size: 18px;"
                         "font-weight: bold;"
                         "background-color: #F3F29A;"
                         "padding: 5px;"
                         "color: #000;")
check = QCheckBox("Согласие на обработку данных")
button_next = QPushButton("Регистрация")
button_next.setStyleSheet("font-size: 16px;"
                          "background-color: #6C0AAB;"
                          "width: 75px;")
button_next.clicked.connect(next_step)

line = QVBoxLayout()
line.addWidget(name,       alignment=Qt.AlignmentFlag.AlignCenter)
line.addWidget(name_input, alignment=Qt.AlignmentFlag.AlignCenter)
line.addWidget(check,      alignment=Qt.AlignmentFlag.AlignCenter)
line.addWidget(button_next)
window.setLayout(line)

feedback = QTextEdit()
feedback.setStyleSheet("font-size: 18px;"
                       "font-weight: bold;"
                       "background-color: #F3F29A;"
                       "padding: 5px;"
                       "color: #000;")
line.addWidget(feedback)
feedback.hide()

window.show()
app.exec()

# Сохранение всех отзывов в файл при завершении приложения
with open("l11/feedbacks.json", "w", encoding="utf-8") as file:
    json.dump(feedbacks, file, ensure_ascii=False)

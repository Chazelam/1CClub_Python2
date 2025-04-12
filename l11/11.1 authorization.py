# Импорт необходимых модулей из PyQt6
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt6.QtWidgets import QLineEdit, QCheckBox, QLabel, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

# Создание объекта приложения
app = QApplication([])

# Создание и настройка главного окна
window = QWidget()
window.resize(150, 200)                             # Установка размеров окна
window.setWindowTitle("Авторизация")                # Заголовок окна
window.setWindowIcon(QIcon("l11/images/cart.png"))  # Установка иконки окна

# Создание элементов интерфейса
name = QLabel("Имя:")                              # Метка для текста "Имя:"
name_input = QLineEdit()                           # Поле для ввода имени
check = QCheckBox("Согласие на обработку данных")  # Чекбокс с текстом
button_next = QPushButton("Регистрация")           # Кнопка регистрации

# Создание вертикального контейнера для элементов
line = QVBoxLayout()
# Добавление элементов в контейнер с выравниванием по центру
line.addWidget(name,        alignment=Qt.AlignmentFlag.AlignCenter)
line.addWidget(name_input,  alignment=Qt.AlignmentFlag.AlignCenter)
line.addWidget(check,       alignment=Qt.AlignmentFlag.AlignCenter)
# Кнопка без специального выравнивания
line.addWidget(button_next)  

# Установка созданного контейнера в окно
window.setLayout(line)

# Отображение окна и запуск приложения
window.show()
app.exec()
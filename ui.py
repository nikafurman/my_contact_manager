from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(412, 500)  # Увеличьте размер окна для новой кнопки

        # Установка стиля фона
        Dialog.setStyleSheet("background-color: rgb(223, 216, 255);")

        # Метки для полей ввода
        self.label_name = QtWidgets.QLabel(Dialog)
        self.label_name.setGeometry(QtCore.QRect(30, 10, 100, 20))
        self.label_name.setText("Имя:")

        self.label_phone = QtWidgets.QLabel(Dialog)
        self.label_phone.setGeometry(QtCore.QRect(30, 50, 100, 20))
        self.label_phone.setText("Телефон:")

        self.label_email = QtWidgets.QLabel(Dialog)
        self.label_email.setGeometry(QtCore.QRect(30, 90, 120, 20))
        self.label_email.setText("Электронная почта:")

        # Поля ввода
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 351, 20))
        self.lineEdit.setStyleSheet("background-color: white;")

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 70, 351, 20))
        self.lineEdit_2.setStyleSheet("background-color: white;")

        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 110, 351, 25))
        self.lineEdit_3.setStyleSheet("background-color: white;")

        # Поле для поиска по телефону
        self.label_search = QtWidgets.QLabel(Dialog)
        self.label_search.setGeometry(QtCore.QRect(30, 150, 120, 20))
        self.label_search.setText("Поиск по телефону:")

        self.lineEdit_search = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_search.setGeometry(QtCore.QRect(150, 150, 231, 20))
        self.lineEdit_search.setStyleSheet("background-color: white;")

        # Кнопки
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 190, 111, 31))
        self.pushButton.setText("Добавить контакт")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 190, 111, 31))
        self.pushButton_2.setText("Удалить контакт")

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 190, 111, 31))
        self.pushButton_3.setText("Обновить контакт")

        # Кнопка восстановления контакта
        self.pushButton_restore = QtWidgets.QPushButton(Dialog)
        self.pushButton_restore.setGeometry(QtCore.QRect(30, 230 + 211 + 10 ,111 ,31))
        self.pushButton_restore.setText("Восстановить контакт")
        self.pushButton_restore.setStyleSheet("font-size: 7pt;")

        # Таблица для отображения контактов
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(30, 230 ,351 ,211))

        # Установка заголовков столбцов таблицы (без ID)
        headers = ["Имя", "Телефон", "Электронная почта"]
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels(headers)

        # Кнопка для удаления всех контактов (ui.py)
        self.pushButton_clear = QtWidgets.QPushButton(Dialog)
        self.pushButton_clear.setGeometry(QtCore.QRect(150, 230 + 211 + 10, 111, 31))
        self.pushButton_clear.setText("Удалить все")





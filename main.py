from PyQt5 import QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from ui import Ui_Dialog


class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Изменяем заголовок окна
        self.setWindowTitle("Менеджер контактов")

        self.connect_to_database()
        self.load_contacts()

        # Подключение кнопок к функциям
        self.ui.pushButton.clicked.connect(self.add_contact)
        self.ui.pushButton_2.clicked.connect(self.delete_contact)
        self.ui.pushButton_3.clicked.connect(self.update_contact)
        self.ui.pushButton_restore.clicked.connect(self.restore_contact)

        # Подключение поля поиска к функции
        self.ui.lineEdit_search.textChanged.connect(self.search_contact)

        # Подключение кнопки "Удалить все"
        self.ui.pushButton_clear.clicked.connect(self.clear_all_contacts)

        # Переменная для хранения последнего удаленного контакта
        self.last_deleted_contact = None

    def connect_to_database(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('contacts.db')

        if not self.db.open():
            print("Не удалось подключиться к базе данных.")
            return

    def load_contacts(self):
        query = QSqlQuery("SELECT name, phone, email FROM contacts")
        self.ui.tableWidget.setRowCount(0)  # Очистка таблицы перед загрузкой новых данных

        while query.next():
            name = query.value(0)
            phone = query.value(1)
            email = query.value(2)
            row_position = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row_position)

            # Заполнение ячеек таблицы данными из базы
            self.ui.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(name))
            self.ui.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(phone))
            self.ui.tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(email))

    def add_contact(self):
        name = self.ui.lineEdit.text()
        phone = self.ui.lineEdit_2.text()
        email = self.ui.lineEdit_3.text()

        if name and phone and email:
            query = QSqlQuery()
            query.prepare("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)")
            query.addBindValue(name)
            query.addBindValue(phone)
            query.addBindValue(email)

            if query.exec_():
                print(f"Контакт '{name}' добавлен.")
                self.load_contacts()  # Обновление таблицы после добавления
                self.clear_inputs()  # Очистка полей ввода
            else:
                print("Ошибка при добавлении контакта:", query.lastError().text())

    def delete_contact(self):
        selected_row = self.ui.tableWidget.currentRow()  # Получаем выбранную строку
        if selected_row >= 0:
            name = self.ui.tableWidget.item(selected_row, 0).text()  # Имя контакта
            phone = self.ui.tableWidget.item(selected_row, 1).text()  # Телефон контакта

            # Сохраняем информацию о последнем удаленном контакте для восстановления
            self.last_deleted_contact = (name, phone)

            query = QSqlQuery()
            query.prepare("DELETE FROM contacts WHERE name=? AND phone=?")
            query.addBindValue(name)
            query.addBindValue(phone)

            if query.exec_():
                print(f"Контакт '{name}' успешно удален.")
                self.load_contacts()  # Обновление таблицы после удаления
            else:
                print("Ошибка при удалении контакта:", query.lastError().text())
        else:
            print("Ошибка: Пожалуйста, выберите контакт для удаления.")

    def restore_contact(self):
        if self.last_deleted_contact:
            name, phone = self.last_deleted_contact
            email = f"{name.lower()}@example.com"  # Простой email на основе имени

            query = QSqlQuery()
            query.prepare("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)")
            query.addBindValue(name)
            query.addBindValue(phone)
            query.addBindValue(email)

            if query.exec_():
                print(f"Контакт '{name}' восстановлен.")
                self.load_contacts()  # Обновление таблицы после восстановления
                self.last_deleted_contact = None  # Сбрасываем информацию о восстановленном контакте
            else:
                print("Ошибка при восстановлении контакта:", query.lastError().text())
        else:
            print("Ошибка: Нет контакта для восстановления.")

    def update_contact(self):
        selected_row = self.ui.tableWidget.currentRow()  # Получаем выбранную строку
        if selected_row >= 0:
            old_name = self.ui.tableWidget.item(selected_row, 0).text()  # Старое имя
            old_phone = self.ui.tableWidget.item(selected_row, 1).text()  # Старый телефон

            new_name = self.ui.lineEdit.text()
            new_phone = self.ui.lineEdit_2.text()
            new_email = self.ui.lineEdit_3.text()

            if new_name and new_phone and new_email:
                query = QSqlQuery()
                query.prepare("UPDATE contacts SET name=?, phone=?, email=? WHERE name=? AND phone=?")
                query.addBindValue(new_name)
                query.addBindValue(new_phone)
                query.addBindValue(new_email)
                query.addBindValue(old_name)
                query.addBindValue(old_phone)

                if query.exec_():
                    print(f"Контакт '{old_name}' обновлен на '{new_name}'.")
                    self.load_contacts()  # Обновление таблицы после обновления
                    self.clear_inputs()  # Очистка полей ввода
                else:
                    print("Ошибка при обновлении контакта:", query.lastError().text())
            else:
                print("Ошибка ввода: Пожалуйста, заполните все поля.")
        else:
            print("Ошибка: Пожалуйста, выберите контакт для обновления.")

    def clear_inputs(self):
        # Очистка полей ввода
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()

    def closeEvent(self, event):
        # Закрытие соединения при закрытии окна
        if hasattr(self.db, 'close'):
            if callable(getattr(self.db, 'close')):
                try:
                    return_value = self.db.close()
                except Exception as e:
                    print(f"Ошибка при закрытии соединения: {e}")

    def search_contact(self):
        search_text = self.ui.lineEdit_search.text().strip()  # Получаем текст для поиска
        query = QSqlQuery()

        if search_text:  # Если текст не пустой
            query.prepare("SELECT name, phone, email FROM contacts WHERE phone LIKE ?")
            query.addBindValue(f"%{search_text}%")  # Используем LIKE для частичных совпадений
        else:  # Если текст пустой, загружаем все контакты
            query.prepare("SELECT name, phone, email FROM contacts")

        self.ui.tableWidget.setRowCount(0)  # Очищаем таблицу перед загрузкой новых данных

        if query.exec_():
            while query.next():
                name = query.value(0)
                phone = query.value(1)
                email = query.value(2)

                row_position = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(row_position)

                # Заполняем таблицу результатами поиска или всех контактов
                self.ui.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(name))
                self.ui.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(phone))
                self.ui.tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(email))
        else:
            print("Ошибка при поиске контактов:", query.lastError().text())

    def clear_all_contacts(self):
        """Метод для удаления всех контактов из базы данных."""
        reply = QtWidgets.QMessageBox.question(
            self,
            'Подтверждение',
            'Вы уверены, что хотите удалить все контакты?',
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No
        )

        if reply == QtWidgets.QMessageBox.Yes:
            query = QSqlQuery()
            query.prepare("DELETE FROM contacts")

            if query.exec_():
                print("Все контакты успешно удалены.")
                self.load_contacts()  # Обновление таблицы после удаления
            else:
                print("Ошибка при удалении всех контактов:", query.lastError().text())


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

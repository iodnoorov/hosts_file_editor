import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
import design
from urllib.parse import urlparse


class ExampleApp(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnAdd.clicked.connect(self.hosts_save)
        self.inputUrl.clear()

    def hosts_save(self):
        hosts_file = open('C:\\Windows\\System32\\drivers\\etc\\hosts', "a")
        url = urlparse(self.inputUrl.text())
        add_text = '\n127.0.0.1 ' + url.netloc
        if hosts_file.write(add_text):
            self.statusText.setText("Status: Success")
        else:
            self.statusText.setText("Status: Error")
        hosts_file.close()


def main():
    app = QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
import design
from urllib.parse import urlparse
import validators


class ExampleApp(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnAdd.clicked.connect(self.hosts_save)
        self.inputUrl.clear()

    def hosts_save(self):
        if validators.url(self.inputUrl.text()) is True:
            url = urlparse(self.inputUrl.text())
            add_text = '\n127.0.0.1 ' + url.netloc
            hosts_file = open('C:\\Windows\\System32\\drivers\\etc\\hosts', "a")
            if hosts_file.write(add_text):
                self.statusText.setText("Status: Success")
            else:
                self.statusText.setText("Status: Save error")
            hosts_file.close()
        else:
            self.statusText.setText("Not url")


def main():
    app = QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()

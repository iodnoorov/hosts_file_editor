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

    def validate_input_data(self):
        url = self.inputUrl.text()
        ip = self.inputIp.text()
        if validators.url(url) is True \
                and (validators.ipv4(ip) is True
                     or validators.ipv6(ip) is True
                     or not self.inputIp.text()):
            return True
        else:
            return False

    def hosts_save(self):
        ip = self.inputIp.text()
        url = self.inputUrl.text()
        if self.validate_input_data():
            if not ip:
                ip = '127.0.0.1'
            url = urlparse(url)
            add_text = '\n' + ip + ' ' + url.netloc.replace("www.", "", 1)
            hosts_file = open('C:\\Windows\\System32\\drivers\\etc\\hosts', "a")
            if hosts_file.write(add_text):
                self.statusText.setText("Status: Success")
            else:
                self.statusText.setText("Status: Save error")
            hosts_file.close()
        else:
            self.statusText.setText("Validation error")


def main():
    app = QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()

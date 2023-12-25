import sys
from config import config
from PyQt6.QtCore import QTranslator
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog
from controller.actionsController import actionsController
from model.ruleModel import ruleModel
from view.add_rule import Ui_AddRuleWindow
from view.design import Ui_HostsEditor
from view.about import Ui_creditsDialog


class HostsApp(QMainWindow, Ui_HostsEditor):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        translator = QTranslator()
        translator.load('translations\\design_' + config.LANGUAGE + '.qm')
        _app = QApplication.instance()
        _app.installTranslator(translator)
        self.retranslateUi(self)
        # buttons with popups
        self.infoBtn.clicked.connect(lambda: self.information())
        self.addBtn.clicked.connect(lambda: self.add_rule())

    def information(self):
        InfoDialog(self).exec()

    def add_rule(self):
        addWindow(self).show()


class addWindow(QMainWindow, Ui_AddRuleWindow):
    def __init__(self, parent=None):
        super(addWindow, self).__init__(parent)
        self.setupUi(self)
        translator = QTranslator()
        translator.load('translations\\addrule_' + config.LANGUAGE + '.qm')
        _app = QApplication.instance()
        _app.installTranslator(translator)
        self.retranslateUi(self)


class InfoDialog(QDialog, Ui_creditsDialog):
    def __init__(self, parent=None):
        super(InfoDialog, self).__init__(parent)
        self.setupUi(self)
        translator = QTranslator()
        translator.load('translations\\about_' + config.LANGUAGE + '.qm')
        _app = QApplication.instance()
        _app.installTranslator(translator)
        self.retranslateUi(self)
        self.pushButton.clicked.connect(self.btnClosed)

    def btnClosed(self):
        self.close()


def main():
    app = QApplication(sys.argv)
    model = ruleModel()
    window = HostsApp()
    actionsController(model, window)
    window.show()
    app.exec()


if __name__ == '__main__':
    main()

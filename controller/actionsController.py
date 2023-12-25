import sys

class actionsController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.reset()


        # view.editBtn.clicked.connect(lambda: self.edit_rule())
        # view.deleteBtn.clicked.connect(lambda: self.delete_rule())
        # view.saveBtn.clicked.connect(lambda: self.save())
        view.resetBtn.clicked.connect(lambda: self.reset())
        # view.scheduleBtn.clicked.connect(lambda: self.schedule())
        # view.ieBtn.clicked.connect(lambda: self.input_output())
        # view.settingsBtn.clicked.connect(lambda: self.settings())

        view.exitBtn.clicked.connect(lambda: self.quit())

    def reset(self):
        self.view.hostsList.clear()
        data = self.model.get_data()
        self.view.hostsList.addItems(data)

    #def information(self):
    #    app.info()

    @staticmethod
    def quit():
        sys.exit()

    '''def hosts_save(self):
        ip = self.inputIp.text()
        url = self.inputUrl.text()
        if ValidationController.validate_input_data():
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
'''

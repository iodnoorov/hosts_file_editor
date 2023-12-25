class ruleModel:
    def __init__(self):
        self.data = None

    def get_data(self):
        hosts = open('C:\\Windows\\System32\\drivers\\etc\\hosts', "r")
        self.data = hosts.readlines()
        hosts.close()
        return self.data

    def set_data(self, data):
        hosts = open('C:\\Windows\\System32\\drivers\\etc\\hosts', "w")
        self.data = data
        hosts.writelines(self.data)
        hosts.close()

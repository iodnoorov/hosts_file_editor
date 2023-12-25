from app import HostsApp
import validators


class ValidationController(HostsApp):
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

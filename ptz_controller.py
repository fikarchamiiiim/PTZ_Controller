import requests
from requests.auth import HTTPDigestAuth

class PtzHikvision():
    def __init__(self, ip_add, username, password):
        self.ip_add = ip_add
        self.username = username
        self.password = password

        self.url = "http://{}@{}/ISAPI/PTZCtrl/channels/1/continuous".format(self.username, self.ip_add)
        self.data = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
        self.stop = True
        # self.num_cam = 151

        self.headers = {
            "Content-Type":"application/xml"
        }

    def func_start(self, data):
        body= self.data + "<PTZData>{}</PTZData>".format(data)
        r = requests.put(self.url, headers=self.headers, auth=HTTPDigestAuth(self.username, self.password), data=body)
        self.stop = False
        print(r)

    def func_stop(self):
        body= self.data + "<PTZData><pan>0</pan><tilt>0</tilt></PTZData>"
        r = requests.put(self.url, headers=self.headers, auth=HTTPDigestAuth(self.username, self.password), data=body)
        self.stop = True
        print(r)

    def up(self, speed=60):
        if self.stop:
            self.func_start("<pan>0</pan><tilt>{}</tilt>".format(speed))
        else:
            self.func_stop()

    def down(self, speed=60):
        if self.stop:
            self.func_start("<pan>0</pan><tilt>-{}</tilt>".format(speed))
        else:
            self.func_stop()

    def right(self, speed=60):
        if self.stop:
            self.func_start("<pan>{}</pan><tilt>0</tilt>".format(speed))
        else:
            self.func_stop()

    def left(self, speed=60):
        if self.stop:
            self.func_start("<pan>-{}</pan><tilt>0</tilt>".format(speed))
        else:
            self.func_stop()
    
    def zoom_in(self, speed=60):
        if self.stop:
            self.func_start("<PTZData><zoom>{}</zoom></PTZData>".format(speed))
        else:
            self.func_stop()

    def zoom_out(self, speed=60):
        if self.stop:
            self.func_start("<PTZData><zoom>-{}</zoom></PTZData>".format(speed))
        else:
            self.func_stop()
    


class PtzOkav():
    def __init__(self, ip_add, username, password):
        self.ip_add = ip_add
        self.username = username
        self.password = password

        self.url = "http://{}:{}@{}/merlin/PtzCtrl.cgi?operation={}&speed={}&channelno=0&value=0"

        self.stop = True
        # self.num_cam = 151

    def func_start(self, operation, speed):
        url = self.url.format(self.username, self.password, self.ip_add, operation, speed)
        r = requests.post(url)
        self.stop = False
        r.close()
        print(r)

    def func_stop(self):
        url = self.url.format(self.username, self.password, self.ip_add, 0, 0)
        r = requests.post(url)
        self.stop = True
        r.close()
        print(r)

    def up(self, speed=5):
        if self.stop == True:
            self.func_start(2,speed)
        elif self.stop == False:
            self.func_stop()

    def down(self, speed=5):
        if self.stop == True:
            self.func_start(7,speed)
        elif self.stop == False:
            self.func_stop()

    def right(self, speed=5):
        if self.stop == True:
            self.func_start(5,speed)
        elif self.stop == False:
            self.func_stop()

    def left(self, speed=5):
        if self.stop == True:
            self.func_start(4,speed)
        elif self.stop == False:
            self.func_stop()
    
    def zoom_in(self, speed=5):
        if self.stop == True:
            self.func_start(10, speed)
        elif self.stop == False:
            self.func_stop()

    def zoom_out(self, speed=5):
        if self.stop == True:
            self.func_start(9, speed)
        elif self.stop == False:
            self.func_stop()

    def test(self):
        test = "oke {}"
        testPrint = test.format("Print")
        print(testPrint)
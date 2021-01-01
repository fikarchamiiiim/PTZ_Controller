from ptz_controller import PtzHikvision, PtzOkav
import time

# hv = PtzHikvision("192.168.1.64", "admin", "0R4150ml38u")
okv = PtzOkav("192.168.1.151", "admin", "Litbangau1")
okv.test()
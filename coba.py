from ptz_controller import PtzHikvision, PtzOkav
import time

hv = PtzHikvision("192.168.88.64", "admin", "0r4150ml38u")
# okv = PtzOkav("192.168.1.151", "admin", "Litbangau1")
#

hv.focus_incr()
time.sleep(10)
hv.focus_incr()

hv.focus_decr()
time.sleep(10)
hv.focus_decr()
from ptz_controller import PtzHikvision, PtzOkav
import time
import env

hv = PtzHikvision(env.hikvision['host'], env.hikvision["user"], env.hikvision['pass'])
okav = PtzOkav(env.okav['host'], env.okav["user"], env.okav['pass'])
#

hv.focus_incr()
time.sleep(10)
hv.focus_incr()

hv.focus_decr()
time.sleep(10)
hv.focus_decr()
# import subprocess
# subprocess.Popen(['notify-send','ssk from python'])

import notify2
notify2.init('niku')
path ='/home/ssk/pro/linux controll/voice control/niku_1.0/baby/logo/logo.png'
def notify_msg(title = "msg from niku",message = 'some data not reccived corectly',icon=path):
    n = notify2.Notification(title,message,icon)
    n.set_timeout(5000)
    n.show()
#    n.close()
#notify_msg()


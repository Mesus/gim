import time
class timeTools:
    def __init__(self):
        print ''
    def ctwithymdhms(self):
        today = time.strftime('%Y%m%d %H:%M:%S', time.localtime(time.time()))
        return today
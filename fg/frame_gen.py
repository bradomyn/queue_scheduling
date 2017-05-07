import random

class frame_gen(object):

    BANDWIDTH = 800
    LEN_MIN = 64
    LEN_MAX = 1500
    QOS = 7

    def __init__(self, bandwidth = None, len_min = None, len_max = None):
        self.badwidth = bandwidth if bandwidth is not None else self.BANDWIDTH
        self.len_min = len_min if len_min is not None else self.LEN_MIN
        self.len_max = len_max if len_max is not None else self.LEN_MAX

    def frame_pay_load(self):
        return random.randint(self.len_min, self.len_max)
    
    def frame_qos(self):
        return random.randint(0, self.QOS)     

if __name__ == '__main__':
    fg = frame_gen()

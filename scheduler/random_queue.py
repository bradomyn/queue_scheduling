import random

class random_queue(object):

    def __init__(self):
        self.stat = 0

    def next_q(self):
        return random.randint(0,7)
        

if __name__ == '__main__':
    rq = random_queue()
    print rq.next_q()

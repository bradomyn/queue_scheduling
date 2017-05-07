import sys
import os
from collections import deque

class output_queue():
    
    NUM_QUEUE = 8
    LEN_QUEUE = 6400
    
    def __init__ (self, num_queue = None, len_queue = None) :
        self.num_queue = num_queue if num_queue is not None else self.NUM_QUEUE
        self.len_queue = len_queue if len_queue is not None else self.LEN_QUEUE
        self.out_queue = [deque(maxlen=len_queue) for y in range(num_queue)]

    def add_frame_queue(self, prio_queue, len_frame) :
        if sum(list(self.out_queue[prio_queue])) + len_frame > 6400 :
            print "overun queue", prio_queue, sum(self.out_queue[prio_queue])
        else :
            self.out_queue[prio_queue].append(len_frame) 
    
    def tx_frame_queue(self, queue):
        try:
            self.out_queue[queue].popleft()
        except:
            e = sys.exc_info()[0]
            print("<p>Error: %s</p> queue %d" % (e, queue))

if __name__ == '__main__':
    output_queue()


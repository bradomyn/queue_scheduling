from fg import frame_gen
from output_queue import output_queue 
from scheduler import random_queue

fg = frame_gen()
q = output_queue(8,10)
scheduler = random_queue()

for x in range(10000):

    pay_load = fg.frame_pay_load()
    qos = fg.frame_qos()
    
    q.add_frame_queue(qos, pay_load)
    
    tx_queue = scheduler.next_q()

    q.tx_frame_queue(tx_queue)


    
print list(q.out_queue[0])
print list(q.out_queue[1])
print list(q.out_queue[2])
print list(q.out_queue[3])
print list(q.out_queue[4])
print list(q.out_queue[5])
print list(q.out_queue[6])
print list(q.out_queue[7])


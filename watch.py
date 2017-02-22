import threading
import time


class Watch(threading.Thread):

    def __init__(self, queue, t_size):
        threading.Thread.__init__(self)
        self.queue = queue
        self.t_size = t_size

    def set_t_max(self, t_max):
        self.t_max = t_max

    def run(self):
        self.running = True
        start = time.time()
        previous = start
        elapsed = start - time.time()
        while elapsed <= self.t_max and self.running:
            time.sleep(self.t_size)
            current = time.time()
            elapsed = time.time() - start
            delta = current - previous
            previous = current
            self.queue.put(delta)

    def stop(self):
        self.running = False

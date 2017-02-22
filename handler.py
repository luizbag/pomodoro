import queue
import threading
from watch import Watch
from gi.repository import Gtk


class Handler:

    def __init__(self, lbl_time):
        self.q = queue.Queue()
        self.lbl_time = lbl_time
        self.watch = Watch(self.q, 1)

    def convert(self, t):
        m = int(t / 60)
        s = int(t % 60)
        return str(m).zfill(2) + ':' + str(s).zfill(2)

    def worker(self):
        self.rem = self.time
        while self.watch.is_alive():
            t = self.q.get()
            self.rem -= t
            self.lbl_time.set_text(self.convert(self.rem))
            self.q.task_done()

    def window_destroy_cb(self, *args):
        Gtk.main_quit()

    def btn_pomodoro_clicked_cb(self, button):
        self.lbl_time.set_text("25:00")
        self.time = 25 * 60.0

    def btn_short_break_clicked_cb(self, button):
        self.lbl_time.set_text("05:00")
        self.time = 5 * 60.0

    def btn_long_break_clicked_cb(self, button):
        self.lbl_time.set_text("10:00")
        self.time = 10 * 60.0

    def btn_start_clicked_cb(self, button):
        self.watch = Watch(self.q, 1)
        self.watch.set_t_max(self.time)
        self.watch.start()
        thread = threading.Thread(target=self.worker)
        thread.start()

    def btn_stop_clicked_cb(self, button):
        self.watch.stop()

    def btn_reset_clicked_cb(self, button):
        self.lbl_time.set_text(self.convert(self.time))

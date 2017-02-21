import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Keybinder', '3.0')
from gi.repository import Gtk
from gi.repository import Keybinder
from enum import Enum


class KeyBinds(Enum):
    pomodoro = "<Ctrl><Alt>P"
    short_break = "<Ctrl><Alt>S"
    long_break = "<Ctrl><Alt>L"
    timer = "<Ctrl><Alt>T"
    reset = "<Ctrl><Alt>R"
    quit = "<Ctrl><Alt>Q"


class Handler:

    def window_destroy_cb(self, *args):
        Gtk.main_quit()

    def btn_pomodoro_clicked_cb(self, button):
        lbl_time.set_text("25:00")

    def btn_short_break_clicked_cb(self, button):
        lbl_time.set_text("05:00")

    def btn_long_break_clicked_cb(self, button):
        lbl_time.set_text("10:00")

    def btn_start_clicked_cb(self, button):
        print("Start")

    def btn_stop_clicked_cb(self, button):
        print("Stop")

    def btn_reset_clicked_cb(self, button):
        print("Reset")


handler = Handler()


def callback(keystr):
    if keystr == KeyBinds.pomodoro.value:
        handler.btn_pomodoro_clicked_cb(None)
    elif keystr == KeyBinds.short_break.value:
        handler.btn_short_break_clicked_cb(None)
    elif keystr == KeyBinds.long_break.value:
        handler.btn_long_break_clicked_cb(None)
    elif keystr == KeyBinds.timer.value:
        handler.btn_start_clicked_cb(None)
        handler.btn_stop_clicked_cb(None)
    elif keystr == KeyBinds.reset.value:
        handler.btn_reset_clicked_cb(None)
    elif keystr == KeyBinds.quit.value:
        handler.window_destroy_cb(None)


if __name__ == "__main__":
    builder = Gtk.Builder()
    builder.add_from_file("./pomodoro.glade")
    builder.connect_signals(handler)
    window = builder.get_object("window")
    lbl_time = builder.get_object("lbl_time")
    window.show_all()
    Keybinder.init()
    for keystr in KeyBinds:
        Keybinder.bind(keystr.value, callback)
    Gtk.main()

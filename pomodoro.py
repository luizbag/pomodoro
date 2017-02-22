# -*- coding: utf-8-unix; -*-
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Keybinder', '3.0')
from gi.repository import Gtk
from gi.repository import Keybinder
from enum import Enum
from handler import Handler


class KeyBinds(Enum):
    pomodoro = "<Ctrl><Alt>P"
    short_break = "<Ctrl><Alt>S"
    long_break = "<Ctrl><Alt>L"
    timer = "<Ctrl><Alt>T"
    reset = "<Ctrl><Alt>R"
    quit = "<Ctrl><Alt>Q"


def callback(keystr):
    if keystr == KeyBinds.pomodoro.value:
        handler.btn_pomodoro_clicked_cb(None)
    elif keystr == KeyBinds.short_break.value:
        handler.btn_short_break_clicked_cb(None)
    elif keystr == KeyBinds.long_break.value:
        handler.btn_long_break_clicked_cb(None)
    elif keystr == KeyBinds.timer.value:
        if handler.watch and handler.watch.is_alive():
            handler.btn_stop_clicked_cb(None)
        else:
            handler.btn_start_clicked_cb(None)
    elif keystr == KeyBinds.reset.value:
        handler.btn_reset_clicked_cb(None)
    elif keystr == KeyBinds.quit.value:
        handler.window_destroy_cb(None)


if __name__ == "__main__":
    handler = Handler
    builder = Gtk.Builder()
    builder.add_from_file("./pomodoro.glade")
    window = builder.get_object("window")
    lbl_time = builder.get_object("lbl_time")
    handler = Handler(lbl_time)
    builder.connect_signals(handler)
    window.show_all()
    Keybinder.init()
    for keystr in KeyBinds:
        Keybinder.bind(keystr.value, callback)
    Gtk.main()

#!/usr/bin/env python3

from tkinter import Tk

import keyboard

from gui import MonitorGUI

root = Tk()
root.attributes('-topmost', 1)
print(root.winfo_screenheight() - root.winfo_reqheight())

position = {
    'x': root.winfo_screenwidth() - root.winfo_reqwidth() - 230,
    'y': root.winfo_screenheight() - root.winfo_reqheight() + 100
}
gui = MonitorGUI(root, width=420, height=50, position=position, title='KeyboardMonitor v1')
keyboard.on_press(gui.press_key)
keyboard.on_release(gui.release_key)
root.mainloop()
keyboard.wait()

# todo make async

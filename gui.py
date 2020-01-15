#!/usr/bin/env python3
from tkinter import Label


class MonitorGUI:

    def __init__(self, master, title, width, height, position):

        self.master = master
        self.master.title(title)
        self.master.geometry(f"{width}x{height}+{position['x']}+{position['y']}")
        self.master.resizable(False, False)

        self.btn_style = {
            'font': ('Arial', 24),
            'fg': 'black',
            'bg': 'white',
            'width': 5,
            'height': 5
        }
        self.ctrl_btn = Label(self.master, **self.btn_style)
        self.shift_btn = Label(self.master, **self.btn_style)
        self.alt_btn = Label(self.master, **self.btn_style)
        self.some_btn = Label(self.master, **self.btn_style)

        self.ctrl_btn.pack(side='left', padx=10, pady=5)
        self.shift_btn.pack(side='left', padx=10, pady=5)
        self.alt_btn.pack(side='left', padx=10, pady=5)
        self.some_btn.pack(side='left', padx=10, pady=5)

    def press_key(self, event):
        if event.name == 'ctrl':
            self.ctrl_btn['text'] = 'CTRL'
        elif event.name == 'shift':
            self.shift_btn['text'] = 'SHIFT'
        elif event.name == 'alt':
            self.alt_btn['text'] = 'ALT'
        else:
            self.some_btn['text'] = event.name
        self.master.update()

    def release_key(self, event):
        if event.name == 'ctrl':
            self.ctrl_btn['text'] = ''
        elif event.name == 'shift':
            self.shift_btn['text'] = ''
        elif event.name == 'alt':
            self.alt_btn['text'] = ''
        else:
            self.some_btn['text'] = ''
        self.master.update()

import tkinter as tk
import os

from datetime import datetime
from tkinter import INSERT, END
from tkinter import filedialog as fd
from gui import Gui

class App(Gui):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.__set_path()
        self.valid_path: bool = False

    def get_folder(self):
        self.shape_path: str = fd.askdirectory()
        self.file_entry.insert(0, self.shape_path)

    def run(self):
        self.__set_path()
        if not os.path.exists(self.shape_path):
            self.__write("Path does not exist...")            

    def __set_path(self):
        self.shape_path: str = self.file_entry.get()

    def __write(self, message: str):
        self.console.insert(INSERT, f'{self.__message(message)}\n')

    def __message(self, string):
        return f'{datetime.today()}: {string}'
        
if __name__ == '__main__':
    app = App()
    app.mainloop()
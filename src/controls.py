import tkinter as tk
import os
import time

from datetime import datetime
from tkinter import INSERT, END, DISABLED, NORMAL
from tkinter import filedialog as fd
from gui import Gui
from cShape import ShapeData

class App(Gui):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.shape_path:str = None
        self.__set_path()
        self.run_btn.config(state=DISABLED)
        self.import_btn.config(state=DISABLED)
        self.browse_text = self.browse_sv.get()
        self.fields_len: int = None
        self.records_len: int = None
        self.shapes_len: int = None
        
    def get_folder(self):
        self.shape_path: str = fd.askopenfilename(filetypes=[("Shape Files", ".shp")])
        self.file_entry.insert(0, self.shape_path)
        self.__toggle_btns()

    def import_data(self):
        is_valid = self.__validate_path() 
        if is_valid:
            new_shape = ShapeData(self.shape_path)
            self.fields_len = len(new_shape.fields)
            self.__write(f'{self.fields_len} fields loaded')
            self.records_len = len(new_shape.records)
            self.__write(f'{self.records_len} records loaded')
            self.shapes_len = len(new_shape.shapes)
            self.__write(f'{self.shapes_len} shapes loaded')
            self.__set_labels()
        else: 
            self.__write("Invalid path...")

    def run(self):
        self.__set_path()
        if not os.path.exists(self.shape_path):
            self.__write("Path does not exist...")  

    def file_entry_event(self, event): 
        self.__toggle_btns()
    
    def __set_path(self):
        self.shape_path: str = self.browse_sv.get()

    def __write(self, message: str):
        self.console.insert(INSERT, f'{self.__message(message)}\n')

    def __message(self, string):
        return f'{datetime.today()}: {string}'
    
    def __validate_path(self) -> bool:
        if os.path.exists(self.shape_path) and self.shape_path.endswith('.shp'):
            return True
        else:
            return False
        
    def __toggle_btns(self):
        self.__set_path()
        if len(self.browse_sv.get()) > 0:
            self.run_btn.config(state=NORMAL)
            self.import_btn.config(state=NORMAL)
        else:
            self.run_btn.config(state=DISABLED)
            self.import_btn.config(state=DISABLED)

    def __set_labels(self):
        self.fields_label.config(text=f'Fields: {self.fields_len}')
        self.records_label.config(text=f'Records: {self.records_len}')
        self.shapes_label.config(text=f'Shapes: {self.shapes_len}')


        
if __name__ == '__main__':
    pass
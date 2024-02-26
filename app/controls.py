import tkinter as tk
import os
import time
import geopandas as gp
import matplotlib.pyplot as plt

from datetime import datetime
from tkinter import INSERT, END, DISABLED, NORMAL, StringVar
from tkinter import filedialog as fd
from gui import Gui
from cShape import ShapeData

class App(Gui):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.shape_path:str = None
        self.file: str = None
        self.__set_path()
        self.console.config(state=DISABLED)
        self.preview_btn.config(state=DISABLED)
        self.run_btn.config(state=DISABLED)
        self.import_btn.config(state=DISABLED)
        self.file_entry.config(state=NORMAL)
        self.browse_btn.config(state=NORMAL)
        self.browse_text = self.browse_sv.get()
        self.fields_len: int = None
        self.records_len: int = None
        self.shapes_len: int = None
        self.data_imported: bool = False
        self.shape = None
        
    def get_folder(self):
        self.shape_path: str = fd.askopenfilename(filetypes=[("Shape Files", ".shp")])
        self.file_entry.insert(0, self.shape_path)
        self.__refresh()

    def import_data(self):
        is_valid = self.__validate_path() 
        if is_valid:
            self.shape = ShapeData(self.shape_path)
            self.file = os.path.basename(self.shape_path)
            self.title.config(text=self.file)
            self.fields_len = len(self.shape.fields)
            self.__write(f'{self.fields_len} fields loaded from {self.file}')
            self.records_len = len(self.shape.records)
            self.__write(f'{self.records_len} records loaded {self.file}')
            self.shapes_len = len(self.shape.shapes)
            self.__write(f'{self.shapes_len} shapes loaded {self.file}')
            self.__set_labels()
            self.data_imported = True
            self.__refresh()
        else: 
            self.__write("Invalid path...")

    def export(self):
        new_file = f'{fd.asksaveasfilename(filetypes=[("Excel Files", "*.xlsx")])}'
        if not new_file.endswith('.xlsx'):
            new_file +='.xlsx'
        print(new_file)
        self.__disable_gui()
        self.__write(f"Writing to {os.path.basename(new_file)}")
        try:
            self.shape.data.to_excel(new_file)
            self.__write(f"Save complete")
            self.__refresh()
        except Exception as e:
            self.__write("Something went wrong")
            self.__refresh()

    def file_entry_event(self, event): 
        self.__set_path()
        self.__refresh()

    def preview(self):
        df = gp.read_file(self.shape_path)
          
        ax = df.plot(
            'auto',
            column = 'Covertype',
            figsize=(15, 10),
            legend = True,            
        )
        self.__disable_gui()
        plt.show()
        self.__refresh()

    def __refresh(self):
        self.console.config(state=DISABLED)
        self.file_entry.config(state=NORMAL)
        self.browse_btn.config(state=NORMAL)

        if len(self.shape_path) > 0:
            self.import_btn.config(state=NORMAL)
        else:
            self.import_btn.config(state=DISABLED)

        if self.data_imported:
            self.run_btn.config(state=NORMAL)
            self.preview_btn.config(state=NORMAL)
        else:
            self.preview_btn.config(state=DISABLED)
            self.run_btn.config(state=DISABLED)
        
    
    def __set_path(self):
        self.shape_path: str = self.browse_sv.get()

    def __write(self, message: str):
        self.console.config(state=NORMAL)
        self.console.insert(END, f'{self.__message(message)}\n')
        self.console.config(state=DISABLED)

    def __message(self, string):
        return f'{datetime.today()}: {string}'
    
    def __validate_path(self) -> bool:
        if os.path.exists(self.shape_path) and self.shape_path.endswith('.shp'):
            return True
        else:
            return False

    def __set_labels(self):
        self.fields_label.config(text=f'Fields: {self.fields_len}')
        self.records_label.config(text=f'Records: {self.records_len}')
        self.shapes_label.config(text=f'Shapes: {self.shapes_len}')

    def __disable_gui(self):
        self.console.config(state=DISABLED)
        self.preview_btn.config(state=DISABLED)
        self.run_btn.config(state=DISABLED)
        self.import_btn.config(state=DISABLED)
        self.file_entry.config(state=DISABLED)
        self.browse_btn.config(state=DISABLED)


        
if __name__ == '__main__':
    pass
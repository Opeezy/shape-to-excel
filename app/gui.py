import tkinter as tk

from tkinter import ttk, StringVar
# from styles import *


class Gui(tk.Tk):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)

        '''Root Settings'''
        self.title("Shape to Excel")
        #self.geometry("500x500")
        #self.resizable(False, False)
        #self.attributes('-fullscreen', True)
        self.state('zoomed')

        '''Variables'''

        self.browse_sv = StringVar()

        '''Widgets'''

        # Master
        self.master_frame = ttk.Frame(self)

        # Console
        self.console = tk.Text(self.master_frame, height=20, font=('Consolas 9'), bg='white', fg='black')

        # Info and Buttons
        self.run_frame = ttk.Frame(self.master_frame)
        self.run_info_frame = ttk.Frame(self.run_frame)
        self.title = ttk.Label(self.run_info_frame, text='<FILE>', anchor='center')
        self.run_info_details= ttk.Frame(self.run_info_frame)
        self.single_details = ttk.Frame(self.run_info_details)
        self.fields_label = ttk.Label(self.single_details, text='Fields:')
        self.records_label = ttk.Label(self.single_details, text='Records:')
        self.shapes_label = ttk.Label(self.single_details, text='Shapes:')
        self.batch_details = ttk.Frame(self.run_info_details)
        self.run_divider = ttk.Separator(self.run_frame, orient='vertical')
        self.run_buttons_frame = ttk.Frame(self.run_frame)
        self.preview_btn = ttk.Button(self.run_buttons_frame, width=10, text='Preview', command=self.preview)
        self.import_btn = ttk.Button(self.run_buttons_frame, width=10, text='Import', command=self.import_data)
        self.run_btn = ttk.Button(self.run_buttons_frame, width=10, text='Export', command=self.export)

        # Divider
        self.browse_divider = ttk.Separator(self.master_frame, orient='horizontal')

        # File browser
        self.file_frame = ttk.Frame(self.master_frame)
        self.file_entry = ttk.Entry(self.file_frame, width=68, textvariable=self.browse_sv)
        self.browse_btn = ttk.Button(self.file_frame, text='Browse', width=10, command=self.get_folder)

        '''Grid Config'''

        # Root
        self.rowconfigure(index=0, weight=1)
        self.columnconfigure(index=0, weight=1)

        # Master
        self.master_frame.rowconfigure(index=0, weight=4)
        self.master_frame.rowconfigure(index=1, weight=2)
        self.master_frame.rowconfigure(index=3, weight=1)
        self.master_frame.columnconfigure(index=0, weight=1)

        # Info and buttons
        self.run_frame.rowconfigure(index=0, weight=1)
        self.run_frame.columnconfigure(index=0, weight=2)
        self.run_info_frame.rowconfigure(index=1, weight=2)
        self.run_info_frame.columnconfigure(index=0, weight=1)
        self.run_info_details.rowconfigure(index=0, weight=1)
        self.run_info_details.columnconfigure(index=0, weight=1)
        self.run_info_details.columnconfigure(index=1, weight=1)
        self.single_details.rowconfigure(index=0, weight=1)
        self.single_details.rowconfigure(index=1, weight=1)
        self.single_details.rowconfigure(index=2, weight=1)
        self.single_details.columnconfigure(index=0, weight=1)
        self.run_buttons_frame.rowconfigure(index=0, weight=1)
        self.run_buttons_frame.rowconfigure(index=1, weight=1)
        self.run_buttons_frame.rowconfigure(index=2, weight=1)
        self.run_buttons_frame.columnconfigure(index=0, weight=1)

        # File browser
        self.file_frame.columnconfigure(index=1, weight=1)
        
        '''Gridding'''

        # Master
        self.master_frame.grid(row=0, column=0, sticky='nsew')  

        # Console      
        self.console.grid(row=0, column=0, sticky='nsew', padx=4, pady=4)

        # Info and buttons
        self.run_frame.grid(row=1, column=0, sticky='nsew')
        self.run_info_frame.grid(row=0, column=0, sticky='nsew')
        self.title.grid(row=0, column=0, sticky='new')
        self.run_info_details.grid(row=1, column=0, sticky='nsew')
        self.fields_label.grid(row=0, column=0, sticky='ew', padx=2)
        self.single_details.grid(row=0, column=0, sticky='nsew')
        self.records_label.grid(row=1, column=0, sticky='ew', padx=2)
        self.shapes_label.grid(row=2, column=0, sticky='ew', padx=2) 
        self.batch_details.grid(row=0, column=1, sticky='nsew')
        self.run_divider.grid(row=0, column=1, sticky='ns', pady=3)
        self.run_buttons_frame.grid(row=0, column=2, sticky='nsew')
        self.preview_btn.grid(row=0, column=0, sticky='e', padx=4, pady=4)
        self.import_btn.grid(row=1, column=0, sticky='e', padx=4, pady=4)
        self.run_btn.grid(row=2, column=0, sticky='e', padx=4, pady=4)

        # Divider
        self.browse_divider.grid(row=2, column=0, sticky='ews')

        # File browser
        self.file_frame.grid(row=3, column=0, sticky='ew')
        self.file_entry.grid(row=0, column=0, sticky='w', padx=4, pady=2,columnspan=2)
        self.browse_btn.grid(row=0, column=1, sticky='e', padx=4)

        '''Bindings'''

        # File browser
        self.file_entry.bind("<KeyRelease>", self.file_entry_event)

        '''Styles'''

        # Testing
        run_frame_style = ttk.Style()
        run_frame_style.configure("run_frame_style.TFrame", background="red")

        run_info_frame_style = ttk.Style()
        run_info_frame_style .configure("run_info_frame_style.TFrame", background="blue")

        run_info_details_style = ttk.Style()
        run_info_details_style .configure("run_info_details_style.TFrame", background="green")

        run_buttons_frame_style = ttk.Style()
        run_buttons_frame_style .configure("run_buttons_frame_style.TFrame", background="black")
        
        


if __name__ == '__main__':
    pass
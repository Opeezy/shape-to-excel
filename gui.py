import tkinter as tk

from tkinter import ttk 


class Gui(tk.Tk):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title("Shape to Excel")
        self.geometry("500x500")
        self.resizable(False, False)
        style = ttk.Style()
        style.configure("style.TFrame", background="red")

        # Widgets
        self.master_frame = ttk.Frame(self)
        self.console = tk.Text(self.master_frame, height=20)
        self.run_frame = ttk.Frame(self.master_frame)
        self.import_btn = ttk.Button(self.run_frame, width=10, text='Import')
        self.run_btn = ttk.Button(self.run_frame, width=10, text='Run', command=self.run)
        self.divider = ttk.Separator(self.master_frame, orient='horizontal')
        self.file_frame = ttk.Frame(self.master_frame)
        self.file_entry = ttk.Entry(self.file_frame, width=68)
        self.browse_btn = ttk.Button(self.file_frame, text='Browse', width=10, command=self.get_folder)

        # Grid Config
        self.rowconfigure(index=0, weight=1)
        self.columnconfigure(index=0, weight=1)
        self.master_frame.rowconfigure(index=0, weight=4)
        self.master_frame.rowconfigure(index=1, weight=2)
        self.master_frame.rowconfigure(index=2, weight=1)
        self.master_frame.rowconfigure(index=3, weight=1)
        self.master_frame.columnconfigure(index=0, weight=1)
        self.run_frame.rowconfigure(index=0, weight=1)
        self.run_frame.columnconfigure(index=0, weight=1)
        self.run_frame.columnconfigure(index=1, weight=1)
        self.file_frame.columnconfigure(index=1, weight=1)
        
        # Gridding
        self.master_frame.grid(row=0, column=0, sticky='nsew')        
        self.console.grid(row=0, column=0, sticky='nsew', padx=4)
        self.run_frame.grid(row=1, column=0, sticky='nsew')
        self.import_btn.grid(row=0, column=0, sticky='wn', padx=4, pady=4)
        self.run_btn.grid(row=0, column=1, sticky='en', padx=4, pady=4)
        self.divider.grid(row=2, column=0, sticky='ews')
        self.file_frame.grid(row=3, column=0, sticky='ew')
        self.file_entry.grid(row=0, column=0, sticky='w', padx=4, pady=2,columnspan=2)
        self.browse_btn.grid(row=0, column=1, sticky='e', padx=4)
        


if __name__ == '__main__':
    app = App()
    app.mainloop()
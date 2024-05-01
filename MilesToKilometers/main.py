import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

class App:
    def __init__(self, window: tk.Tk) -> None:
        window.geometry('300x150')
        window.title('Miles to Kilometers')
        
        self.titleLabel = ttk.Label(master=window, text='Miles to Kilometers', font="Calibri 24 bold")
        self.titleLabel.pack()

        self.entryInt = tk.IntVar()
        self.outputStr = tk.StringVar()

        self.inputFrame = ttk.Frame(master=window)
        self.entry = ttk.Entry(master=self.inputFrame, textvariable=self.entryInt)
        self.button = ttk.Button(master=self.inputFrame, text="Convert", command=self.convert)
        self.entry.pack(side='left', padx=15)
        self.button.pack(side='left')
        self.inputFrame.pack(pady=10)
        
        self.outputLabel = ttk.Label(
            master=window,
            textvariable=self.outputStr,
            font="Calibri 24"
            )
        self.outputLabel.pack(pady=5)

    def convert(self, *args):
        mileInput = self.entryInt.get()
        kmOutput = mileInput * 1.61
        self.outputStr.set(f"{kmOutput} miles")
    


def main():
    window = ttk.Window(themename= 'journal')
    App(window)
    window.mainloop()

if __name__ == "__main__":
    main()
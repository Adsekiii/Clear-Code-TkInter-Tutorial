import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self, window) -> None:
        self.label = ttk.Label(master=window, text="Normal text")
        self.entry = ttk.Entry(master=window)
        self.button = ttk.Button(master= window, text="Click", command=self.buttonFunc)
        self.resetButton = ttk.Button(master= window, text="Reset", command=self.resetButtonFunc)
        
        self.label.pack()
        self.entry.pack()
        self.button.pack()
        self.resetButton.pack()

    def buttonFunc(self):
        #print(self.entry.get())
        entryText = self.entry.get()
        self.label['text'] = entryText    #self.label.config(text="Magical text")
        self.entry['state'] = 'disabled'
        
    def resetButtonFunc(self):
        self.label['text'] = 'some text'
        self.entry['state'] = 'enabled'
    
def main() -> None :
    window = tk.Tk()
    App(window)
    window.mainloop()

if __name__ == "__main__":
    main()
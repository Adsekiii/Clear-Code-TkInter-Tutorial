import tkinter as tk
from tkinter import ttk


class App:
    def __init__(self, window: tk.Tk) -> None:
        window.geometry("700x500")
        window.title("MultiLineText")
        
        self.userInput = tk.StringVar()
        
        self.topText = ttk.Label(master=window, text="Notes")     
        self.exercise = ttk.Label(master=window, text="label")   
        self.textFrame = tk.Text(master=window)
        
        self.buttonFrame = ttk.Frame(master=window)
        self.entry = ttk.Entry(master=window, textvariable=self.userInput)
        self.button = ttk.Button(master=window, text="Click", command=self.printEntry)
        self.exerciseButton = ttk.Button(master=window, text="Exercise Button", command=lambda: print("Hello") )#self.exercisePrint)
        
        #packing the app itself 
        self.topText.pack()
        self.textFrame.pack()
        self.entry.pack()
        self.exercise.pack()
        self.button.pack()
        self.exerciseButton.pack()
        
    def printEntry(self) -> None :
        print(f"text: {self.entry.get()}")
    
    # def exercisePrint(self):
    #     print("Hello")

def main() -> None :
    window = tk.Tk()
    App(window)
    window.mainloop()

if __name__ == "__main__":
    main()
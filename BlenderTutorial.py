import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import TutorialProgressMonitor
import os
import TutorialStrings as ts

class BlenderTutorial:

    def __init__(self, filename) -> None:
        self.filename = filename

        self.root = tk.Tk()
        self.root.geometry("500x250+50+50")
        self.root.title("Welcome to Blender")
        self.root.attributes('-topmost', 1)

        self.step_label = tk.Label(self.root, text=ts.instructions['i1'], font=("Arial", 18), wraplength=300, justify="center")
        self.step_label.pack(padx=10, pady=20)

        self.file_event_handler = TutorialProgressMonitor.Tm(self, self.filename)
        self.file_event_handler.startObserving()

        self.root.protocol("WM_DELETE_WINDOW", self.onClosing)

        self.progress = {
            '1': False,
            '2': False
        }
        
        #continue button  
        self.step_count = 0
        self.inst_count = 2
        print(self.inst_count)
        
        self.continue_btn = Button(self.root, text = 'Continue', command = self.nextInstruction)
        self.continue_btn.pack(pady=10)
        self.continue_btn.pack(side = 'bottom')
        
        self.root.mainloop()
    
    #function for replacing instructions
    def nextInstruction(self): 
        
        #keep going
        if (self.inst_count == 2):
              self.step_label.config(text = ts.instructions['i2'])
              self.inst_count +=1

        elif (self.inst_count == 3):
              self.step_label.config(text = ts.instructions['i3'])
              self.inst_count +=1
              
    #checks progress.txt        
    def onProgressChange(self):
        #self.showMessage("Progress Changed!", "")
        # 1. read last line of file
        # 2. check if step 1 is finished
        # 3. change the label text
        lastLine = self.readProgress()
        
        #progress checks. keep repeating
        if (lastLine == "1_done"): 
            self.progress['1'] = True
            self.step_label.config(text="Step 2")

        if (lastLine == "2_done"): 
            self.progress['2'] = True
            self.step_label.config(text="Step 3")

    def showMessage(self, msg, title):
        messagebox.showinfo(title=title, message=msg)

    def onClosing(self):
        self.file_event_handler.stopObserving()
        self.root.destroy()

    def readProgress(self):
        with open(self.filename, "rb") as file:
            try:
                file.seek(-2, os.SEEK_END)
                while file.read(1) != b'\n':
                    file.seek(-2, os.SEEK_CUR)
            except OSError:
                file.seek(0)
            last_line = file.readline().decode()
            return last_line

    #function for progress bar

if __name__ == "__main__":
    BlenderTutorial("/users/vivian/Documents/blender/progress.txt")

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
        self.root.geometry("500x300+50+50")
        self.root.title("Welcome to Blender")
        self.root.attributes('-topmost', 1)

        self.step_label = tk.Label(self.root, text=ts.instructions['i1'], font=("Arial", 18), wraplength=300, justify="center")
        self.step_label.pack(padx=10, pady=20)

        self.file_event_handler = TutorialProgressMonitor.Tm(self, self.filename)
        self.file_event_handler.startObserving()

        self.root.protocol("WM_DELETE_WINDOW", self.onClosing)

        self.progress = {
            '1': False,
            '2': False,
            '3': False
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
        
        elif (self.inst_count == 4):
              self.root.title("View Port Controls: Looking Around")
              self.step_label.config(text = ts.instructions['i4'])
              self.inst_count +=1
        
        elif (self.inst_count == 5):
              self.step_label.config(text = ts.instructions['i5'])
              self.inst_count +=1
        
        elif (self.inst_count == 6):
              self.step_label.config(text = ts.instructions['i6'])
              self.inst_count +=1
        
        elif (self.inst_count == 7):
              self.root.title("View Port Controls: Orthographic views")
              self.step_label.config(text = ts.instructions['i7'])
              self.inst_count +=1
        
        elif (self.inst_count == 8):
              self.root.title(" ")
              self.step_label.config(text = ts.instructions['i8'])
              self.inst_count +=1
              
        elif (self.inst_count == 9):
              self.root.title("Adding Objects")
              self.step_label.config(text = ts.instructions['i9'])
              self.inst_count +=1
              
        elif (self.inst_count == 10):
              self.step_label.config(text = ts.instructions['i10'])
              self.inst_count +=1
        
        elif (self.inst_count == 11):
            # 1. check if cube is added
            if self.progress['1']:
                #change text
                self.step_label.config(text = ts.instructions['i11'])
                self.inst_count +=1
            else:
                # popup a error button
                self.errorPop("Add the cube to continue!")
        
        elif (self.inst_count == 12):
              self.root.title("Deleting Objects and Undo/Redos")
              self.step_label.config(text = ts.instructions['i12'])
              self.inst_count +=1  
        
        elif (self.inst_count == 13):
              self.step_label.config(text = ts.instructions['i13'])
              self.inst_count +=1   
        
        elif (self.inst_count == 14):
            if self.progress['2'] == True:
                #change text
                self.step_label.config(text = ts.instructions['i14'])
                self.inst_count +=1 
            else:
                # popup a error button
                self.errorPop("Delete the cube to continue!")  
        
        elif (self.inst_count == 15):
              self.step_label.config(text = ts.instructions['i15'])
              self.inst_count +=1
        
        elif (self.inst_count == 16):
              self.step_label.config(text = ts.instructions['i16'])
              self.inst_count +=1
        
        elif (self.inst_count == 17):
              self.step_label.config(text = ts.instructions['i17'])
              self.inst_count +=1
              
        elif (self.inst_count == 18):
            if self.progress['3'] == True:
                #change text
                self.step_label.config(text = ts.instructions['i18'])
                self.inst_count +=1
            else:
                # popup a error button
                self.errorPop("Adjust the vertices and fill-type to continue!")
                
        elif (self.inst_count == 19):
              self.step_label.config(text = ts.instructions['i19'])
              self.inst_count +=1
        
         
    
    #function for error message
    def errorPop(self, message):
        self.root.title(" ")
        self.error_pop = Toplevel(self.root)
        self.error_pop.geometry("100x60")
        self.error_pop.config(bg ="red")
        self.error_label = Label(self.error_pop, text=message, bg="red", fg="white", wraplength=75, justify="center")
        self.error_label.pack()
        self.error_pop.eval('tk::PlaceWindow . center')
        self.error_pop.pack()                 
              
    #checks progress.txt        
    def onProgressChange(self):
        #self.showMessage("Progress Changed!", "")
        # 1. read last line of file
        # 2. check if step 1 is finished
        # 3. change the label text
        lastLine = self.readProgress()
        
        #progress checks. keep repeating
        # add cube
        if (lastLine == "1_done"): 
            self.progress['1'] = True

        #delete cube
        if (lastLine == "2_done"): 
            self.progress['2'] = True
        
        #circle vertices and fill
        if (lastLine == "3_done"): 
            self.progress['3'] = True

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

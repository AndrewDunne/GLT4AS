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
            '3': False,
            '4': False,
            '5': False,
            '6': False,
            '7': False,
            '8': False,
            '9': False
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
              print(self.inst_count)
        
        elif (self.inst_count == 18):
              self.step_label.config(text = ts.instructions['i18'])
              self.inst_count +=1
              
        #vertices check      
        elif (self.inst_count == 19):
            if self.progress['3'] == True:
                print("check 3 is passed")
                #change text
                self.step_label.config(text = ts.instructions['i19'])
                print("text changed line run")
                self.inst_count +=1
            else:
                # popup a error button
                self.errorPop("Adjust the vertices and fill-type to continue!")
        
        elif (self.inst_count == 20): 
              self.root.title("Basic Transformations")
              self.step_label.config(text = ts.instructions['i20'])
              self.inst_count +=1
              
        elif (self.inst_count == 21): 
              self.step_label.config(text = ts.instructions['i21'])
              self.inst_count +=1
              
        #move cube check     
        elif (self.inst_count == 22): 
              if self.progress['4'] == True:
                #change text
                self.step_label.config(text = ts.instructions['i22'])
                self.inst_count +=1
              else:
                # popup a error button
                self.errorPop("Move the cube to continue")
        
        elif (self.inst_count == 23): 
              self.step_label.config(text = ts.instructions['i23'])
              self.inst_count +=1
              
        #rotate cube check
        elif (self.inst_count == 24): 
              if self.progress['5'] == True:
                #change text
                self.step_label.config(text = ts.instructions['i24'])
                self.inst_count +=1
              else:
                # popup a error button
                self.errorPop("Rotate the cube to continue")
        
        elif (self.inst_count == 25): 
              self.step_label.config(text = ts.instructions['i25'])
              self.inst_count +=1
        
        #scale cube check
        elif (self.inst_count == 26): 
              if self.progress['6'] == True:
                #change text
                self.step_label.config(text = ts.instructions['i26'])
                self.inst_count +=1
              else:
                # popup a error button
                self.errorPop("Scale the cube to continue")
        
        elif (self.inst_count == 27):
              self.step_label.config(text = ts.instructions['i27'])
              self.inst_count +=1
        
        elif (self.inst_count == 28):
              self.root.title("Transform Panel")
              self.step_label.config(text = ts.instructions['i28'])
              self.inst_count +=1
        
        elif (self.inst_count == 29):
              self.root.title("Selecting Objects")
              self.step_label.config(text = ts.instructions['i29'])
              self.inst_count +=1
        
        elif (self.inst_count == 30):
              self.step_label.config(text = ts.instructions['i30'])
              self.inst_count +=1
        
        elif (self.inst_count == 31):
              self.step_label.config(text = ts.instructions['i31'])
              self.inst_count +=1
                   
        elif (self.inst_count == 32): 
              self.step_label.config(text = ts.instructions['i32'])
              self.inst_count +=1
        
        elif (self.inst_count == 33): 
              self.root.title("Flat and Smooth Shading")
              self.step_label.config(text = ts.instructions['i33'])
              self.inst_count +=1
        
        elif (self.inst_count == 34):  
              self.step_label.config(text = ts.instructions['i34'])
              self.inst_count +=1
        
        #smooth shading check
        elif (self.inst_count == 35):  
              if self.progress['7'] == True:
                #change text
                self.step_label.config(text = ts.instructions['i35'])
                self.inst_count +=1
              else:
                # popup a error button
                self.errorPop("shade the sphere smooth to continue")
        
        elif (self.inst_count == 36):  
              self.step_label.config(text = ts.instructions['i36'])
              self.inst_count +=1
        
        elif (self.inst_count == 37):  
              self.step_label.config(text = ts.instructions['i37'])
              self.inst_count +=1
        
        #auto shading check
        elif (self.inst_count == 38):  
              if self.progress['8'] == True:
                #change text
                self.step_label.config(text = ts.instructions['i38'])
                self.inst_count +=1
              else:
                # popup a error button
                self.errorPop("turn on auto shade smooth to continue")
        
        elif (self.inst_count == 39):
              self.root.title("Duplicating Objects") 
              self.step_label.config(text = ts.instructions['i39'])
              self.inst_count +=1
        
        elif (self.inst_count == 40):  
              self.step_label.config(text = ts.instructions['i40'])
              self.inst_count +=1
        
        elif (self.inst_count == 41):  
              self.step_label.config(text = ts.instructions['i41'])
              self.inst_count +=1
        
        #check duplicate object
        elif (self.inst_count == 42):  
              self.step_label.config(text = ts.instructions['i42'])
              self.inst_count +=1
        
        #done with object mode tutorial
        #start of edit mode tutorial
    
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
        
        #cube move
        if (lastLine == "4_done"): 
            self.progress['4'] = True
        
        #cube rotate
        if (lastLine == "5_done"): 
            self.progress['5'] = True
        
        #cube scale
        if (lastLine == "6_done"): 
            self.progress['6'] = True
        
        #sphere shade smooth 
        if (lastLine == "7_done"): 
            self.progress['7'] = True
            
        #cylinder auto shade smooth
        if (lastLine == "8_done"): 
            self.progress['8'] = True
        
        #duplicate object 
        if (lastLine == "9_done"): 
            self.progress['9'] = True

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

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
            '9': False,
            '10': False,
            '11': False,
            '12': False,
            '13': False,
            '14': False,
            '15': False,
            '16': False,
            '17': False,
            '18': False,
            '19': False,
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
                self.errorPop("Add the cube to continue")
        
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
                self.errorPop("Delete the cube to continue")  
        
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
                self.errorPop("Shade the sphere smooth to continue")
        
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
                self.errorPop("Turn on auto shade smooth to continue")
        
        elif (self.inst_count == 39):
              self.root.title("Duplicating Objects") 
              self.step_label.config(text = ts.instructions['i39'])
              self.inst_count +=1
        
        elif (self.inst_count == 40):  
              self.step_label.config(text = ts.instructions['i40'])
              self.inst_count +=1

        #check duplicate object
        elif (self.inst_count == 41):  
              if self.progress['9'] == True:
                #change text
                self.step_label.config(text = ts.instructions['i41'])
                self.inst_count +=1
              else:
                # popup a error button
                self.errorPop("Duplicate the object to continue")
        elif (self.inst_count == 42):
              self.root.title("Switching Modes")  
              self.step_label.config(text = ts.instructions['i42'])
              self.inst_count +=1
            
        #done with object mode tutorial
        #start of edit mode tutorial
      
         #check edit mode
        elif (self.inst_count == 43):  
            if self.progress['10'] == True:
                  self.step_label.config(text = ts.instructions['i43'])
                  self.inst_count += 1
            else:
                  self.errorPop("Change to edit mode to continue")
      
        elif (self.inst_count == 44):  
              self.step_label.config(text = ts.instructions['i44'])
              self.inst_count +=1
        elif (self.inst_count == 45): 
              self.root.title("Vertices, Edges, and Faces") 
              self.step_label.config(text = ts.instructions['i45'])
              self.inst_count +=1
        elif (self.inst_count == 46):
              self.root.title("Selecting and Transforming in Edit Mode")  
              self.step_label.config(text = ts.instructions['i46'])
              self.inst_count +=1
        #cube edited check
        elif (self.inst_count == 47):  
            if self.progress['11'] == True:
                  self.step_label.config(text = ts.instructions['i47'])
                  self.inst_count += 1
            else:
                  self.errorPop("Edit the cube to continue")
        
      #change selection mode check
        elif (self.inst_count == 48):
            self.root.title("Loop Select")  
            if self.progress['12'] == True:
                  self.step_label.config(text = ts.instructions['i48'])
                  self.inst_count += 1
            else:
                  self.errorPop("Change selection mode to continue")
        elif (self.inst_count == 49):  
              self.step_label.config(text = ts.instructions['i49'])
              self.inst_count +=1
        elif (self.inst_count == 50):
              self.root.title("Proportional editing")  
              self.step_label.config(text = ts.instructions['i50'])
              self.inst_count +=1
        elif (self.inst_count == 51):  
              self.step_label.config(text = ts.instructions['i51'])
              self.inst_count +=1
        elif (self.inst_count == 52):  
              self.step_label.config(text = ts.instructions['i52'])
              self.inst_count +=1
      #proportional editing check
        elif (self.inst_count == 53):  
            if self.progress['13'] == True:
                  self.step_label.config(text = ts.instructions['i53'])
                  self.inst_count += 1
            else:
                  self.errorPop("Proportionally edit the cube to continue")

      # geometry edited check
        elif (self.inst_count == 54):  
            if self.progress['14'] == True:
                  self.step_label.config(text = ts.instructions['i54'])
                  self.inst_count += 1
            else:
                  self.errorPop("Edit the geometry to continue")
        elif (self.inst_count == 55):
              self.root.title("Proportional Editing Falloff")  
              self.step_label.config(text = ts.instructions['i55'])
              self.inst_count +=1
        elif (self.inst_count == 56):  
              self.step_label.config(text = ts.instructions['i56'])
              self.inst_count +=1
      # falloff set to sharp check
        elif (self.inst_count == 57):  
            if self.progress['15'] == True:
                  self.step_label.config(text = ts.instructions['i57'])
                  self.inst_count += 1
            else:
                  self.errorPop("Set fall off to sharp to continue")
        elif (self.inst_count == 58):
              self.root.title("Extrude")  
              self.step_label.config(text = ts.instructions['i58'])
              self.inst_count +=1
        elif (self.inst_count == 59):  
              self.step_label.config(text = ts.instructions['i59'])
              self.inst_count +=1
      # geometry extruded check
        elif (self.inst_count == 60):  
            if self.progress['16'] == True:
                  self.step_label.config(text = ts.instructions['i60'])
                  self.inst_count += 1
            else:
                  self.errorPop("Extrude the geometry to continue")
        elif (self.inst_count == 61):
              self.root.title("Inset Face")  
              self.step_label.config(text = ts.instructions['i61'])
              self.inst_count +=1
        elif (self.inst_count == 62):  
              self.step_label.config(text = ts.instructions['i62'])
              self.inst_count +=1
      #face inset check
        elif (self.inst_count == 63):  
            if self.progress['17'] == True:
                  self.step_label.config(text = ts.instructions['i63'])
                  self.inst_count += 1
            else:
                  self.errorPop("Inset the face to continue")
        elif (self.inst_count == 64):
              self.root.title("Loop Cut")  
              self.step_label.config(text = ts.instructions['i64'])
              self.inst_count +=1
        elif (self.inst_count == 65):  
              self.step_label.config(text = ts.instructions['i65'])
              self.inst_count +=1
      #loop cut check
        elif (self.inst_count == 66):  
            if self.progress['18'] == True:
                  self.step_label.config(text = ts.instructions['i66'])
                  self.inst_count += 1
            else:
                  self.errorPop("Loop cut to continue")
        elif (self.inst_count == 67):
              self.root.title("Bevel")  
              self.step_label.config(text = ts.instructions['i67'])
              self.inst_count +=1
        elif (self.inst_count == 68):  
              self.step_label.config(text = ts.instructions['i68'])
              self.inst_count +=1
        elif (self.inst_count == 69):  
              self.step_label.config(text = ts.instructions['i69'])
              self.inst_count +=1
      #cube beveled check
        elif (self.inst_count == 70):  
            if self.progress['19'] == True:
                  self.step_label.config(text = ts.instructions['i70'])
                  self.inst_count += 1
            else:
                  self.errorPop("Bevel the cube to continue")

    #function for error message
    def errorPop(self, message):
        self.root.title(" ")
        self.error_pop = Toplevel(self.root)
        self.error_pop.geometry("200x120")
        self.error_pop.config(bg ="red")
        self.error_label = Label(self.error_pop, text=message, bg="red", fg="white", wraplength=180, justify="center")
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
      
        # change to edit mode check
        if lastLine == "10_done": 
            self.progress['10'] = True

            #transformed vertices check working on it
        if lastLine == "11_done": 
            self.progress['11'] = True

            #change selection mode check
        if lastLine == "12_done": 
            self.progress['12'] = True

        # geometry edited check
        if lastLine == "13_done": 
            self.progress['13'] = True

        # geometry edited check
        if lastLine == "14_done": 
            self.progress['14'] = True

        #falloff set to sharp check
        if lastLine == "15_done": 
            self.progress['15'] = True

        # Check for geometry extruded
        if lastLine == "16_done": 
            self.progress['16'] = True

        # Check for face inset
        if lastLine == "17_done": 
            self.progress['17'] = True

        # Check for loop cut
        if lastLine == "18_done": 
            self.progress['18'] = True

        # Check for cube beveled
        if lastLine == "19_done": 
            self.progress['19'] = True

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
    BlenderTutorial("/Users/suchir/Downloads/SIP/Blender/Vivian/progress.txt")

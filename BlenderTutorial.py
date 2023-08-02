import tkinter as tk
from tkinter import messagebox
import TutorialProgressMonitor
import os

class BlenderTutorial:

    def __init__(self, filename) -> None:
        self.filename = filename

        self.root = tk.Tk()
        self.root.geometry("500x250+50+50")
        self.root.title("Blender Tutorial")
        self.root.attributes('-topmost', 1)

        self.step_label = tk.Label(self.root, text="Step 1: Please click the button to add Cube!", font=("Arial", 18))
        self.step_label.pack(padx=10, pady=10)

        self.file_event_handler = TutorialProgressMonitor.Tm(self, self.filename)
        self.file_event_handler.startObserving()

        self.root.protocol("WM_DELETE_WINDOW", self.onClosing)

        self.root.mainloop()

    def onProgressChange(self):
        #self.showMessage("Progress Changed!", "")
        # 1. read last line of file
        # 2. check if step 1 is finished
        # 3. change the label text
        lastLine = self.readProgress()
        if (lastLine == "1_done"):
            self.step_label.config(text="Step 2 Rotate the Cube!")

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



if __name__ == "__main__":
    BlenderTutorial("/users/vivian/Documents/blender/progress.txt")
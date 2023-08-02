import bpy

class BlenderStatusMonitor:
    
    def __init__(self, max_count, filename) -> None:
        self.counter = 0
        self.max_count = max_count
        self.filename = filename
        
        # initialize file
        open(self.filename, "w+").close() # This will clear file content
        
        self.startMonitor()
        
    def onTimeHandler(self):
        print("Timer Event")
        self.progress_file = open(self.filename, "a")
     
        # ........ check status
        
        self.counter += 1
        if (self.counter >= self.max_count):
            self.appendToFile("tutorial completed")
            self.progress_file.close()
            return None
        else:    
            self.appendToFile("Timer Event " + str(self.counter))
            self.progress_file.close()
            return 5.0
         
    def startMonitor(self):
        bpy.app.timers.register(self.onTimeHandler)
        
    def appendToFile(self, str):
        self.progress_file.write("\n")
        self.progress_file.write(str)
        
if __name__ == "__main__":
    BlenderStatusMonitor(10, "/users/vivian/Documents/blender/progress.txt") 
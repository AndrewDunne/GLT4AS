import bpy

class BlenderStatusMonitor:
    
    def __init__(self, max_count, filename) -> None:
        self.counter = 0
        self.max_count = max_count
        self.filename = filename
        
        self.progress = {
            '1': False,
            '2': False
        }
        
        # initialize file
        open(self.filename, "w+").close() # This will clear file content
        
        self.startMonitor()
        
    def onTimeHandler(self):
        print("Timer Event")
        self.progress_file = open(self.filename, "a")
     
        #check status
        step1_result = self.checkStep1()
        print("step1 result is: " + step1_result)
        
        step2_result = self.checkStep2()
        print("step1 result is: " + step2_result)
        
        
        self.counter += 1
        if (self.counter >= self.max_count):
            self.appendToFile("tutorial completed")
            self.progress_file.close()
            return None
        else:
            if (step1_result != ""): 
                self.appendToFile(step1_result)
            if (step2_result != ""): 
                self.appendToFile(step2_result)
                
            self.progress_file.close()
            return 3.0
         
    def startMonitor(self):
        bpy.app.timers.register(self.onTimeHandler)
        
    def appendToFile(self, str):
        self.progress_file.write("\n")
        self.progress_file.write(str)
    
    # status checks
    
    #adding a cube check
    def checkStep1(self):
        if self.progress['1'] == False:
            for item in bpy.data.objects:
                if item.name == 'Cube':
                    self.progress['1'] = True
                    return "1_done"
            return ""
        else:
            return ""
    
    #moving with G check
    def checkStep2(self):
        if self.progress['1'] == True and self.progress['2'] == False:
            print("false and tru checks work")
            if bpy.data.objects['Cube'].location.x != 0.0 or bpy.data.objects['Cube'].location.y != 0.0 or bpy.data.objects['Cube'].location.z != 0.0:
                self.progress['2'] = True
                return "2_done"
            return ""
        else:
            return ""
   
   #def setStepTrue(self):
       #for step in self.progress:
           #step = True
           #return step + "_done"
       
if __name__ == "__main__":
    BlenderStatusMonitor(10, "/users/vivian/Documents/blender/progress.txt") 

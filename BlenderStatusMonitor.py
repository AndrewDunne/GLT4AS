import bpy

class BlenderStatusMonitor:
    
    def __init__(self, max_count, filename) -> None:
        self.counter = 0
        self.max_count = max_count
        self.filename = filename
        
        self.progress = {
            '1': False,
            '2': False,
            '3': False,
            '4': False,
            '5': False,
            '6': False,
            '7': False
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
        print("step2 result is: " + step2_result)
        
        step3_result = self.checkStep3()
        print("step3 result is: " + step3_result)
        
        step4_result = self.checkStep4()
        print("step4 result is: " + step4_result)
        
        step5_result = self.checkStep5()
        print("step5 result is: " + step5_result)
        
        step6_result = self.checkStep6()
        print("step6 result is: " + step6_result)
        
        step7_result = self.checkStep7()
        print("step7 result is: " + step7_result)
        
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
            if (step3_result != ""): 
                self.appendToFile(step3_result)
            if (step4_result != ""): 
                self.appendToFile(step4_result)
            if (step5_result != ""): 
                self.appendToFile(step5_result)
            if (step6_result != ""): 
                self.appendToFile(step6_result)
            if (step7_result != ""): 
                self.appendToFile(step7_result)
                
            self.progress_file.close()
            return 2.0
         
    def startMonitor(self):
        bpy.app.timers.register(self.onTimeHandler)
        
    def appendToFile(self, str):
        self.progress_file.write("\n")
        self.progress_file.write(str)
    
    #object checks to simplify and shorten code    
    def findObj(self, name):
        for obj in bpy.data.objects:
            if obj.name == name:
                return obj
        return None 
    
    # status checks
    
    #adding a cube check
    def checkStep1(self):
        result = ''
        if self.progress['1'] == False:
            cube = self.findObj('Cube')
            if cube != None:
                self.progress['1'] = True
                result = "1_done"   
        return result
        
    #deleting a cube check    
    def checkStep2(self):
         result = ''
         if self.progress['1'] == True and self.progress['2'] == False:
              cube = self.findObj('Cube')
              if cube == None:
                  self.progress['2'] = True
                  result = "2_done"
         return result
    
    #circle vertices check
    def checkStep3(self):
        result = ''
        if self.progress['2'] == True and self.progress['3'] == False:
            circle = self.findObj('Circle')
            if circle != None:
                if len(circle.data.vertices.items()) == 6:
                    self.progress['3'] = True
                    result = "3_done"
        return result

    #moving with G check
    def checkStep4(self):
        result = ''
        if self.progress['3'] == True and self.progress['4'] == False:
            cube = self.findObj('Cube')
            if cube != None:
                if cube.location.x != 0.0 or cube.location.y != 0.0 or cube.location.z != 0.0:
                    self.progress['4'] = True
                    result = "4_done"
        return result
    
    #rotating check
    def checkStep5(self):
        result = ''
        if self.progress['4'] == True and self.progress['5'] == False:
            cube = self.findObj('Cube')
            if cube != None:
                if cube.rotation_euler.x != 0.0 or cube.rotation_euler.y != 0.0 or cube.rotation_euler.z != 0.0:
                    self.progress['5'] = True
                    result = "5_done"
        return result
        
    #scaling check
    def checkStep6(self):
        result = ''
        if self.progress['5'] == True and self.progress['6'] == False:
            cube = self.findObj('Cube')
            if cube != None:
                if cube.scale.x != 1.0 or cube.scale.y != 1.0 or cube.scale.z != 1.0:
                    self.progress['6'] = True
                    result = "6_done"
        return result
    
    #smooth sphere check
    def checkStep7(self):
        result = ''
        if self.progress['6'] == True and self.progress['7'] == False:
            sphere = self.findObj('Sphere')
            if sphere != None:
                if sphere.data.shade_smooth() == True:
                    self.progress['7'] = True
                    result = "7_done"
        return result
        
       
if __name__ == "__main__":
    BlenderStatusMonitor(1000, "/users/vivian/Documents/blender/progress.txt") 

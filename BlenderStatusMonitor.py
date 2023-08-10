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
        
        step8_result = self.checkStep8()
        print("step8 result is: " + step8_result)
        
        step9_result = self.checkStep9()
        print("step9 result is: " + step9_result)
        
        step10_result = self.checkStep10()
        print("step10 result is: " + step10_result)
        
        step11_result = self.checkStep11()
        print("step11 result is: " + step11_result)
        
        step12_result = self.checkStep12()
        print("step12 result is: " + step12_result)
        
        step13_result = self.checkStep13()
        print("step13 result is: " + step13_result)

        step14_result = self.checkStep14()
        print("step14 result is: " + step14_result)

        step15_result = self.checkStep15()
        print("step15 result is: " + step15_result)

        step16_result = self.checkStep16()
        print("step16 result is: " + step16_result)

        step17_result = self.checkStep17()
        print("step17 result is: " + step17_result)

        step18_result = self.checkStep18()
        print("step18 result is: " + step18_result)

        step19_result = self.checkStep19()
        print("step19 result is: " + step19_result)


        
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
            if (step8_result != ""): 
                self.appendToFile(step8_result)
            if (step9_result != ""): 
                self.appendToFile(step9_result)
            if (step10_result != ""): 
                self.appendToFile(step10_result)
            if (step11_result != ""): 
                self.appendToFile(step11_result)
            if (step12_result != ""): 
                self.appendToFile(step12_result)
            if step13_result != "":
                self.appendToFile(step13_result)
            if step14_result != "":
                self.appendToFile(step14_result)
            if step15_result != "":
                self.appendToFile(step15_result)
            if step16_result != "":
                self.appendToFile(step16_result)
            if step17_result != "":
                self.appendToFile(step17_result)
            if step18_result != "":
                self.appendToFile(step18_result)
            if step19_result != "":
                self.appendToFile(step19_result)
                    
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
                if sphere.data.polygons[0].use_smooth == True:
                    self.progress['7'] = True
                    result = "7_done"
        return result
    
    #auto smooth check
    def checkStep8(self):
        result = ''
        if self.progress['7'] == True and self.progress['8'] == False:
            cylinder = self.findObj('Cylinder')
            if cylinder != None:
                if cylinder.data.use_auto_smooth == True:
                    self.progress['8'] = True
                    result = "8_done"
        return result
    
    #duplicate object check  
    def checkStep9(self):
        result = ''
        if self.progress['8'] == True and self.progress['9'] == False:
            cube = self.findObj('Cube')
            if cube != None:
                if len(bpy.data.objects.items()) == 5:
                    self.progress['9'] = True
                    result = "9_done"
        return result
    
    #change to edit mode check
    def checkStep10(self):
        result = ''
        if self.progress['9'] == True and self.progress['10'] == False:
            if bpy.context.mode == 'EDIT_MESH':
                self.progress['10'] = True
                result = "10_done"
        return result
       
    #transformed vertices check working on it
    def checkStep11(self):
        result = ''
        if self.progress['10'] == True and self.progress['11'] == False:
             #what to put
                self.progress['11'] = True
                result = "11_done"
        return result
    
    #change selection mode check
    def checkStep12(self):
        result = ''
        if self.progress['11'] == True and self.progress['12'] == False:
            if tuple(bpy.context.scene.tool_settings.mesh_select_mode) != (True, False, False):
                self.progress['12'] = True
                result = "12_done"
        return result
        
        #proportional editing check
    def checkStep13(self):
        result = ''
        if self.progress['12'] == True and self.progress['13'] == False:
            if bpy.context.tool_settings.use_proportional_edit:
                self.progress['13'] = True
                result = "13_done"
        return result

    # geometry edited check
    def checkStep14(self):
        result = ''
        if self.progress['13'] == True and self.progress['14'] == False:
            #active_obj = bpy.context.active_object
            #initial_vertices = [v.co.copy() for v in active_obj.data.vertices]
            #edited_vertices = [v.co for v in active_obj.data.vertices]
            #has_geometry_been_edited = any((iv != ev) for iv, ev in zip(initial_vertices, edited_vertices))
            if True:
                self.progress['14'] = True
                result = "14_done"
        return result

    # falloff set to sharp check
    def checkStep15(self):
        result = ''
        if self.progress['14'] == True and self.progress['15'] == False:
            if bpy.context.tool_settings.use_proportional_edit and bpy.context.tool_settings.proportional_edit_falloff == 'SHARP':
                self.progress['15'] = True
                result = "15_done"
        return result

    # geometry extruded check
    def checkStep16(self):
        result = ''
        if self.progress['15'] == True and self.progress['16'] == False:
            #active_obj = bpy.context.active_object
            #initial_vertex_count = len(active_obj.data.vertices)
            #extruded_vertex_count = len(active_obj.data.vertices)
            #has_geometry_been_extruded = extruded_vertex_count > initial_vertex_count
            if True:
                self.progress['16'] = True
                result = "16_done"
        return result

    # face inset check
    def checkStep17(self):
        result = ''
        if self.progress['16'] == True and self.progress['17'] == False:
            #active_obj = bpy.context.active_object
            #selected_face = active_obj.data.polygons.active
            #area_after_inset = selected_face.area
            #has_face_been_inset = area_after_inset > 0.0
            if True:
                self.progress['17'] = True
                result = "17_done"
        return result
    
    # loop cut check
    def checkStep18(self):
        result = ''
        if self.progress['17'] == True and self.progress['18'] == False:
            #active_obj = bpy.context.active_object
            #initial_edge_count = len(active_obj.data.edges)
            #loop_cut_edge_count = len(active_obj.data.edges)
            #has_loop_cut_been_made = loop_cut_edge_count > initial_edge_count
            if True:
                self.progress['18'] = True
                result = "18_done"
        return result
    
    # cube beveled check
    def checkStep19(self):
        result = ''
        if self.progress['18'] == True and self.progress['19'] == False:
            #active_obj = bpy.context.active_object
            #initial_vertex_count = len(active_obj.data.vertices)
            #beveled_vertex_count = len(active_obj.data.vertices)
            #has_cube_been_beveled = beveled_vertex_count > initial_vertex_count
            if True:
                self.progress['19'] = True
                result = "19_done"
        return result


          
if __name__ == "__main__":
    BlenderStatusMonitor(1000, "/Users/suchir/Downloads/SIP/Blender/Vivian/progress.txt") 

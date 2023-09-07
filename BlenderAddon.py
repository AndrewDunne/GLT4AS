import bpy
from . TutorialStrings import constants
from . BlenderStatusMonitor import BlenderStatusMonitor

#creates the UI panel
class TutorialPanel(bpy.types.Panel):
    
    bl_label = "Blender Tutorial"
    bl_idname = "Blender_Tutorial"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tutorial"
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        scene = context.scene
        myprop = scene.my_prop
        row.label(text = "Enter Desired Time")
        layout.prop(myprop, "time")
        
        row = layout.row()
        row.label(text = "Enter File Location")
        layout.prop(myprop, "file_location")
        
        row = layout.row()
        row.operator("object.blender_execute", text="Start Tutorial")


#class for properties
class MyProperties(bpy.types.PropertyGroup):
    
    file_location: bpy.props.StringProperty(name = "", default = constants['default_file'])
    
    time: bpy.props.IntProperty(name = "", default=20, soft_min = 20, soft_max = 45)
    
    
#class to execute blenderstatusmoniter    
class BlenderExecute(bpy.types.Operator):
    
    bl_idname = "object.blender_execute"
    bl_label = "Blender Execute"
    
    def execute(self, context):
        self.report({'INFO'}, "Button clicked!, class run") 
         
        scene = context.scene
        myprop = scene.my_prop
        
        #pulling data from panel
        file =  myprop.file_location
        min = myprop.time
        
        # convert min to number of intervals
        seconds = min * 60
        intervals = seconds // 2
        
        BlenderStatusMonitor(intervals, file)
        self.report({'INFO'}, "intervals: " + str(intervals) + " location is: " + file) 
        return {'FINISHED'}

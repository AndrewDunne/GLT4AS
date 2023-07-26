import bpy

class dialogBox1(bpy.types.Operator):
    bl_label = "Tutorial"
    bl_idname = "dialog.box1"

    def execute(self, context):
        bpy.ops.dialog.box2('INVOKE_DEFAULT')
        return {'FINISHED'}

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Welcome to Blender!", icon = "BLENDER", icon_value = 9)
        row = layout.row()
        row.label(text="Click OK to begin your tutorial, or hit 'esc' to exit.")


    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

class dialogBox1b(bpy.types.Operator):
    bl_label = "Tutorial"
    bl_idname = "dialog.box1b"

    def execute(self, context):
        return {'FINISHED'}

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Welcome to Blender!", icon = "BLENDER", icon_value = 9)
        row = layout.row()
        row.label(text="Click OK to begin your tutorial, or hit 'esc' to exit.")


    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    
class dialogBox2(bpy.types.Operator):
    bl_label = "Tutorial"
    bl_idname = "dialog.box2"

    def execute(self, context):
        bpy.ops.dialog.box3('INVOKE_DEFAULT')
        return {'FINISHED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Select an Object", icon = "BLENDER")
        row = layout.row()
        row.label(text="Click on the object to select it.")
        row = layout.row()
        row.label(text="You can also click the object from the menu on the top right to select it.")
        row = layout.row()
        row.label(text="Click outside the object to deselect it.")
        row = layout.row()
        row.operator("dialog.box1b", text = "Previous")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width = 400)
    
class dialogBox2b(bpy.types.Operator):
    bl_label = "Tutorial"
    bl_idname = "dialog.box2b"

    def execute(self, context):
        return {'FINISHED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Select an Object", icon = "BLENDER")
        row = layout.row()
        row.label(text="Click on the object to select it.")
        row = layout.row()
        row.label(text="You can also click the object from the menu on the top right to select it.")
        row = layout.row()
        row.label(text="Click outside the object to deselect it.")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width = 400)
    
class dialogBox3(bpy.types.Operator):
    bl_label = "Tutorial"
    bl_idname = "dialog.box3"

    def execute(self, context):
        bpy.ops.dialog.box4('INVOKE_DEFAULT')
        return {'FINISHED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Move the Object", icon = "BLENDER")
        row = layout.row()
        row.label(text="Click on the object, then click 'G' to move it.")
        row = layout.row()
        row.operator("dialog.box2b", text = "Previous")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    
class dialogBox3b(bpy.types.Operator):
    bl_label = "Tutorial"
    bl_idname = "dialog.box3b"

    def execute(self, context):
        return {'FINISHED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Move the Object", icon = "BLENDER")
        row = layout.row()
        row.label(text="Click on the object, then click 'G' to move it.")


    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    
class dialogBox4(bpy.types.Operator):
    bl_label = "Tutorial"
    bl_idname = "dialog.box4"

    def execute(self, context):
        bpy.ops.dialog.box5('INVOKE_DEFAULT')
        return {'FINISHED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Rotate the Object", icon = "BLENDER")
        row = layout.row()
        row.label(text="Click on the object, then click 'R' to rotate it.")
        row = layout.row()
        row.operator("dialog.box3b", text = "Previous")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

class dialogBox4b(bpy.types.Operator):
    bl_label = "Tutorial"
    bl_idname = "dialog.box4b"

    def execute(self, context):
        return {'FINISHED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Rotate the Object", icon = "BLENDER")
        row = layout.row()
        row.label(text="Click on the object, then click 'R' to rotate it.")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    
class dialogBox5(bpy.types.Operator):
    bl_label = "Tutorial"
    bl_idname = "dialog.box5"

    def execute(self, context):
        bpy.ops.dialog.box6('INVOKE_DEFAULT')
        return {'FINISHED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Scale the Object", icon = "BLENDER")
        row = layout.row()
        row.label(text="Click on the object, then click 'S' to scale it.")
        row = layout.row()
        row.operator("dialog.box4b", text = "Previous")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

class dialogBox5b(bpy.types.Operator):
    bl_label = "Tutorial"
    bl_idname = "dialog.box5b"

    def execute(self, context):
        return {'FINISHED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Scale the Object", icon = "BLENDER")
        row = layout.row()
        row.label(text="Click on the object, then click 'S' to scale it.")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    
class dialogBox6(bpy.types.Operator):
    bl_label = "Tutorial"
    bl_idname = "dialog.box6"

    def execute(self, context):
        bpy.ops.dialog.box7('INVOKE_DEFAULT')
        return {'FINISHED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Transform the Object", icon = "BLENDER")
        row = layout.row()
        row.label(text="Click on the object, then click 'T' to transform it.")
        row = layout.row()
        row.operator("dialog.box5b", text = "Previous")
        row = layout.row()
        row.operator("dialog.box6c", text = "Learn more")
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    
class dialogBox6b(bpy.types.Operator):
    bl_label = "Tutorial"
    bl_idname = "dialog.box6b"

    def execute(self, context):
        return {'FINISHED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Transform the Object", icon = "BLENDER")
        row = layout.row()
        row.label(text="Click on the object, then click 'T' to transform it.")
        row = layout.row()
        row.operator("dialog.box6c", text = "Learn more")
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)


class dialogBox6c(bpy.types.Operator):
    bl_label = "Tutorial"
    bl_idname = "dialog.box6c"

    def execute(self, context):
        return {'FINISHED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Transform the Object", icon = "BLENDER")
        row = layout.row()
        row.label(text="Transform allows for the object to be moved, rotated, and scaled at the same time.")

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width = 450)
    
class dialogBox7(bpy.types.Operator):
    bl_label = "Tutorial"
    bl_idname = "dialog.box7"

    def execute(self, context):
        bpy.ops.dialog.box8('INVOKE_DEFAULT')
        return {'FINISHED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Add Button", icon = "BLENDER")
        row = layout.row()
        row.label(text="In the menu bar at the top, you can add new objects.")
        row = layout.row()
        row.label(text="Try adding a sphere. Add > Mesh > UV Sphere")
        row = layout.row()
        row.operator("dialog.box6b", text = "Previous")
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
    
class dialogBox7b(bpy.types.Operator):
    bl_label = "Tutorial"
    bl_idname = "dialog.box7b"

    def execute(self, context):
        return {'FINISHED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Add Button", icon = "BLENDER")
        row = layout.row()
        row.label(text="In the menu bar at the top, you can add new objects.")
        row = layout.row()
        row.label(text="Try adding a sphere. Add > Mesh > UV Sphere")
        row = layout.row()
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

class dialogBox8(bpy.types.Operator):
    bl_label = "Tutorial"
    bl_idname = "dialog.box8"

    def execute(self, context):
        if context.active_object.mode != 'EDIT':
            bpy.ops.dialog.box8c('INVOKE_DEFAULT')
            bpy.ops.dialog.box8('INVOKE_DEFAULT')
        #bpy.ops.dialog.box9('INVOKE_DEFAULT')
        return {'FINISHED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Changing Modes", icon = "BLENDER")
        row = layout.row()
        row.label(text="Click the droptown labeled 'Object Mode' to see a list of modes.")
        row = layout.row()
        row.label(text="Switch to Edit Mode.")
        row = layout.row()
        row.operator("dialog.box7b", text = "Previous")
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width = 400)
    
class dialogBox8b(bpy.types.Operator):
    bl_label = "Tutorial"
    bl_idname = "dialog.box8b"

    def execute(self, context):
        return {'FINISHED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Changing Modes", icon = "BLENDER")
        row = layout.row()
        row.label(text="Click the droptown labeled 'Object Mode' to see a list of modes.")
        row = layout.row()
        row.label(text="Switch to Edit Mode.")
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width = 400)

class dialogBox8c(bpy.types.Operator):
    bl_label = "Tutorial"
    bl_idname = "dialog.box8c"

    def execute(self, context):
        return {'FINISHED'}
    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Changing Modes", icon = "BLENDER")
        row = layout.row()
        row.label(text="CMake sure you have switched to edit mode.")
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

def register():
    bpy.utils.register_class(dialogBox1)
    bpy.utils.register_class(dialogBox1b)
    bpy.utils.register_class(dialogBox2)
    bpy.utils.register_class(dialogBox2b)
    bpy.utils.register_class(dialogBox3)
    bpy.utils.register_class(dialogBox3b)
    bpy.utils.register_class(dialogBox4)
    bpy.utils.register_class(dialogBox4b)
    bpy.utils.register_class(dialogBox5)
    bpy.utils.register_class(dialogBox5b)
    bpy.utils.register_class(dialogBox6)
    bpy.utils.register_class(dialogBox6b)
    bpy.utils.register_class(dialogBox6c)
    bpy.utils.register_class(dialogBox7)
    bpy.utils.register_class(dialogBox7b)
    bpy.utils.register_class(dialogBox8)
    bpy.utils.register_class(dialogBox8b)
    bpy.utils.register_class(dialogBox8c)

def unregister():
    bpy.utils.unregister_class(dialogBox1)
    bpy.utils.unregister_class(dialogBox1b)
    bpy.utils.unregister_class(dialogBox2)
    bpy.utils.unregister_class(dialogBox2b)
    bpy.utils.unregister_class(dialogBox3)
    bpy.utils.unregister_class(dialogBox3b)
    bpy.utils.unregister_class(dialogBox4)
    bpy.utils.unregister_class(dialogBox4b)
    bpy.utils.unregister_class(dialogBox5)
    bpy.utils.unregister_class(dialogBox5c)
    bpy.utils.unregister_class(dialogBox6)
    bpy.utils.unregister_class(dialogBox6b)
    bpy.utils.unregister_class(dialogBox6c)
    bpy.utils.unregister_class(dialogBox7)
    bpy.utils.unregister_class(dialogBox7b)
    bpy.utils.unregister_class(dialogBox8)
    bpy.utils.unregister_class(dialogBox8b)
    bpy.utils.unregister_class(dialogBox8c)
    
    

if __name__ == "__main__":
    register()
    bpy.ops.dialog.box1('INVOKE_DEFAULT')
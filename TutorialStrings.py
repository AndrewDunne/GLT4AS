steps = {
    1: ""
}

instructions = {
    'i1': "Welcome to Blender! Blender is a 3D modeling software, which means you can use it to create 3D objects, simulate 3D scenes, make art, etc. In this tutorial, you’ll learn the basics of controlling the software and how to make your own simple objects!",
    'i2':"To start, let’s explain what’s on screen. The main window is called the 3D viewport. This is where you see the 3D scene, and all of the objects inside of it. You start with a cube, light, and camera but for this tutorial, the cube will not be present yet ",
    'i3':"To move through the tutorial, press ‘Continue’. Sometimes, you will have to perform an action in order to move onto the next step",
    'i4':"How do you navigate this 3D scene? This tutorial will assume you are using a computer mouse with a mouse wheel. To orbit the camera, hold down the middle mouse button and move the mouse around, or left click and drag the gizmo in the top right of the viewport.",
    'i5':"To zoom the camera, scroll up or down on the mouse wheel, or left click and drag the magnifying glass icon in the top right.",
    'i6':"To move the camera, hold down shift and the middle mouse button and move the mouse, or left click and drag the hand icon in the top right. These are the three basic ways to look around!" ,
    'i7':"If you want to look into the scene from a specific direction, such as from the top or bottom, you can click the red, green, or blue circles in the 3D gizmo. X and -X show left and right views, Y and -Y show front and back views, and Z and -Z show top and bottom views",
    'i8': "Next Up: Adding objects",
    'i9':"Let’s learn how to add objects to the scene. There are a number of different types of objects in Blender. For now let’s focus on meshes, which are the most common kind of object.",
    'i10':"To add a mesh into the scene, click ‘add’ button at the top of the 3D viewport. From here, find the object that you want to add - let’s add a cube, which is under the ‘Mesh’ category. You can also press Shift+A on the keyboard to bring up this menu quickly.",
    #add cube check
    'i11':"Good Job on adding your first object!",
    'i12': "Moving on to Deleting Objects and Undo/Redo",
    'i13':"There’s an object sitting in the scene that you don’t want any more - to delete it, select it, click 'x' on your keyboard, and press delete. Try removing the cube in the scene right now",
    #delete cube check
    'i14':"Cube deleted. Simple as that!",
    'i15':"Just in case, if you’ve undone an action that you actually didn’t want to undo, you can ‘redo’ it by pressing Shift+Ctrl+Z. (CMD + Z on mac)",
    'i16':"Moving onto new object settings!",
    'i17':"Whenever you add a new object to the scene, Blender gives you some options that you can change. Add a circle to the scene and when the ‘add circle’ pop-up appears in the bottom left, click it to expand the options.",
    'i18':"By lowering the amount of vertices, you can make a polygon like a triangle or square, increase the radius of the circle, and fill the circle in! Give the circle 6 vertices to make a hexagon, and set the fill type to ‘N-Gon’ to fill it in.",
    #vertices on circle check
    'i19':"You made a hexagon! Good Job!",
    'i20':"The next lesson will teach you about the 3 most basic actions you can perform which are moving, rotating, and scaling.",
    'i21':"Clear the scene and add a cube. Select it and press the G key. G stands for grab! Move the mouse around until you’re satisfied with where the cube is, and then left click or press the enter key to place it down. You can move on a specific axis by pressing G and then x, y, or z. Try it!",
    #move cube check
    'i22':"Good job moving the cube!",
    'i23':"To rotate the cube, press R while selecting it. The same rules apply for rotating; move the mouse cursor to spin the cube, and then left click/enter to confirm the rotation. You can also rotate on a specific axis by pressing R and then x, y, or z. ",
    #rotate cube check
    'i24':"Good job rotating the cube!",
    'i25':"Finally, to scale the cube, press S. The same rules apply",
    #scale cube check
    'i26':"Good job on scaling! You just learned the 3 basic actions for objects!",
    'i27': "Sometimes while performing an action, such as moving an object, you decide that you don’t want to do it. In order to cancel your current action, press the ‘Esc’ key! Try it out",
    'i28': "After you move, rotate, or scale an object, those transformations can be seen in a panel on the right of the viewport. This panel be used to manually set location, rotation, and scale to more exact values. Press N on your keyboard to open the panel. Experiment with it a little!",
    'i29':"Now lets learn about Selecting Objects",
    #ask user to add cone
    'i30':"Clear the scene and add a cone (under meshes). Left click to select it. You’ll see it become highlighted in orange when selected, and left clicking anywhere else in the viewport will deselect it and remove the highlight",
    #ask user to add 2 cones to scene
    'i31':"Add 2 more cones! You can select multiple objects at once by left clicking and dragging in the viewport to box-select, or you can select one object and then shift-left click the other objects to add them to your selection. Try selecting all 3 cones in the scene.",
    'i32':"When you have multiple objects selected, you can perform actions on all of them at once! Try deleting all the cones at the same time!",
    'i33': "Nice! Now lets move on to flat and smooth shading",
    'i34': "Add a UV-Sphere. You might have noticed that it looks like a golf ball - they have many small, square faces. If you want the sphere to appear smooth, select the sphere and right click to bring up a menu. Then, select the top option: “Shade Smooth”",
    #shade smooth check
    'i35': "Good Job Now it looks more like a bouncy ball!",
    'i36': "Smooth shading looks nice on objects that should be smooth, but on angular things like cubes it doesn’t look right - the default ‘flat’ shading looks better. However, some objects like cylinders have some flat parts and some smooth parts. To account for this, there is another option - auto smooth shading.",
    'i37': "Remove the sphere and add a cylinder. Select and right click it, and then select the “Shade Auto Smooth” option.",
    #check shade auto smooth
    'i38': "Good job! Now you know how to change the shading of meshes!",
    'i39': "Now lets move on to duplicating objects!",
    'i40': "While in most programs you use the hotkeys Ctrl+C and Ctrl+V in order to duplicate things, in Blender there is a single hotkey instead: Shift+D (option + D on mac). This duplicates any selected objects!",
    'i41': "Try using Shift+D to duplicate the chair in the scene, and then place it down wherever you like.",
    #check duplicate object
    'i42':"Nice!",
    #i want to clear the scene but how?
    'i43':"So far you have made objects and manipulated them, but now it’s time to start modeling your meshes. To do so, you must enter ‘Edit Mode’ on an object.The 3D viewport has a few different modes, and so far you’ve only been using ‘Object Mode’",
    'i44': "To switch modes: select the cube in the scene, and then click on the label that says ‘Object Mode’ in the top left of the viewport. This will bring down a list of modes that you can switch to. Switch to Edit Mode.",
    #check switch mode
    'i45': "Perfect! Now that you're in Edit Mode, you’ll be learning more about how to make things with it.",
    'i46': "You’ll notice there are circles on the corners of the cube - these are vertices. The lines that go between them are edges, and the surfaces that connect the edges are faces. You can only perform actions on meshes’ vertices, edges, and faces in Edit Mode",
    'i47': "Just like how you can select and transform objects, you can use the same hotkeys to select and transform vertices, edges, and faces. Try selecting some of the vertices, and then moving, rotating, or scaling them.",
    #check for transformed vertices
    'i48': "Good Job! Looks strange doesn't it?",
    'i49': "In order to manipulate edges or faces instead of vertices, you can change the selection mode. In the top right of the viewport next to ‘Edit Mode’ you’ll see three cube-shaped icons. They represent vertices, edges, and faces respectively. Click them to enter edge or face select modes, or press ‘1’, ‘2’, or ‘3’ on your keyboard.",
    #check that selection mode changed
    'i50': "Yay! You just learned how to manipulate vertices, edges, and faces of objects in Edit Mode",
    'i51': "",
    'i52': "",
    'i53': "",
    'i54': "",
    'i55': "",
    'i56': "",
    'i57': "",
    'i58': "",
    'i59': "",
}

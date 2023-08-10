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
    'i23':"To rotate the cube, press R while selecting it. The same rules apply for rotating; move the mouse cursor to spin the cube, and then left click/enter to confirm the rotation.",
    #rotate cube check
    'i24':"Good job rotating the cube!",
    'i25':"Finally, to scale the cube, press S.",
    #scale cube check
    'i26':"Good job on scaling! You just learned the 3 basic actions for objects!",
    'i27': "Sometimes while performing an action, such as moving an object, you decide that you don’t want to do it. In order to cancel your current action, press the ‘Esc’ key! Try it out",
    'i28':"Now lets learn about Selecting Objects",
    #ask user to add cone
    'i29':"Clear the scene and add a cone (under meshes). Left click to select it. You’ll see it become highlighted in orange when selected, and left clicking anywhere else in the viewport will deselect it and remove the highlight",
    #ask user to add 2 cones to scene
    'i30':"Add 2 more cones! You can select multiple objects at once by left clicking and dragging in the viewport to box-select, or you can select one object and then shift-left click the other objects to add them to your selection. Try selecting all 3 cones in the scene.",
    'i31':"When you have multiple objects selected, you can perform actions on all of them at once! Try deleting all the cones at the same time!",
    'i32': "Nice! Now lets move on to flat and smooth shading",
    'i33': "Add a UV-Sphere. You might have noticed that it looks like a golf ball - they have many small, square faces. If you want the sphere to appear smooth, select the sphere and right click to bring up a menu. Then, select the top option: “Shade Smooth”",
    #shade smooth check
    'i34': "Good Job Now it looks more like a bouncy ball!",
    'i35': "Smooth shading looks nice on objects that should be smooth, but on angular things like cubes it doesn’t look right - the default ‘flat’ shading looks better. However, some objects like cylinders have some flat parts and some smooth parts. To account for this, there is another option - auto smooth shading.",
    'i36': "Remove the sphere and add a cylinder. Select and right click it, and then select the “Shade Auto Smooth” option.",
    #check shade auto smooth
    'i37': "Good job! Now you know how to change the shading of meshes!",
    'i38': "Now lets move on to duplicating objects!",
    'i39': "While in most programs you use the hotkeys Ctrl+C and Ctrl+V in order to duplicate things, in Blender there is a single hotkey instead: Shift+D. This duplicates any selected objects!",
    'i40': "Try using Shift+D to duplicate the chair in the scene, and then place it down wherever you like.",
    #check duplicate object
    'i41':"Nice!",
    'i42': "So far you have made objects and manipulated them a bit, but now it’s time to actually start modeling your own meshes. To do so, you need to enter ‘Edit Mode’ on an object.The 3D viewport has a few different modes, and so far you’ve been only using ‘Object Mode’ which lets you select different objects.",
    #check edit mode
    'i43': "To switch modes: select the cube in the scene, and then click on the label that says ‘Object Mode’ in the top left of the viewport. This will bring down a list of modes that you can switch to to modify the object you have selected in different ways. Try switching to different modes!",
    'i44': "In the following lessons, you’ll learn more about edit mode and how to make things with it.",
    'i45': "You’ll notice there are circles on the corners of the cube - these are vertices. The lines that go between them are edges, and the surfaces that connect the edges are faces. You can only perform actions on meshes’ vertices, edges, and faces in Edit Mode",
    'i46': "Just like how you can select and transform objects, you can use the same hotkeys to select and transform vertices, edges, and faces. Try entering edit mode on the cube, selecting some of the vertices, and then moving, rotating, or scaling them somehow.",
    #cube edited check
    'i47': "In order to select and manipulate edges or faces instead of vertices, you can change the selection mode. In the top right of the viewport next to ‘Edit Mode’ you’ll see three cube-shaped icons, with the left one highlighted blue. Click the others to enter edge or face select modes, or press ‘1’, ‘2’, or ‘3’ on your keyboard to switch between modes faster.",
    #selection mode check
    'i48': "One way to select a section of vertices, edges, or faces on your mesh is called loop selection; often there will be ‘loops’ of vertices/edges/faces all in a row, connected by what is called an edge loop. For example, the ring of edges that go around a sphere vertically or horizontally are edge loops.",
    'i49': "If you want to select an edge loop all at once, hold down the ‘Alt’ key and left click on an edge! Try selecting an edge loop on the sphere and scale it with S.",
    'i50': "On meshes with many vertices, edges, and faces (collectively called ‘geometry’), it can be tiresome to select exactly the ones you want to manipulate, and it can also be difficult to edit in a way that feels more organic, which you might want if you’re modeling something like an apple.",
    'i51': "To solve these problems, there exists a tool in edit mode called ‘Proportional Editing’! Proportional editing makes changes to the geometry you’re selecting also apply (but less strongly) to nearby geometry.",
    'i52': "To turn on proportional editing, find the icon on the top of the 3D viewport that looks like a dot with a circle around it and click it.",
    #proportional editing check
    'i53': "Now, select some geometry and try editing it!",
    #geometry edited check
    'i54': "You may notice that a circle appears now when you are performing transformations - this represents the radius of the proportional editing, basically how big the effect is. You can make the radius larger or smaller by scrolling the mouse wheel while performing the transformation. Try it out!",
    'i55': "With the default settings for proportional editing, grabbing a vertex and moving it around drags a sort of blob-shaped section of geometry with it - this often works, but sometimes you want to edit the geometry in different ways, such as stretching out the geometry like it’s a balloon.",
    'i56': "To change the shape of the proportional editing, click the dark bump icon to the right of the proportional editing icon to change its ‘falloff curve’. It’s using the ‘smooth’ curve by default, but the ‘sharp’ curve provides a nice contrast! Try out the sharp falloff setting.",
    #fall off sharp check
    'i57': "Using different falloff curves lets you model new things and get unique artistic effects.",
    'i58': "Edit mode also gives you many new tools for adding geometry to a mesh. One of the simplest and most useful is the ‘Extrude’ tool.",
    'i59': "This can be found on the left-hand toolbar, or you can quickly extrude by pressing the E key after selecting geometry. See what happens when you extrude vertices, edges, and faces!",
    #geometry extruded check
    'i60': "Extrude is good for branching out new geometry from your mesh, for example making legs for a table or giving a person’s hand fingers.",
    'i61': "Edit mode’s ‘Inset Face’ tool is a great partner to the extrude tool.",
    'i62': "With a face selected, find the inset face icon in the left toolbar, or press the i key to begin the action. A smaller face will appear inside the selected one, and you can move your cursor to change its size. Try using i to inset a face on the cube!",
    #face inset check
    'i63': "This is great to use with extrude, because adding the extra geometry gives you new faces to extrude from. For example, extruding up the center from the top face of a cube could give you the stem for a (very blocky) apple!",
    'i64': "One of the most useful tools in edit mode doesn’t even change the shape of the mesh you’re modeling - meet the ‘loop cut’. The loop cut tool adds a loop of edges around a mesh, giving you the geometry you need to add finer details!",
    'i65': "To start a loop cut, find its icon on the left toolbar or use the hotkey Ctrl+R, then move your cursor over the mesh until you see a yellow shape wrap around the mesh. Left click to confirm the loop, and then slide the loop around with your mouse until you’re happy with its position, and then click again to place the loop. Try making a loop cut around the cylinder.",
    #loop cut check
    'i66': "By making the loop cut, you’re now able to independently edit the top and bottom walls of the cylinder! If you ever need more geometry to add details, loop cut is your friend.",
    'i67': "If you want to add a bit of style to your meshes’ edges, the bevel tool is for you.",
    'i68': "Select one or more edges in edit mode, then click the bevel icon in the toolbar, or use the hotkey Ctrl+B. The bevel tool will split the selected edges into faces, making the transition between larger faces less hard.",
    'i69': "Try bevelling the cube with Ctrl+B, and then see what settings are available after once the bevel menu appears. There are some interesting options!",
    #Cube beveled
    'i70': "Tutorial Complete"
}
# O.P.E.
Object Placement Exporter, from Blender to UE4. A fork of TSTools by Tom Shannon.

## Purpose of this plugin.
There currently exists multiple plugins with the function of exporting objects from Blender to Unreal Engine 4. However, when you thereafter want to add them into the scene, you will have to manually place each object and/or write in the different translation information to the object in UE4. With O.P.E., one can now simply produce a script that will create placeholder boxes in the UE4 scene that you can then replace with the objects you want. It will work with the base scale in Blender, and all from the transform, rotation, scale and origin will all be included.

### Instructions and result.
1) Select the objects you want to export the transform, scale and rotation information to UE4.
2) Click the panel menu to then find the "O.P.E.".
3) With the selected objects, click the "Create info from selected".
4) The information is now directly copied to your clipboard. As such you can now simply go to UE4 and paste the information in the workplace.

5) [END RESULT] Placeholder boxes should now appear on the scene, which you can then change the object to the one you wish.

### Notes
- This code is based on Tom Shannon's TSTools, where it produces a clipboard script which can thus be used in UE4. In essence, it is simply reformatted to work with Blender, so all credit goes to Tom Shannon for the original code.
- This is my first Python project, so there’s bound to be many obvious areas where the setup of this repository and the code itself that can be vastly improved. If you spot any issues, please do tell so I can improve.

# O.P.E.
Object Placement Exporter, from Blender to UE4. A fork of TSTools by Tom Shannon.

## Purpose of this plugin.
While there exists different plugins with the purpose of exporting different objects and assets into UE4 Editor, there is a lack of practical methods of importing every asset from an already laid out Blender scene with it's transform, scale and rotation information into UE4. This plugin is hopefully an functional method of solving this, where it produces placeholder boxes with the information which you can thus switch out the the objects you wish.

### Instructions and result.
1) Select the objects you want to export the transform, scale and rotation information to UE4.
2) Click the panel menu to then find the "O.P.E.".
3) With the selected objects, click the "Create info from selected".
4) The information is now directly copied to your clipboard. As such you can now simply go to UE4 and paste the information in the workplace.

Result) Placeholder boxes should now appear on the scene, where you can then change the object to the one you wish.

### Notes
- This code is based on Tom Shannon's TSTools, where it produces a clipboard script which can thus be used in UE4. In essence, it is simply reformatted to work with Blender, so all credit goes to Tom Shannon for the original code.
- This is my first Python project ever, so there is bound to be a lot of areas in both how this repository is setup and the code itself that can be vastly improved. As such, if you spot any issues, please do tell so I can imporve. ;)

bl_info = {
    "name": "O.P.E. (Object Placement Exporter)",
    "author": "Restalot",
    "version": (0, 2),
    "blender": (2, 83, 2),
    "location": "View3D > Panel > OPE",
    "description": "Adds placement information to your clipboard.\n Works only for UE4 Editor.",
    "warning": "",
    "wiki_url": "",
    "category": "Creates Text Script.",
}


import bpy


class OPE_PT_main_panel(bpy.types.Panel):
    
    bl_label = "O.P.E (Object Placement Exporter)"
    bl_idname = "OPE_main_panel"
    
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'O.P.E.'

    def draw(self, context):
        layout = self.layout

        layout.operator("ope.addbasic_operator")



class OPE_OT_add_basic(bpy.types.Operator):
    bl_label = "Create info from selected"
    bl_idname = "ope.addbasic_operator"


    def execute(self, context):
           
        export_info = ""

        for obj in bpy.context.selected_objects:
                
            x_location = float(obj.location.x) * 100
            x_location = str(x_location)
            y_location = float(obj.location.y) * 100
            y_location = str(y_location)
            z_location = float(obj.location.z) * 100
            z_location = str(z_location)
                
            pitch = (float(obj.rotation_euler[1]) * 100) / 1.745329
            pitch = str(pitch)
            yaw = (float(obj.rotation_euler[0]) * 100) / 1.745329
            yaw = str(yaw)
            roll = (float(obj.rotation_euler[2]) * 100) / 1.745329
            roll = str(roll)


            export_info +=  "      Begin Actor Class=StaticMeshActor Name=" + obj.name + \
                            " Archetype=StaticMeshActor'/Script/Engine.Default__StaticMeshActor'\n̈́" \
                            "         Begin Object Class=StaticMeshComponent Name=StaticMeshComponent0 " \
                            "ObjName=StaticMeshComponent0 Archetype=StaticMeshComponent " \
                            "'/Script/Engine.Default__StaticMeshActor:StaticMeshComponent0'\n" \
                            "         End Object\n" \
                            "         Begin Object Name=StaticMeshComponent0\n" \
                            "            StaticMesh=StaticMesh'/Engine/EditorMeshes/EditorCube.EditorCube'\n" \
                            "            RelativeLocation=(X=" + x_location + ", Y=" + y_location + \
                            ", Z=" + z_location + ")\n" \
                            "            RelativeScale3D=(X=1, Y=1, Z=1)\n" \
                            "            RelativeRotation=(Pitch=" + pitch + ", Yaw=" + yaw + ", Roll=" + roll + ")\n" \
                            "         End Object\n" \
                            "         StaticMeshComponent=StaticMeshComponent0\n" \
                            "         Components(0)=StaticMeshComponent0\n" \
                            "         RootComponent=StaticMeshComponent0\n" \
                            '         ActorLabel="' + obj.name + '"\n' \
                            "      End Actor\n"



        intro_script = f"Begin Map\n" \
                           f"   Begin Level\n"

        main_script = ""

        ending_script = "   End Level\n" \
                            "Begin surface\n" \
                            "End Surface\n" \
                            "End Map"

        main_script += intro_script
        main_script += export_info
        main_script += ending_script

        
        bpy.context.window_manager.clipboard = main_script
        
        return {'FINISHED'}



classes = [OPE_PT_main_panel, OPE_OT_add_basic]
 
 
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
 
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
 
 
 
if __name__ == "__main__":
    register()
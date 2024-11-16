
import bpy

class ToolsPanel:
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "PoseTools"


class POSETOOL_UL_poseset_item(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            row = layout.row(align=True)
            if item.target:
                row.prop(item.target, "name", text="", emboss=False)
        elif self.layout_type == 'GRID':
            layout.alignment = 'CENTER'
            layout.label(text="", icon_value=icon)

class POSETOOL_UL_pose_item(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            row = layout.row(align=True)
            row.prop(item, "name", text="", emboss=False)
            row.prop(item, "rate", text="",slider=True)
                
        elif self.layout_type == 'GRID':
            layout.alignment = 'CENTER'
            layout.label(text="", icon_value=icon)
    
class POSETOOL_PT_pose_utils(ToolsPanel,bpy.types.Panel):
    bl_idname="POSETOOL_PT_pose_utils"
    bl_label = "Pose Tools"

    def __init__(self):
        pass

    @classmethod
    def poll(cls, context):
        return True
    
    def draw_target(self,target,layout):
        row = layout.row()
        row.prop(target, "name", text="Name")
        
        poseList = target.blend_pose

        row = layout.row()
        col = row.column()
        col.template_list("POSETOOL_UL_pose_item", "", poseList,
                          "pose_list", poseList, "active_index", rows=4)
        col = row.column()
        sub = col.column(align=True)
        sub.operator("object.pose_util_pose_add", icon="ADD", text="")
        sub.operator("object.pose_util_pose_remove", icon="REMOVE", text="")
        if len(poseList.pose_list) > 0:
            current = poseList.pose_list[poseList.active_index]
            header , subPanel = layout.panel("blend_pose_panel", default_closed=False)
            header.label(text="Pose")
            row=subPanel.row()
            row.prop(current, "name", text="Name")
            row=subPanel.row()
            row.prop(current, "rate", text="Rate")
            row=subPanel.row()
            row.operator("object.pose_util_pose_update")
            row=subPanel.row()
            row.operator("object.pose_util_select_pose_bones")
            row=subPanel.row()
            row.prop(current,"target_bone_list",text="bones")



    

    def draw(self, context):
        layout = self.layout
        poseList = context.scene.blend_pose_set
        row = layout.row()
        col = row.column()
        col.template_list("POSETOOL_UL_poseset_item", "", poseList,
                          "pose_list_set", poseList, "active_index", rows=3)
        
        col = row.column()
        sub = col.column(align=True)
        sub.operator("scene.pose_util_pose_list_add", icon="ADD", text="")
        sub.operator("scene.pose_util_pose_list_remove", icon="REMOVE", text="")
        if len(poseList.pose_list_set) > 0:
            current = poseList.pose_list_set[poseList.active_index]
            if current.target:
                self.draw_target(current.target,layout)
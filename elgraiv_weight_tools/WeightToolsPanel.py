'''
Created on 2017/12/23

@author: take
'''

import bpy
class ToolsPanel:
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "WeightTools"


class WEITGHT_PT_weight_analyzer(ToolsPanel,bpy.types.Panel):
    bl_idname="WEITGHT_PT_weight_analyzer"
    bl_label = "Weight Tools"

    def __init__(self):
        pass

    @classmethod
    def poll(cls, context):
        obj = context.object
        return (obj and obj.type in {'MESH'})

    def draw(self, context):
        layout = self.layout
        layout.operator("object.analyze_weight_count")
        layout.operator("mesh.select_many_weights")
        layout.operator("object.remove_small_weights")
        layout.separator()

class WEITGHT_PT_weight_utils(ToolsPanel,bpy.types.Panel):
    bl_idname="WEITGHT_PT_weight_utils"
    bl_label = "Weight Tools"

    def __init__(self):
        pass

    @classmethod
    def poll(cls, context):
        obj = context.object
        return (obj and obj.type in {'ARMATURE'})

    def draw(self, context):
        layout = self.layout
        layout.operator("object.add_vertex_group_selected")
        layout.operator("object.remove_vertex_group_unselected")
        layout.separator()


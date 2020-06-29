'''
Created on 2017/12/29

@author: take
'''


import bpy
import elgraiv_weight_tools.WeightUtils

class AddVertexGroupForSelectedBonesOp(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.add_vertex_group_selected"
    bl_label = "Add Vertex Groups"

    def execute(self, context):

        if context.selected_bones==None:
            return{'FINISHED'}
        elgraiv_weight_tools.WeightUtils.AddVertexGroupForSelectedBones(context.selected_objects, context.selected_bones)
        return {'FINISHED'}

class RemoveVertexGroupUnselectedBonesOp(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.remove_vertex_group_unselected"
    bl_label = "Remove Vertex Groups"

    def execute(self, context):

        if context.selected_bones==None:
            return{'FINISHED'}
        elgraiv_weight_tools.WeightUtils.RemoveVertexGroupUnselectedBones(context.selected_objects, context.selected_bones)
        return {'FINISHED'}
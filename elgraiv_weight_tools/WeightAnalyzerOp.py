'''
Created on 2017/12/23

@author: take
'''
import bpy
import elgraiv_weight_tools.WeightAnalyzer

class WeightAnalyzerOp(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.analyze_weight_count"
    bl_label = "Analyze Weight Count"

    def execute(self, context):
        obj=context.active_object
        if obj.type!='MESH':
            return{'FINISHED'}
        elgraiv_weight_tools.WeightAnalyzer.AnalyzeWeightCount(obj)
        return {'FINISHED'}

class SelectManyWeightsOp(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "mesh.select_many_weights"
    bl_label = "Select Many Weights"

    def execute(self, context):
        obj=context.active_object
        if context.mode!='EDIT_MESH':
            return {'FINISHED'}
        if obj.type!='MESH':
            return{'FINISHED'}
        elgraiv_weight_tools.WeightAnalyzer.SelectContainsManyWeights(obj)
        obj.data.update()
        return {'FINISHED'}

class RemoveSmallWeightsOp(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.remove_small_weights"
    bl_label = "Remove Small Weights"

    def execute(self, context):
        obj=context.active_object
        if obj.type!='MESH':
            return{'FINISHED'}
        elgraiv_weight_tools.WeightAnalyzer.RemoveSmallWeghit(obj, 0.05)
        return {'FINISHED'}

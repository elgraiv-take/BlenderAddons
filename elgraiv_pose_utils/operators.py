'''
Created on 2024/11/09

@author: take
'''

import bpy

import elgraiv_pose_utils.functions

class PoseListSetupOp(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "scene.pose_util_pose_list_add"
    bl_label = "Setup Pose List"

    def execute(self, context):
        if context.active_object and context.active_object.type in {'ARMATURE'}:
            newItem = context.scene.blend_pose_set.pose_list_set.add()
            newItem.target=context.active_object
        return {'FINISHED'}

class PoseListRemoveOp(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "scene.pose_util_pose_list_remove"
    bl_label = "Remove Pose List"

    def execute(self, context):
        setList = context.scene.blend_pose_set
        delIndex = setList.active_index
        setList.pose_list_set.remove(delIndex)
        return {'FINISHED'}

class PoseAddOp(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.pose_util_pose_add"
    bl_label = "Add Pose"

    def execute(self, context):
        if context.active_object and context.active_object.type in {'ARMATURE'}:
            bones=context.selected_pose_bones_from_active_object
            if bones and len(bones)>0:
                newItem=context.active_object.blend_pose.pose_list.add()
                newItem.object=context.active_object
                elgraiv_pose_utils.functions.RegisterPose(context,newItem,bones)
        return {'FINISHED'}

class PoseUpdateOp(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.pose_util_pose_update"
    bl_label = "Update Pose"

    def execute(self, context):
        if context.active_object and context.active_object.type in {'ARMATURE'}:
            index=context.active_object.blend_pose.active_index
            poseList=context.active_object.blend_pose.pose_list
            bones=context.selected_pose_bones_from_active_object
            if index<len(poseList) and bones and len(bones)>0:
                item=poseList[index]
                item.target_bone_list.clear()
                elgraiv_pose_utils.functions.RegisterPose(context,item,bones)
        return {'FINISHED'}

class SelectPoseBonesOp(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.pose_util_select_pose_bones"
    bl_label = "Select Bones"

    def execute(self, context):
        if context.active_object and context.active_object.type in {'ARMATURE'}:
            index=context.active_object.blend_pose.active_index
            poseList=context.active_object.blend_pose.pose_list
            if index<len(poseList):
                item=poseList[index]
                for bone in item.target_bone_list:
                    context.active_object.pose.bones[bone.name].bone.select=True

        return {'FINISHED'}
class PoseRemoveOp(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.pose_util_pose_remove"
    bl_label = "Remove Pose"

    def execute(self, context):
        setList = context.active_object.blend_pose
        delIndex = setList.active_index
        setList.pose_list.remove(delIndex)
        return {'FINISHED'}
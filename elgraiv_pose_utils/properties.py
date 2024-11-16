
import bpy

import elgraiv_pose_utils.functions

class TargetBonePose(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty()
    translate: bpy.props.FloatVectorProperty(subtype="TRANSLATION")
    rotate: bpy.props.FloatVectorProperty(size=4,subtype="QUATERNION")
    scale: bpy.props.FloatVectorProperty(subtype="XYZ")

class PoseSet(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(default="NewPose")
    object: bpy.props.PointerProperty(type=bpy.types.Object)
    rate: bpy.props.FloatProperty(subtype="FACTOR",min=0.0,max=1.0,update=elgraiv_pose_utils.functions.UpdatePose)
    target_bone_list: bpy.props.CollectionProperty(type=TargetBonePose)

class BlendPoseProperty(bpy.types.PropertyGroup):
    active_index: bpy.props.IntProperty()
    pose_list: bpy.props.CollectionProperty(type=PoseSet)

class BlendPosePtrProperty(bpy.types.PropertyGroup):
    target: bpy.props.PointerProperty(type=bpy.types.Object)

class BlendPoseSetProperty(bpy.types.PropertyGroup):
    active_index: bpy.props.IntProperty()
    pose_list_set: bpy.props.CollectionProperty(type=BlendPosePtrProperty)

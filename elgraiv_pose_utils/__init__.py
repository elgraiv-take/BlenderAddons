bl_info = {
    "name": "Pose Utilities",
    "author": "take@elgraiv",
    "blender": (4, 2, 3),
    "location": "",
    "description": "Pose Utilities",
    "warning": "",
    "tracker_url": "",
    "category": "Animation"
    }


import bpy
import elgraiv_pose_utils.panels
import elgraiv_pose_utils.properties
import elgraiv_pose_utils.operators

classes=[
    properties.TargetBonePose,
    properties.PoseSet,
    properties.BlendPoseProperty,
    properties.BlendPosePtrProperty,
    properties.BlendPoseSetProperty,

    operators.PoseListSetupOp,
    operators.PoseListRemoveOp,
    operators.PoseAddOp,
    operators.PoseRemoveOp,
    operators.PoseUpdateOp,
    operators.SelectPoseBonesOp,

    panels.POSETOOL_PT_pose_utils,
    panels.POSETOOL_UL_poseset_item,
    panels.POSETOOL_UL_pose_item,
    ]

def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.Scene.blend_pose_set=bpy.props.PointerProperty(type=properties.BlendPoseSetProperty)
    bpy.types.Object.blend_pose=bpy.props.PointerProperty(type=properties.BlendPoseProperty)


def unregister():
    del bpy.types.Object.blend_pose
    del bpy.types.Scene.blend_pose_set
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
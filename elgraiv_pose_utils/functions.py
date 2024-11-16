
import bpy
import mathutils

def UpdatePose(self,context):
    object=self.object
    blendPose=object.blend_pose
    pose={}
    for targetPose in blendPose.pose_list:
        rate=targetPose.rate
        for targetBone in targetPose.target_bone_list:
            transformOrigin=mathutils.Matrix.LocRotScale(targetBone.translate,targetBone.rotate,targetBone.scale)
            transform=mathutils.Matrix.Identity(4).lerp(transformOrigin,rate)
            if not targetBone.name in pose:
                pose[targetBone.name]=mathutils.Matrix.Identity(4)
            pose[targetBone.name]=pose[targetBone.name]@transform
    
    for boneName,t in pose.items():
        object.pose.bones[boneName].matrix_basis=t

def RegisterPose(context,poseSet,bones):
    for bone in bones:
        target=poseSet.target_bone_list.add()
        target.name=bone.name
        transform=bone.matrix_basis
        target.translate=transform.to_translation()
        target.rotate=transform.to_quaternion()
        target.scale=transform.to_scale()
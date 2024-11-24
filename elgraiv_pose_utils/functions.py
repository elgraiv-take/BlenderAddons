
import bpy
import mathutils

def MakeMatrixDict(object,ignore):
    blendPose=object.blend_pose
    pose={}
    for targetPose in blendPose.pose_list:
        if targetPose is ignore:
            continue
        rate=targetPose.rate
        for targetBone in targetPose.target_bone_list:
            transformOrigin=mathutils.Matrix.LocRotScale(targetBone.translate,targetBone.rotate,targetBone.scale)
            transform=mathutils.Matrix.Identity(4).lerp(transformOrigin,rate)
            if not targetBone.name in pose:
                pose[targetBone.name]=mathutils.Matrix.Identity(4)
            pose[targetBone.name]=pose[targetBone.name]@transform
    return pose


def UpdatePose(self,context):
    object=self.object
    pose=MakeMatrixDict(object,None)
    
    for boneName,t in pose.items():
        object.pose.bones[boneName].matrix_basis=t

def RegisterPose(context,poseSet,bones):
    pose=MakeMatrixDict(poseSet.object,poseSet)
    for bone in bones:
        target=poseSet.target_bone_list.add()
        target.name=bone.name
        transform=bone.matrix_basis        
        if bone.name in pose:
            t=pose[bone.name].inverted_safe()
            transform=t@transform
        target.translate=transform.to_translation()
        target.rotate=transform.to_quaternion()
        target.scale=transform.to_scale()
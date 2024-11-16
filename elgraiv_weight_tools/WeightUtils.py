'''
Created on 2017/12/29

@author: take
'''

import bpy
import math

def AddVertexGroupForSelectedBones(objects,bones):
    for obj in objects:
        if obj.type!='MESH':
            continue
        for bone in bones:
            boneName=bone.name
            if obj.vertex_groups.get(boneName,None)==None:
                obj.vertex_groups.new(name=boneName)


def RemoveVertexGroupUnselectedBones(objects,bones):
    for obj in objects:
        if obj.type!='MESH':
            continue
        removeList=[]
        for vg in obj.vertex_groups:
            for bone in bones:
                if vg.name==bone.name:
                    break
            else:
                removeList.append(vg)
        for vg in removeList:
            obj.vertex_groups.remove(vg)






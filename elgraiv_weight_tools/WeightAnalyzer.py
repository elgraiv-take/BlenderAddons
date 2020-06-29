'''
Created on 2017/12/23

@author: take
'''

import bpy
import bmesh

CountColorLayerName="_WeightCount"
CountColorTable=[
    [0.0,0.0,0.0],
    [0.0,0.0,1.0],
    [0.0,1.0,0.0],
    [1.0,0.0,0.0],
    ]

def CountWeight(meshObj):
    mesh=meshObj.data
    counts=[0]*len(mesh.vertices)
    for i in range(len(mesh.vertices)):
        for vg in meshObj.vertex_groups:
            value=0.0
            try:
                value=vg.weight(i)
            except:
                pass
            if(value>0.0):
                counts[i]+=1

    return counts

def ConvertCountToVertexColor(meshObj,counts):
    mesh=meshObj.data
    colorLayer=None
    if mesh.vertex_colors.find(CountColorLayerName)<0:
        colorLayer=mesh.vertex_colors.new(CountColorLayerName)
    else:
        colorLayer=mesh.vertex_colors[CountColorLayerName]
    for i in range(len(colorLayer.data)):
        vertexIndex=mesh.loops[i].vertex_index
        colorIndex=counts[vertexIndex]
        if not colorIndex<len(CountColorTable):
            colorIndex=len(CountColorTable)-1
        colorLayer.data[i].color[0]=CountColorTable[colorIndex][0]
        colorLayer.data[i].color[1]=CountColorTable[colorIndex][1]
        colorLayer.data[i].color[2]=CountColorTable[colorIndex][2]

def AnalyzeWeightCount(meshObj):
    counts=CountWeight(meshObj)
    ConvertCountToVertexColor(meshObj, counts)


def SelectContainsManyWeights(meshObj):
    counts=CountWeight(meshObj)
    mesh=bmesh.from_edit_mesh(meshObj.data)
    for i in range(len(mesh.verts)):
        if counts[i]>2:
            mesh.verts[i].select=True
        else:
            mesh.verts[i].select=False

def RemoveSmallWeghit(meshObj,threshold):
    mesh=meshObj.data
    for i in range(len(mesh.vertices)):
        for vg in meshObj.vertex_groups:
            try:
                value=0.0
                value=vg.weight(i)
                if(value<threshold):
                    try:
                        vg.remove([i])
                    except Exception as e:
                        print(e)
            except:
                pass

'''
Created on 2019/08/11

@author: take
'''


import bpy

class FbxExportItem(bpy.types.PropertyGroup):
    name:bpy.props.StringProperty()

class FbxExportSet(bpy.types.PropertyGroup):
    name:bpy.props.StringProperty()
    save_path:bpy.props.StringProperty()
    active_object_index:bpy.props.IntProperty()
    object_list:bpy.props.CollectionProperty(type=FbxExportItem)

class FbxExportSetProperty(bpy.types.PropertyGroup):
    active_index:bpy.props.IntProperty()
    export_set_list:bpy.props.CollectionProperty(type=FbxExportSet)

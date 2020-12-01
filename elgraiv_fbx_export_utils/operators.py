'''
Created on 2019/08/11

@author: take
'''


import bpy
import bpy_extras


class FbxToolsExportOp(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "export_scene.fbx_ex"
    bl_label = "Export Fbx set"

    def execute(self, context):
        current = context.scene.export_set.export_set_list[context.scene.export_set.active_index]
        if len(current.save_path) <= 0:
            return {'FINISHED'}
        layerCollection = context.window.view_layer.layer_collection
        layers = [(layer.name, layer.exclude)
                  for layer in layerCollection.children]
        for layer in layers:
            layerCollection.children[layer[0]].exclude = False
        bpy.ops.object.select_all(action='DESELECT')
        invisibles=[]
        for n in current.object_list:
            if not n.item.visible_get():
                invisibles.append(n.item.name)
            n.item.select_set(True)
        if len(invisibles)>0:
            self.report({'ERROR'}, "Hidden Items:"+str(invisibles))
            return {'CANCELLED'}
        bpy.ops.export_scene.fbx(
            filepath=current.save_path,
            check_existing=True,
            bake_anim=current.export_anim,
            filter_glob="*.fbx",
            use_selection=True,
            apply_scale_options="FBX_SCALE_ALL",
            object_types={'EMPTY', 'ARMATURE', 'MESH'})

        for layer in layers:
            layerCollection.children[layer[0]].exclude = layer[1]
        return {'FINISHED'}


class FbxToolsExportSetAddOp(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "scene.fbx_export_set_add"
    bl_label = "Add Export Set"

    def execute(self, context):
        newItem = context.scene.export_set.export_set_list.add()
        newItem.name = "NewSet"
        for o in context.selected_objects:
            item = newItem.object_list.add()
            item.item = o
        return {'FINISHED'}


class FbxToolsExportSetRemoveOp(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "scene.fbx_export_set_remove"
    bl_label = "Remove Export Set"

    def execute(self, context):
        setList = context.scene.export_set
        delIndex = setList.active_index
        setList.export_set_list.remove(delIndex)
        return {'FINISHED'}


class FbxToolsExportSetChoosePathOp(bpy.types.Operator, bpy_extras.io_utils.ExportHelper):
    bl_idname = "export_scene.choose_fbx_path"
    bl_label = "Choose Export Path"
    filename_ext = ".fbx"

    def execute(self, context):
        sets = context.scene.export_set
        activeIndex = sets.active_index
        sets.export_set_list[activeIndex].save_path = self.filepath
        return {'FINISHED'}

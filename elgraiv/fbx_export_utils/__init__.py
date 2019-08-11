bl_info = {
    "name": "Fbx Export Utilities",
    "author": "take@elgraiv",
    "blender": (2, 80, 0),
    "location": "",
    "description": "Fbx Export Utilities",
    "warning": "",
    "tracker_url": "",
    "category": "Import-Export"
    }


import bpy

import elgraiv.fbx_export_utils.properties
import elgraiv.fbx_export_utils.operators

def register():
    import imp

#     imp.reload(ElgraivFbxTools.FbxToolsPanel)
#     imp.reload(ElgraivFbxTools.FbxToolsExportSetProps)

    bpy.utils.register_module(__name__)
    bpy.types.Scene.export_set=bpy.props.PointerProperty(type=elgraiv.fbx_export_utils.properties.FbxExportSetProperty)


def unregister():
    del bpy.types.Scene.export_set
    bpy.utils.unregister_module(__name__)

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

import elgraiv_fbx_export_utils.properties
import elgraiv_fbx_export_utils.operators
import elgraiv_fbx_export_utils.panels

classes=[
    properties.FbxExportItem,
    properties.FbxExportSet,
    properties.FbxExportSetProperty,

    operators.FbxToolsExportOp,
    operators.FbxToolsExportSetAddOp,
    operators.FbxToolsExportSetRemoveOp,

    panels.FBXTOOL_UL_export_set,
    panels.FBXTOOL_UL_export_item,
    panels.FBXTOOL_PT_fbx_exporter,

    ]

def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.Scene.export_set=bpy.props.PointerProperty(type=properties.FbxExportSetProperty)


def unregister():
    del bpy.types.Scene.export_set
    for c in reversed(classes):
        bpy.utils.unregister_class(c)

        
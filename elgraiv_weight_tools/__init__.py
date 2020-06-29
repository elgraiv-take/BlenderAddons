bl_info = {
    "name": "WeightTools",
    "author": "take@elgraiv",
    "blender": (2, 80, 0),
    "location": "",
    "description": "Weight Tools",
    "warning": "",
    "tracker_url": "",
    "category": "Mesh"
    }


import bpy

import elgraiv_weight_tools.WeightAnalyzer
import elgraiv_weight_tools.WeightAnalyzerOp

import elgraiv_weight_tools.WeightUtils
import elgraiv_weight_tools.WeightUtilsOp

import elgraiv_weight_tools.WeightToolsPanel

classes=[
    WeightAnalyzerOp.RemoveSmallWeightsOp,
    WeightAnalyzerOp.SelectManyWeightsOp,
    WeightAnalyzerOp.WeightAnalyzerOp,

    WeightUtilsOp.AddVertexGroupForSelectedBonesOp,
    WeightUtilsOp.RemoveVertexGroupUnselectedBonesOp,

    WeightToolsPanel.WEITGHT_PT_weight_analyzer,
    WeightToolsPanel.WEITGHT_PT_weight_utils,
]

def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
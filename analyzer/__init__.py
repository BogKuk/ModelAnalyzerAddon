bl_info = {
    "name": "Analyzer",
    "author": "Kukushkin Bogdan Aleksandrovich",
    "version": (0, 0, 1),
    "blender": (4, 4, 3),
    "location": "View3D > N-panel > Overdetail",
    "description": "Assessment of the quality and excessive detail of 3D models",
    "category": "Object",
}

import bpy

from .operators import OBJECT_OT_analyzer, OBJECT_OT_CheckNonManifold, OBJECT_OT_fix_inverted_normals
from .panel import VIEW3D_PT_analyzer_panel
from .props import register_props, unregister_props

classes = (
    OBJECT_OT_analyzer,
    OBJECT_OT_CheckNonManifold,
    OBJECT_OT_fix_inverted_normals,
    VIEW3D_PT_analyzer_panel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    register_props()

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    unregister_props()

if __name__ == "__main__":
    register()

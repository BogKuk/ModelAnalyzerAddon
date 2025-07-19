import bpy

class VIEW3D_PT_analyzer_panel(bpy.types.Panel):
    bl_label = "Analyzer"
    bl_idname = "VIEW3D_PT_analyzer_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Analyzer'

    def draw(self, context):
        layout = self.layout
        layout.operator("object.analyzer")

import bpy

class VIEW3D_PT_analyzer_panel(bpy.types.Panel):
    bl_label = "Analyzer"
    bl_idname = "VIEW3D_PT_analyzer_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Analyzer'

    def draw(self, context):
        layout = self.layout
        layout.operator("object.analyzer", icon='VIEWZOOM')
        layout.operator("object.check_non_manifold", icon='VIEWZOOM')
        scene = context.scene

        layout.label(text=f"Polygon Count: {scene.poly_count}")
        layout.label(text=f"Polygon Density: {scene.poly_density:.2f}")
        layout.label(text=scene.non_manifold_report)

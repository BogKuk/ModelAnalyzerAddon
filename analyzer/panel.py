import bpy

class VIEW3D_PT_analyzer_panel(bpy.types.Panel):
    bl_label = "Analyzer"
    bl_idname = "VIEW3D_PT_analyzer_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Analyzer'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        layout.operator("object.analyzer", icon='VIEWZOOM')
        layout.label(text=f"Polygon Count: {scene.poly_count}")
        layout.label(text=f"Polygon Density: {scene.poly_density:.2f}")

        layout.operator("object.check_non_manifold", icon='VIEWZOOM')
        layout.label(text=scene.non_manifold_report)

        layout.operator("object.fix_inverted_normals", icon="MOD_NORMALEDIT")

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

        layout.prop(scene, "overdetail_context", text="Контекст")

        box = layout.box()
        box.label(text="Плотность (pols/m²):")
        box.prop(scene, "overdetail_threshold_hero", text="Hero")
        box.prop(scene, "overdetail_threshold_prop", text="Prop")
        box.prop(scene, "overdetail_threshold_background", text="Background")

        layout.label(text="Общий анализ:")
        layout.prop(scene, "poly_count", text="Полигонов")
        layout.prop(scene, "poly_density", text="Плотность")

        if scene.overdetail_report:
            for line in scene.overdetail_report.split('\n'):
                layout.label(text=line)

        layout.separator()

        layout.operator("object.analyzer", icon='VIEWZOOM')

        layout.operator("object.check_non_manifold", icon='VIEWZOOM')
        layout.label(text=scene.non_manifold_report)

        layout.operator("object.fix_inverted_normals", icon="MOD_NORMALEDIT")

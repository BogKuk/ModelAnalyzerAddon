import bpy

from analyzer import utils, props

class OBJECT_OT_analyzer(bpy.types.Operator):
    bl_idname = "object.analyzer"
    bl_label = "Общий анализ"
    bl_description = "Проверяет кол-во полигонов и их плотность"
    bl_options = {'REGISTER'}

    def execute(self, context):
        obj = context.active_object
        utils.object_check(self, obj)

        utils.edit_mode_select(obj)

        mesh = obj.data
        context.scene.poly_count = len(mesh.polygons)
        context.scene.poly_density = utils.calculate_poly_density(obj)

        self.report({'INFO'}, "Базовый анализ завершен")
        return {'FINISHED'}

class OBJECT_OT_CheckNonManifold(bpy.types.Operator):
    bl_idname = "object.check_non_manifold"
    bl_label = "Non-manifold анализ"
    bl_description = "Проверяет наличие non-manifold геометрии"

    def execute(self, context):
        obj = context.active_object
        utils.object_check(self, obj)

        utils.edit_mode_select(obj)

        non_manifold_edges = utils.remove_non_manifold_edges(obj)
        context.scene.non_manifold_report = f"Non-manifold рёбер: {non_manifold_edges}"

        self.report({'INFO'}, "Анализ non-manifold рёбер завершен")
        return {'FINISHED'}

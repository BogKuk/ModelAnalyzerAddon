import bpy

from analyzer import utils

class OBJECT_OT_analyzer(bpy.types.Operator):
    bl_idname = "object.analyzer"
    bl_label = "Проверить модель"
    bl_description = "Проверяет качество и избыточность детализации текущего объекта"
    bl_options = {'REGISTER'}

    def execute(self, context):
        obj = context.active_object
        if not obj or obj.type != 'MESH':
            self.report({'WARNING'}, "Выделите объект с типом MESH")
            return {'CANCELLED'}

        mesh = obj.data
        poly_count = len(mesh.polygons)
        density = utils.calculate_poly_density(obj)

        self.report({'INFO'}, f"Полигоны: {poly_count}, Плотность: {density:.2f}")
        return {'FINISHED'}

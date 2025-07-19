import bpy

class OBJECT_OT_analyzer(bpy.types.Operator):
    bl_idname = "object.analyzer"
    bl_label = "Проверить модель"
    bl_description = "Проверяет качество и избыточность детализации текущего объекта"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        if not obj or obj.type != 'MESH':
            self.report({'WARNING'}, "Выделите объект с типом MESH")
            return {'CANCELLED'}

        mesh = obj.data
        poly_count = len(mesh.polygons)
        bbox = obj.dimensions
        density = poly_count / (bbox.x * bbox.y * bbox.z) if bbox.x * bbox.y * bbox.z > 0 else 0

        self.report({'INFO'}, f"Полигоны: {poly_count}, Плотность: {density:.2f}")
        return {'FINISHED'}

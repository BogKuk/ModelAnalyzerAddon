import bpy
import bmesh

from analyzer import utils


class OBJECT_OT_analyzer(bpy.types.Operator):
    bl_idname = "object.analyzer"
    bl_label = "Общий анализ"
    bl_description = "Проверяет кол-во полигонов и их плотность, проводит контекстный анализ"
    bl_options = {'REGISTER'}

    def execute(self, context):
        obj = context.active_object
        utils.object_check(self, obj)

        utils.mode_select(obj,'EDIT')

        mesh = obj.data

        density = utils.calculate_poly_density(obj)
        poly_count = len(mesh.polygons)

        thresh = {
            'HERO': context.scene.overdetail_threshold_hero,
            'PROP': context.scene.overdetail_threshold_prop,
            'BACKGROUND': context.scene.overdetail_threshold_background,
        }[context.scene.overdetail_context]

        is_overdetailed = density > thresh

        result = {
            "poly_count": poly_count,
            "density": density,
            "threshold": thresh,
            "overdetail": is_overdetailed
        }

        context.scene.overdetail_report = (
                f"Контекст: {context.scene.overdetail_context}\n"
                f"Кол-во полигонов: {result['poly_count']}\n"
                f"Плотность: {result['density']:.1f} pols/m² (thr: {result['threshold']:.1f})\n"
                + ("⚠️ Over-detailed" if result['overdetail'] else "✔ OK")
        )

        self.report({'INFO'}, "Контекстный Анализ завершен")
        return {'FINISHED'}

class OBJECT_OT_CheckNonManifold(bpy.types.Operator):
    bl_idname = "object.check_non_manifold"
    bl_label = "Non-manifold анализ"
    bl_description = "Проверяет наличие non-manifold геометрии"

    def execute(self, context):
        obj = context.active_object
        utils.object_check(self, obj)

        utils.mode_select(obj, 'EDIT')

        bm = bmesh.from_edit_mesh(obj.data)
        bm.normal_update()

        for v in bm.verts:
            v.select = False
        for e in bm.edges:
            e.select = False
        for f in bm.faces:
            f.select = False

        non_manifold_edges = [e for e in bm.edges if not e.is_manifold]

        for e in non_manifold_edges:
            e.select = True
            for v in e.verts:
                v.select = True

        bmesh.update_edit_mesh(obj.data)

        non_manifold_edges = len(non_manifold_edges)
        context.scene.non_manifold_report = f"Non-manifold рёбер: {non_manifold_edges}"

        self.report({'INFO'}, "Анализ non-manifold рёбер завершен")
        return {'FINISHED'}

class OBJECT_OT_fix_inverted_normals(bpy.types.Operator):
    bl_idname = "object.fix_inverted_normals"
    bl_label = "Исправить перевернутые нормали"
    bl_description = "Исправляет перевернутые нормали на активном объекте"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        utils.object_check(self, obj)

        utils.mode_select(obj, 'OBJECT')

        me = obj.data

        bm = bmesh.new()
        bm.from_mesh(me)
        bm.normal_update()

        bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
        bm.to_mesh(me)
        bm.free()

        self.report({'INFO'}, "Анализ нормалей завершен.")
        return {'FINISHED'}

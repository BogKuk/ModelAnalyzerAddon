import  bmesh
import bpy


def object_check(self, obj):
    if not obj or obj.type != 'MESH':
        self.report({'WARNING'}, "Выделите объект с типом MESH")
        return {'CANCELLED'}


def mode_select(obj, mode:str):
    if obj.mode != mode:
        bpy.ops.object.mode_set(mode=mode)


def calculate_poly_density(obj):
    bm = bmesh.new()
    bm.from_mesh(obj.data)
    bm.normal_update()

    poly_count = len(bm.faces)
    surface_area = sum(f.calc_area() for f in bm.faces)

    bm.free()

    return poly_count / surface_area if surface_area > 0 else 0

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
    mesh = obj.data
    poly_count = len(mesh.polygons)
    bbox = obj.dimensions
    volume = bbox.x * bbox.y * bbox.z
    return poly_count / volume if volume > 0 else 0

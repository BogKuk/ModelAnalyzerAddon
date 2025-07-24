import  bmesh
import bpy


def object_check(self, obj):
    if not obj or obj.type != 'MESH':
        self.report({'WARNING'}, "Выделите объект с типом MESH")
        return {'CANCELLED'}


def edit_mode_select(obj):
    if obj.mode != 'EDIT':
        bpy.ops.object.mode_set(mode='EDIT')


def calculate_poly_density(obj):
    mesh = obj.data
    poly_count = len(mesh.polygons)
    bbox = obj.dimensions
    volume = bbox.x * bbox.y * bbox.z
    return poly_count / volume if volume > 0 else 0


def remove_non_manifold_edges(obj):
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

    return len(non_manifold_edges)

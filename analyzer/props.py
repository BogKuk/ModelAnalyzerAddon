import bpy

def register_props():
    bpy.types.Scene.poly_count = bpy.props.IntProperty(name="Polygon Count", default=0)
    bpy.types.Scene.poly_density = bpy.props.FloatProperty(name="Polygon Density", default=0.0)
    bpy.types.Scene.non_manifold_report = bpy.props.StringProperty(name="Non-Manifold Info", default="")

def unregister_props():
    del bpy.types.Scene.poly_count
    del bpy.types.Scene.poly_density
    del bpy.types.Scene.non_manifold_report
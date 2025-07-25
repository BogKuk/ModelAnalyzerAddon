import bpy

from bpy.props import EnumProperty, FloatProperty

def register_props():
    bpy.types.Scene.non_manifold_report = bpy.props.StringProperty(name="Non-Manifold грани", default="")
    bpy.types.Scene.overdetail_context = EnumProperty(
        name="Context",
        description="Role of the object in scene",
        items=[
            ('HERO', "Hero", "Main character or close-up mesh"),
            ('PROP', "Prop", "Средний уровень детализации"),
            ('BACKGROUND', "Background", "Фоновые объекты"),
        ],
        default='PROP',
    )
    bpy.types.Scene.overdetail_threshold_hero = FloatProperty(
        name="Hero Threshold",
        default=3000,
        description="Max tris per square meter for hero meshes"
    )
    bpy.types.Scene.overdetail_threshold_prop = FloatProperty(
        name="Prop Threshold",
        default=1000,
        description="Max tris per square meter for props"
    )
    bpy.types.Scene.overdetail_threshold_background = FloatProperty(
        name="Background Threshold",
        default=500,
        description="Max tris per square meter for background"
    )
    bpy.types.Scene.overdetail_report = bpy.props.StringProperty(
        name="Overdetail Report",
        description="Результаты анализа избыточной детализации",
        default=""
    )


def unregister_props():
    del bpy.types.Scene.non_manifold_report
    del bpy.types.Scene.overdetail_context
    del bpy.types.Scene.overdetail_threshold_hero
    del bpy.types.Scene.overdetail_threshold_prop
    del bpy.types.Scene.overdetail_threshold_background
    del bpy.types.Scene.overdetail_report

def calculate_poly_density(obj):
    mesh = obj.data
    poly_count = len(mesh.polygons)
    bbox = obj.dimensions
    volume = bbox.x * bbox.y * bbox.z
    return poly_count / volume if volume > 0 else 0

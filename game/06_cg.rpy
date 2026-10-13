# Optional CGs become available when their original files are placed here.
init python:
    for cg_name in ("change", "invitation"):
        cg_path = "images/cg/" + cg_name + ".jpg"
        if renpy.loadable(cg_path):
            renpy.image("cg " + cg_name, Transform(cg_path, xysize=(1920, 1080), fit="contain"))

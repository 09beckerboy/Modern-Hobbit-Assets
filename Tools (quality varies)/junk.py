import os
import bpy


def purge_orphans():
    if bpy.app.version >= (3, 0, 0):
        bpy.ops.outliner.orphans_purge(
            do_local_ids=True, do_linked_ids=True, do_recursive=True
        )
    else:
        # call purge_orphans() recursively until there are no more orphan data blocks to purge
        result = bpy.ops.outliner.orphans_purge()
        if result.pop() != "CANCELLED":
            purge_orphans()


def clean_scene():
    """
    Removing all of the objects, collection, materials, particles,
    textures, images, curves, meshes, actions, nodes, and worlds from the scene
    """
    if bpy.context.active_object and bpy.context.active_object.mode == "EDIT":
        bpy.ops.object.editmode_toggle()

    for obj in bpy.data.objects:
        obj.hide_set(False)
        obj.hide_select = False
        obj.hide_viewport = False

    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()

    collection_names = [col.name for col in bpy.data.collections]
    for name in collection_names:
        bpy.data.collections.remove(bpy.data.collections[name])

    # in the case when you modify the world shader
    world_names = [world.name for world in bpy.data.worlds]
    for name in world_names:
        bpy.data.worlds.remove(bpy.data.worlds[name])
    # create a new world data block
    bpy.ops.world.new()
    bpy.context.scene.world = bpy.data.worlds["World"]

    purge_orphans()


##########################################################
#  _____                          _          _  _     __
# |  ___|                        | |       _| || |_  /  |
# | |____  ____ _ _ __ ___  _ __ | | ___  |_  __  _| `| |
# |  __\ \/ / _` | '_ ` _ \| '_ \| |/ _ \  _| || |_   | |
# | |___>  < (_| | | | | | | |_) | |  __/ |_  __  _| _| |_
# \____/_/\_\__,_|_| |_| |_| .__/|_|\___|   |_||_|   \___/
#                          | |
#                          |_|
##########################################################

clean_scene()

directory = "C:\\Users\\09beckerboy\\Documents\\Hobbit Modding\\Hobbit Assets"
file_errors = []
for root, dirs, files in os.walk(directory):
    for filename in files:
        if filename.endswith(".obj"):
            try:
                clean_scene()
                file_path = os.path.join(root, filename)
                file_path_2 = os.path.join(root, filename.split(".")[0]+".fbx")
                bpy.ops.import_scene.obj(filepath=file_path)
                bpy.ops.export_scene.fbx(filepath=file_path_2,path_mode="COPY",embed_textures=True)
                continue
            except Exception:
                file_errors.append(filename)
print(file_errors)
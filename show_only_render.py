import bpy

bl_info = {
    'name': "Show Only Render",
    'description': "Toggle to show only rendered objects in the viewport",
    'author': "Artell",
    "version": (1, 10, 10),
    'blender': (2, 80, 0),
    'location': "Tools Panel (T) in viewport",
    'wiki_url': "",
    'category': "Render",
    }


class SOR_PT_menu(bpy.types.Panel):
    bl_category = ""
    bl_label = ""
    bl_options = set({'HIDE_HEADER'})
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_category = "View"    

    @classmethod
    def poll(self, context):
        return True

    def draw(self, context):
        layout = self.layout        
        layout.prop(bpy.context.scene, "sor_show_only_render", text="Show Only Render")

    
def update_show_only_render(self, context):    
    for obj in bpy.context.scene.objects:  
        if context.scene.sor_show_only_render:
            obj.hide_set(obj.hide_render)    
        else:
            obj.hide_set(False)    
           
                
            
            
            
classes = (
    SOR_PT_menu,
    )
    
    
def register():   
    from bpy.utils import register_class

    for cls in classes:
        register_class(cls)
    
    bpy.types.Scene.sor_show_only_render = bpy.props.BoolProperty(name="Show Only Render", default = False, description="Show only renderable objects", update=update_show_only_render)

    
def unregister():   
    from bpy.utils import unregister_class

    for cls in reversed(classes):
        unregister_class(cls)
    
    del bpy.types.Scene.sor_show_only_render



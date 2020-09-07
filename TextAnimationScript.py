import bpy


#-----------Main functions--------------
def main():
    #PrepareText()
    StaggerKeyframes()
#---------------------------------------







#convert to mesh
def ConvertToMesh():
    bpy.ops.object.convert(target='MESH')

#separate by loose objects
def SeparateByLooseObjects():
    bpy.ops.mesh.separate(type='LOOSE')

#set origin to geometry
def SetOriginToGeometry():
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')

#stagger keyframes
def StaggerKeyframes():
    
    #Stagger variables
    offset_frames = 1
    step = 1
    
    #Selected object list
    object_list = bpy.context.selected_objects
    object_list = object_list[::-1] # reverse object list
    
    #loop variables
    index = 0
    
    #staggering loop
    for i in range(0, len(object_list)):
        print("--"+str(i))
        if index>0: #skip if it's the first object            
            object=object_list[index] #assign current object to a variable
            print(object)
            
            #move keyframes by offset
            for fcurve in object.animation_data.action.fcurves:
                for point in fcurve.keyframe_points:
                     point.co.x += offset_frames 
            
            #iterate offset frames
            offset_frames += step #iterate offset frames
        
        index+=step #iterate index
        
def PrepareText():
    ConvertToMesh()
    SeparateByLooseObjects()
    SetOriginToGeometry()

main()

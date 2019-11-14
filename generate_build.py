import bpy
import csv
import math
from datetime import datetime,time,timedelta
import sys

argv = sys.argv
argv = argv[argv.index("--") + 1:]

#path = "/Users/CAL/Desktop/"
#"test_blender_house"
#"garage_4_courses"
#"Garage Bricks v1.3"
#"if needed 16 courses 2 doors"
 
# parameters 
#path = "/Users/CAL/Documents/TC/repos/csv_model_generator/"
path = "/Users/CAL/Desktop/"

if(len(argv) == 1):
    # do here
    file = argv[0]
    track_version = 2
elif(len(argv)):
    # do two args
    file = argv[0]
    track_version = int(argv[1])
else:
    path = "/Users/CAL/Documents/TC/repos/csv_model_generator/"
    file = "example_track1_csv"
    track_version = 1
    

# track v1 dimensions
if (track_version == 1):
    length1 = [0,3820]
    length2 = [5996.5,7684]
    length3 = [9925.5,13638]
    length4 = [15875,17562.5]
elif(track_version == 2):
    #track v2 dimensions (for garage)
    length1 = [0,5620]
    length2 = [6107.5,11292.5]
    length3 = [12107.5,17732.5]
    length4 = [19107.5,24507.5]

def add_brick(x,z,y,angle):
    bpy.ops.mesh.primitive_cube_add(location=(x,z,y), size=1)
    bpy.ops.transform.resize(value=(0.215,0.1025,0.065))
    if (angle > 0):
        bpy.context.active_object.rotation_mode = 'XYZ'
        radians = (angle/180 * math.pi)
        bpy.context.active_object.rotation_euler = (0,0,math.pi/2)

def add_half_brick(x,z,y,angle):
    bpy.ops.mesh.primitive_cube_add(location=(x,z,y), size=1)
    bpy.ops.transform.resize(value=(0.1075,0.1025,0.065))
    if (angle > 0):
        bpy.context.active_object.rotation_mode = 'XYZ'
        radians = (angle/180 * math.pi)
        bpy.context.active_object.rotation_euler = (0,0,math.pi/2)


def ten_brick():
    brick_placement = 0
    for i in range(10):
        add_brick(brick_placement,0.05125,0.0325)
        print("Added brick No. " + str(i + 1))
        brick_placement += 0.215

timeStart = datetime.now()
with open(path + file + '.csv','r') as csvinput:
    reader = csv.reader(csvinput)
    row = next(reader)
    ## gather brick data
    if (float(row[1]) < length1[1]):
        angle = 0
    elif (float(row[1]) < length2[1]):
        angle = 90
    if (row[10] == "TRUE"):
        ghost_brick = True
    else:
        ghost_brick = False
    if (ghost_brick == False):
        print("Brick No. " + row[0])
        add_brick((float(row[1])/1000),0,(float(row[2])/1000),angle)
    length3_y_plane = ((length2[1] - length2[0]) + 56.25 + 56.25 )/1000 
    count = 0
    for row in reader:
        ######
        # brick data
        ######
        if (row[10] == "TRUE"):
            ghost_brick = True
        else:
            ghost_brick = False
        if (row[8] == "TRUE"):
            half_brick_left = True
        else:
            half_brick_left = False
        if (row[9] == "TRUE"):
            half_brick_right = True
        else:
            half_brick_right = False
        ###### length 1
        if (float(row[1]) <= length1[1]):
            angle = 0
            if (half_brick_left):
                # here
                print("Brick No. " + row[0])
                add_half_brick(((float(row[1])/1000)-0.05375),0,(float(row[2])/1000),angle)
            elif(half_brick_right):
                # here
                print("Brick No. " + row[0])
                add_half_brick(((float(row[1])/1000) + 0.05375),0,(float(row[2])/1000),angle)
            elif (ghost_brick == False):
                print("Brick No. " + row[0])
                add_brick((float(row[1])/1000),0,(float(row[2])/1000),angle)
        ###### length 2
        elif (float(row[1]) <= length2[1]):
            angle = 90
            y_pos = (float(row[1])/1000) - ((length2[0] - 56.25)/1000)
            last_y = y_pos
            # fixed x plane is the greatest possible X value for brick on length 1 + 5mm + (102.5mm/2)
            x_plane = length1[1]/1000 + (5/1000) + (102.5/2/1000)
            if (half_brick_left):
                print("Brick No. " + row[0])
                add_half_brick(x_plane,y_pos - 0.05375,(float(row[2])/1000),angle)
            elif(half_brick_right):
                print("Brick No. " + row[0])
                add_half_brick(x_plane,y_pos + 0.05375,(float(row[2])/1000),angle)
            elif (ghost_brick == False):
                print("Brick No. " + row[0])
                add_brick(x_plane,y_pos,(float(row[2])/1000),angle)
        ###### length 3
        elif (float(row[1]) <= length3[1]):
            angle = 0
            x_pos = (length1[1]/1000) - ((float(row[1])/1000)  - (length3[0]/1000))
            if (half_brick_left):
                print("Brick No. " + row[0])
                add_half_brick(x_pos + 0.05375,length3_y_plane,(float(row[2])/1000),angle)
            elif(half_brick_right):
                print("Brick No. " + row[0])
                add_half_brick(x_pos - 0.05375,length3_y_plane,(float(row[2])/1000),angle)
            elif (ghost_brick == False):
                print("Brick No. " + row[0])
                # fixed y plane is the greatest possible y used in the previoius length (2)
                # max brick length 2 - min brick length 2 - 56.25 used as it's difference between brick length centre and brick width centre
                #length3_y_plane = ((length2[1] - length2[0]) + 56.25 + 56.25 )/1000 
                #y_plane = last_y + (5/1000) + (102.5/2/1000)
                add_brick(x_pos,length3_y_plane,(float(row[2])/1000),angle)
        ###### length 4
        elif (float(row[1]) <= length4[1]):
            angle = 270
            y_pos = length3_y_plane - ((float(row[1])/1000) - (length4[0]/1000)) - (56.25 /1000)
            if (half_brick_left):
                print("Brick No. " + row[0])
                add_half_brick(0.05125,y_pos + 0.05375,(float(row[2])/1000),angle)
            elif(half_brick_right):
                print("Brick No. " + row[0])
                add_half_brick(0.05125,y_pos - 0.05375,(float(row[2])/1000),angle)
            elif(ghost_brick == False):
                print("Brick No. " + row[0])
                add_brick(0.05125,y_pos,(float(row[2])/1000),angle)
        count += 1
        bpy.context.active_object.name = "brick_" + format(row[0],"0>5s")


print("Execution completed at ", datetime.now().strftime("%X"))
total = datetime.now() - timeStart
print("Took ", total.total_seconds())

# csv_model_generator
Python file used to read in a CSV file containing a house build to then produce a 3D model/visualisation in Blender

HOWTO Run file:

1) Open Blender > New File (General) > Scripting > Python Console

2) Edit the generate_build.py file. At the top of the file change the path, file and track_version lines. track_version = 1 for the test track and =2 for the garage track.

3) Execute in the console:  exec(compile(open("/Users/CAL/Desktop/generate_build.py").read(), "/Users/CAL/Desktop/generate_build.py", 'exec'))
   Where "/Users/CAL/Desktop/generate_build.py" is the path to the generate_build.py file

4) Do not use blender whilst the code executes - upon build the console will show the time taken to produce the 3D model

# CSV 3D Model Generator
Python file used to read in a CSV file containing a house build to then produce a 3D model/visualisation in Blender

How To Run Automatically:
1) Edit the generate_build.py file. At the top of the file change the default path to your CSV files.

2) Run by double clicking the produce_model.bat file - when prompted input the CSV file name (without '.csv') and track number as 1 or 2. (The bat file should be edited to contain your path to blender and to the generate_build.py file)

Run Automatically From Command Line:

1) No Parameters: Path = Repo folder, File = "example_track1_csv", Track = 1
cd "C:\Program Files\Blender Foundation\Blender\"; ./blender C:\Users\CAL\Documents\first_test.blend --python C:\Users\CAL\Documents\TC\repos\csv_model_generator\generate_build.py --
2) One Parameter: File parameter in quotes
cd "C:\Program Files\Blender Foundation\Blender\"; ./blender C:\Users\CAL\Documents\first_test.blend --python C:\Users\CAL\Documents\TC\repos\csv_model_generator\generate_build.py -- "Garage Bricks v1.3"
3) Two Parameter: File parameter in quotes, Track version as integer
cd "C:\Program Files\Blender Foundation\Blender\"; ./blender C:\Users\CAL\Documents\first_test.blend --python C:\Users\CAL\Documents\TC\repos\csv_model_generator\generate_build.py -- "Four Full Layers (03_10_2019)" 1


How To Run Manually:

1) Open Blender > New File (General) > Scripting > Python Console

2) Edit the generate_build.py file. At the top of the file change the path, file and track_version lines. track_version = 1 for the test track and =2 for the garage track.

3) Execute in the console:  exec(compile(open("/Users/CAL/Desktop/generate_build.py").read(), "/Users/CAL/Desktop/generate_build.py", 'exec'))
   Where "/Users/CAL/Desktop/generate_build.py" is the path to the generate_build.py file

4) Do not use blender whilst the code executes - upon build the console will show the time taken to produce the 3D model

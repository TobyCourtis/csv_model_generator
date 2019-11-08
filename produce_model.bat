ECHO Running blender file

mkdir test_boi
PowerShell -Command "& {cd 'C:\Program Files\Blender Foundation\Blender\'; ./blender C:\Users\CAL\Documents\first_test.blend --python C:\Users\CAL\Documents\TC\repos\csv_model_generator\generate_build.py -- 'Four Full Layers (03_10_2019)' 1}"
ECHO Ended
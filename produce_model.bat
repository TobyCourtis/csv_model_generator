ECHO Running blender file
set /p file_name=Please input the file name here:
set /p track_version=Input the track version here:
PowerShell -Command "& {cd 'C:\Program Files\Blender Foundation\Blender\'; ./blender C:\Users\CAL\Documents\first_test.blend --python C:\Users\CAL\Documents\TC\repos\csv_model_generator\generate_build.py -- '%file_name%' %track_version%}"
ECHO Ended
# VTR Formants Python

A small collection of Python code to enable working with the files from the [UCLA VTR Formants database](http://www.seas.ucla.edu/spapl/VTRFormants.html)

## Description of files 

* `read_fb`: reads the .fb files (binary files containing the formant and bandwidth measurements). This is an (almost) direct port from the MATLAB snippet provided in the VTR database readme. The time offsets added are guesses (the original readme specifies that each frame is 10ms so the offset seconds provided is the midpoint of that window).


# demo-dicom-circle-finder
A small demo program designed to be packaged and distributed as a Python wheel.

Taking the form of a small CLI utility which could be easily incorporated into a data processing pipeline, the program takes a DICOM file, which is an image that represents a single "slice" of an MRI scan, and outputs a csv with columns representing the X position, the Y position, and the radius of any circles detected in the image.

The program is intended to demonstrate good coding design and practices, packaging and distribution methods (wheels), environmental specification and consistency, and logically incorporating a variety of modules to process data and achieve a technical end.

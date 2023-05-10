# demo-dicom-circle-finder
A small demo program designed to be packaged and distributed as a Python wheel (and therefore via pip).

Taking the form of a small CLI utility which could be easily incorporated into a data processing pipeline, the program takes a DICOM file, which represents a single "slice" of an MRI scan, and outputs a csv with columns representing the X position, the Y position, and the radius of any circles detected in the file.

The program is intended to demonstrate good coding design and practices, packaging and distribution methods (wheels), environmental specification and consistency, and logically incorporating a variety of modules to process data and achieve a technical end.
Additionally, the repository management on GitHub is intended to show good working practices, proper Git flow, and the incorpoartion of elementary CI/CD processes and practices (in this case, the incorporation of PyLint as a GitHub workflow).

From the repository root dir -
  * To set up an environment, first create a venv, e.g.:

  ```
  python -m venv .venv && source .venv/bin/activate
  ```
  * Run the tests and Make initialiser:
  ```
  make Makefile test init
  ```
  * Install development package:
  ```
  pip install -e .
  ```
  * Build package which, making an installable wheel available under _dist_:
  ```
  python -m build
  ```
  * command runs with:
  ```
  dicom-circle-finder [filename] -o [output_csv_name]
  ```

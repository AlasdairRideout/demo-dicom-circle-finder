"""
Create context for the tests to run correctly
by allowing the clean importation of the package modules
"""


import os
import sys

# magical incantation
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# has to be imported _after_ the functional code
import dicom_circle_finder.dicom_processing_utils # pylint: disable=unused-import, wrong-import-position

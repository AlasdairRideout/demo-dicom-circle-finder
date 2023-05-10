"""
Utilities for processing DICOM files
"""

import os
import tempfile

import cv2 as cv
from matplotlib import pyplot
import numpy
import pydicom


def find_circles_in_image(filename):
    """
    Uses the Hough Circle Transform to find circles in a given image
    """
    source_image = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)
    grayscale_image = cv.cvtColor(source_image, cv.COLOR_BGR2GRAY)
    grayscale_image = cv.medianBlur(grayscale_image, 5)
    rows = grayscale_image.shape[0]
    circles = cv.HoughCircles(
        grayscale_image,
        cv.HOUGH_GRADIENT,
        1,
        rows/16,
        param1=100,
        param2=30,
        minRadius=1,
        maxRadius=30,
    )
    return circles[0]


class DICOMHandler():
    """
    Loads and encapsulates a DICOM file and provides methods to process it and yield data
    """
    def __init__(self, filename):
        """
        Initialise and use pydicom to read a DICOM file
        """
        self.dataset = pydicom.dcmread(filename)
        self._circles = None

    @property
    def circles(self):
        """
        Property to access the circles data in the DICOM
        """
        if not self._circles:
            self.find_circles_in_dicom()
        return self._circles

    def _export_dataset_as_png(self, filename):
        """
        Private function to convert DICOM data to a format useable by OpenCV
        """
        if self.dataset.pixel_array.any():
            # convert array to matplot image amd save as png
            pyplot.imshow(self.dataset.pixel_array, cmap=pyplot.cm.bone)
            pyplot.axis('off')
            pyplot.savefig(filename, format='png', bbox_inches='tight', pad_inches=0)

    def find_circles_in_dicom(self):
        """
        Creates a temporary directory and file for the image file and then 
        finds the circles in the image, storing it on the object's property
        """
        with tempfile.TemporaryDirectory() as tmp:
            filename = os.path.join(tmp, "DICOM_temp.png")
            self._export_dataset_as_png(filename)
            self._circles = find_circles_in_image(filename)

    def output_circles_to_csv(self, filename):
        """
        I/O function to write the data to a csv file
        """
        numpy.savetxt(filename, self.circles, delimiter=',')

"""
Tests for the file dicom_processing_utils.py

A production version of this code would have a comprehensive testing suite
"""


import pathlib

from context import dicom_circle_finder

import numpy


class TestFindCirclesInImage():
    """
    Class to hold tests for the function find_circles_in_image
    """
    def test_correctness(self):
        """
        Validate that the ouput from the test image is as expected
        """
        test_image = pathlib.Path(__file__).parent / "sample_image_of_dicom_data.png"
        test_image = str(test_image)
        expected_result = numpy.array(
            [
                [219.5, 300.5,  24.3],
                [180.5, 245.5,  21.2],
                [247.5,  84.5,  24.6],
                [157.5,  72.5,  25.4],
                [ 74.5, 217.5,  24.1],
                [196.5, 129.5,  24.5],
                [131.5, 179.5,  24.3],
                [291.5, 245.5,  24.6],
                [ 85.5, 127.5,  24.3],
                [303.5, 155.5,  25.1],
                [244.5, 194.5,  23.5],
                [129.5, 287.5,  23.3],
                [248.5, 141.5,  10.5],
                [234.5, 247.5,  10.3],
                [175.5, 293.5,   9.6],
                [128.5, 232.5,   9.6],
                [ 82.5, 172.5,   9.6],
                [295.5, 201.5,   9.4],
                [203.5,  80.5,  10.6],
                [142.5, 126.5,   9.4],
            ],
            dtype=numpy.float32
        )
        dicom_function = dicom_circle_finder.dicom_processing_utils.find_circles_in_image
        test_result = dicom_function(test_image)
        assert numpy.array_equal(test_result, expected_result)

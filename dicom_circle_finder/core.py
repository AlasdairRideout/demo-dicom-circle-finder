"""
Core functions for the package
"""


import argparse

from dicom_circle_finder.dicom_processing_utils import DICOMHandler


def get_parser():
    """
    Generate our CLI argument parser
    """
    parser = argparse.ArgumentParser(description="Find circles in DICOM file.")
    parser.add_argument("filename", help="An input DICOM filename/path")
    parser.add_argument(
        "-o", "--output-file", dest="output_file", help="A desired output filename/path"
    )
    return parser


def main():
    """
    Primary program logic
    """
    parser = get_parser()
    args = parser.parse_args()
    dicom_handler = DICOMHandler(args.filename)
    if args.output_file:
        dicom_handler.output_circles_to_csv(args.output_file)
    else:
        print(dicom_handler.circles)

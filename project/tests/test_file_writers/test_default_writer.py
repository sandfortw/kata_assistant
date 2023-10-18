from project.file_writers.default_writer import DefaultWriter
import os
import pytest



@pytest.mark.vcr
def test_write_file():
    expected_file_path = os.path.join(os.getcwd(), "codewars_katas", "nesting_structure_comparison.py")
    writer = DefaultWriter(url='https://www.codewars.com/kata/520446778469526ec0000001/train/python')
    writer.write_file()
    assert os.path.exists(expected_file_path), f"File '{expected_file_path}' not found"
    os.remove(expected_file_path)

    #Expect file *.py to be in Desktop/codewars_katas
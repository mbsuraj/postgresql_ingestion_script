import pytest
from src.config import config

# Declare the test class
class TestConfig:
    # Fill in with the correct mandatory argument
    def test_filename_format(self):
        """
        The database format needs to be specified as .ini. otherwise an exception
        is expected to be thrown.
        """
        test_arguments = {
            'filename': 'src/database',
            'section': 'postgresql'
        }
        with pytest.raises(Exception) as exc_info:
            config(**test_arguments)
        expected_error_msg = "Section postgresql not found in the src/database file"
        assert exc_info.match(expected_error_msg)

    def test_section_parameter(self):
        test_arguments = {
            'section': 'postgres'
        }
        with pytest.raises(Exception) as exc_info:
            config(**test_arguments)
        expected_error_msg = "Section postgres not found in the src/database.ini file"
        assert exc_info.match(expected_error_msg)
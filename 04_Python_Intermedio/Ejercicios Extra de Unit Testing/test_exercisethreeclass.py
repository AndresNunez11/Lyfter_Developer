from unittest.mock import mock_open, patch
from exercisethreeclass import read_lines
import pytest


def test_false_file_read_lines_return():
    #Act
    text_lines = "Linea 1\nLinea 2\nLinea 3\n"
    false_file = mock_open(read_data=text_lines)
    true_result = [ "Linea 1\n", "Linea 2\n", "Linea 3\n" ]

    #Act
    with patch("builtins.open", false_file): 
        Result = read_lines("archivo.txt")

    #Assert
    assert Result ==  true_result

def test_not_false_file_read_lines_return():
    #Act
    with patch( "builtins.open", side_effect=FileNotFoundError ): 
        with pytest.raises(FileNotFoundError): 
            read_lines("archivo_inexistente.txt")



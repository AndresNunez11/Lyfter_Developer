from exercisetwoclass import divide
import pytest

def test_divide_number_return_result():
    # Arrange
    number1 = 10
    number2 = 5
    # Act
    Result = divide(number1, number2)
    # Assert
    assert Result == 5.0

def test_divide_number_return_result():
    # Arrange
    number1 = 10
    number2 = 0
    # Act
    with pytest.raises(ValueError):
        divide(number1, number2)
    
def test_divide_number_return_result():
    # Arrange
    number1 = "A"
    number2 = 5
    # Act
    with pytest.raises(TypeError):
            divide(number1, number2)



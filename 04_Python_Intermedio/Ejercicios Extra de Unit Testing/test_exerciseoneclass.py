from exerciseoneclass import sum, average, change_to_string

def test_sum_positive_numbers_return():
    #Arrange
    number1=5
    number2=6
    #Act
    Result = sum(number1, number2)
    #Assert
    assert Result == 11

def test_sum_negative_numbers_return():
    #Arrange
    number1=-5
    number2=-6
    #Act
    Result = sum(number1, number2)
    #Assert
    assert Result == -11

def test_sum_zero_numbers_return():
    #Arrange
    number1=0
    number2=1
    #Act
    Result = sum(number1,number2)
    #Assert
    assert Result == 1

def test_average_positive_numbers_return():
    #Arrange
    number1=5
    number2=6
    #Act
    Result = average(number1, number2)
    #Assert
    assert Result == 5.5

def test_average_negative_numbers_return():
    #Arrange
    number1=-5
    number2=-6
    #Act
    Result = average(number1, number2)
    #Assert
    assert Result == -5.5

def test_averge_zero_numbers_return():
    #Arrange
    number1=0
    number2=1
    #Act
    Result = average(number1,number2)
    #Assert
    assert Result == 0.5

def test_change_to_str_positive_numbers_return():
    #Arrange
    number1=5
    #Act
    Result = change_to_string(number1)
    #Assert
    assert Result == "5"

def test_change_to_str_numbers_return():
    #Arrange
    number1=-5
    #Act
    Result = change_to_string(number1)
    #Assert
    assert Result == "-5"

def test_change_to_str_numbers_return():
    #Arrange
    number1=0
    #Act
    Result = change_to_string(number1)
    #Assert
    assert Result == "0"
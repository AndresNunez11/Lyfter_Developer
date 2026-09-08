from EjerciciosFunciones5class import count_letter

def test_count_letter_Lower_and_Capital_count_letter_return():
    #Arrange
    input_word ="Hola Mundo"
    #Act
    Result = count_letter(input_word)
    #Assert
    assert Result == (2,7)

def test_count_letter_Capital_count_letter_return():
    #Arrange
    input_word ="PYTHON"
    #Act
    Result = count_letter(input_word)
    #Assert
    assert Result == (6,0)

def test_count_letter_Lower_count_letter_return():
    #Arrange
    input_word ="python"
    #Act
    Result = count_letter(input_word)
    #Assert
    assert Result == (0,6)


from EjerciciosFunciones7class import list_primary_numbers

def test_list_primary_numbers_big_List_return_primary_numbers():
    #Arrange
    input_list=[45, 12, 7, 63, 29, 18, 54, 2, 71, 36, 41, 90, 23, 15,
    68, 31, 50, 11, 77, 4, 59, 26, 83, 34, 19, 72, 47, 8,
    61, 55, 14, 37, 96, 43, 20, 67, 6, 25, 89, 30, 53, 16,
    79, 42, 9, 58, 3, 70, 35, 17, 84, 51, 28, 73, 10, 39,
    62, 5, 86, 21, 57, 32, 97, 44, 13, 69, 24, 81, 48, 33]
    primary_list=[7, 29, 2, 71, 41, 23, 31, 11, 59, 83,
    19, 47, 61, 37, 43, 67, 89, 53, 79, 3,
    17, 73, 5, 97, 13]
    #Act
    Result = list_primary_numbers(input_list)
    #Assert
    assert Result == primary_list

def test_list_primary_numbers_small_List_return_primary_numbers():
    #Arrange
    input_list=[1, 4, 6, 7, 13, 9, 67]
    primary_list=[7, 13, 67]
    #Act
    Result = list_primary_numbers(input_list)
    #Assert
    assert Result == primary_list

def test_list_primary_numbers_all_primary_numbers_List_return_primary_numbers():
    #Arrange
    input_list=[2, 3, 5, 7, 11]
    primary_list=[2, 3, 5, 7, 11]
    #Act
    Result = list_primary_numbers(input_list)
    #Assert
    assert Result == primary_list
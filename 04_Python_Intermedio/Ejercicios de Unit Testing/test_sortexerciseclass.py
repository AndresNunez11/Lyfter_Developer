from sortexerciseclass import bubble_sort, validated_bubble_sort
import pytest


# Cree los siguientes unit tests para el algoritmo bubble_sort:
# Funciona con una lista pequeña.
# Funciona con una lista grande (de más de 100 elementos.)
# Funciona con una lista vacía.
# No funciona con parámetros que no sean una lista.

def test_validate_bubble_sort_small_list_return_sort_list():
    #Arreange
    input_list = [5, 6, 7, 8, 2, 4, 1, 9, 3]
    sort_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #Act
    Result = validated_bubble_sort(input_list)
    #Assert
    assert Result == sort_list

def test_validate_bubble_sort_big_list_return_sort_list():
    #Arreange
    input_list = [57, 3, 89, 12, 101, 44, 76, 18, 95, 1, 68, 24, 110, 35, 59, 8, 72, 50, 99, 16, 41, 104, 
    27, 61, 5, 83, 37, 92, 14, 66, 29, 107, 48, 70, 10, 55, 87, 21, 102, 33, 64, 7, 97, 39, 80, 2, 53, 91, 
    25, 74, 109, 46, 60, 13, 85, 31, 100, 52, 19, 78, 6, 43, 105, 28, 69, 11, 94, 36, 58, 17, 82, 49, 106, 
    22, 63, 4, 88, 34, 73, 15, 56, 96, 26, 65, 9, 84, 38, 103, 20, 71, 45, 90, 30, 62, 108, 23, 79, 40, 54, 
    98, 32, 67, 86, 42, 75, 93, 47, 77, 51, 81]
    sort_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
    26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 
    52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 
    78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 
    103, 104, 105, 106, 107, 108, 109, 110]
    #Act
    Result = validated_bubble_sort(input_list)
    #Assert
    assert Result == sort_list


def test_validate_bubble_sort_empty_list_return_raise_error():
    #Arreange
    input_list= []
    #Act
    with pytest.raises(ValueError):
        validated_bubble_sort(input_list)

def test_validate_bubble_sort_data_error_list_return_raise_error():
    #Arreange
    input_list= [5,2,3,4,'A']
    #Act
    with pytest.raises(ValueError):
        validated_bubble_sort(input_list)
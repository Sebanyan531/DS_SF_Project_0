"""Игра угадай число"""

import numpy as np
from game_v2 import score_game
from game_v2 import random_predict

def game_core_v3(number: int = 1) -> int:
    """Угадываем число за 20 попыток или меньше

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    # количество попыток
    count = 0
    min_range = 1
    max_range = 200
    predict_number = (min_range+max_range)//2
       
    while predict_number!=number:
        if predict_number > number:
            max_range = predict_number
            predict_number = (min_range+max_range)//2
            count +=1
        elif predict_number < number:
            min_range = predict_number
            predict_number = (min_range+max_range)//2
            count +=1         
        else:
            break
    return count   
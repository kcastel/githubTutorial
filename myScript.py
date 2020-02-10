import numpy as np
import pandas as pd

<<<<<<< HEAD

def my_function(matrix1,matrix2):
    try:
        matrix1*matrix2
    except ValueError:
        print("matrices are not aligned")
        return None

my_matrix = np.identity(5)
my_second_matrix = np.random.random(size=(4,4))

print(my_function(my_matrix,my_second_matrix))

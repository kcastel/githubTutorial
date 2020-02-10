import numpy as np

my_matrix = np.identity(4)
my_second_matrix=np.random.random(size=(4,4))

def my_function(matrix1,matrix2):
    try:
        matrix1*matrix2
    except ValueError:
        print("matrices are not aligned")
        return None

print(my_function(my_matrix,my_second_matrix))
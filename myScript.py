import numpy as np

my_matrix = np.identity(4)
my_second_matrix=np.random.random(size=(4,5))

def my_function(matrix1,matrix2):
    return(matrix1*matrix2)
print(my_function(my_matrix,my_second_matrix))
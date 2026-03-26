# NumPy Speed Test

import time
import numpy as np

# Creating data with 1 million numbers
size = 1000000

# Using Python list
python_list = list(range(size))

start_time = time.time()
result_list = [x * 2 for x in python_list]
end_time = time.time()

print("Time taken using Python list:", end_time - start_time)

# Using NumPy array
numpy_array = np.arange(size)

start_time = time.time()
result_array = numpy_array * 2
end_time = time.time()

print("Time taken using NumPy array:", end_time - start_time)
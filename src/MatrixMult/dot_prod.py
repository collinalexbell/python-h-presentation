import time
import numpy as np
import random as rn
import dot_prod

def timer(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        result = func(*args, **kwargs)
        after = time.time()
        return after - before, result
    return wrapper
def generate(size, range_):
    arr = [[[rn.randrange(*range_) for _ in range(size)] for _ in range(size)] for _ in range(2)]
    return arr

@timer
def python_implementation(arr1, arr2):
    result = [[0 for _ in range(len(arr1))] for _ in range(len(arr2[0]))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr2[0])):
                result[i][j] += arr1[i][k] * arr2[k][j]
    return result

@timer
def numpy_implementation(arr1, arr2):
    return np.array(arr1).dot(arr2)

@timer
def c_implementation(arr1, arr2):
    return dot_prod.dot_product(arr1, arr2)

@timer
def c_optimized_implementation(arr1, arr2):
    return dot_prod.dot_product_optimized(arr1, arr2)

@timer
def c_optimized_parallel_implementation(arr1, arr2):
    return dot_prod.dot_product_optimized_parallel(arr1, arr2)

if __name__ == '__main__':
    data = generate(size=500, range_=(1, 100))
    numpy_time_taken, numpy_result = numpy_implementation(*data)
    #python_time_taken, python_result = python_implementation(*data)
    #c_time_taken, c_result = c_implementation(*data)
    c_optimized_time_taken, c_optimized_result = c_optimized_implementation(*data)
    c_optimized_parallel_time_taken, _ = c_optimized_parallel_implementation(*data)

    print(f"time taken with numpy: {numpy_time_taken} seconds")
    #print(f"time taken with python: {python_time_taken} seconds")
    #print(f"time taken with c: {c_time_taken} seconds")
    print(f"time taken with optimized c: {c_optimized_time_taken} seconds")
    print(f"time taken with optimized parallelized c: {c_optimized_parallel_time_taken} seconds")

#import matplotlib.pyplot as plt
#def writeStats(stats, f, data, size, implementation):
#    time_taken, _ = f(*data)
#    stats[implementation].append({'size': size, 'time_taken': time_taken})
#    return stats

#if __name__ == '__main__':
#    implementations = [f for f in globals().keys() if callable(globals()[f]) and '_' in f and f != 'python_implementation']
#    stats = {k: [] for k in implementations}

#    for i in range(100, 1500, 100):
#        data = generate(i, range_=(1, 100))
#        for implementation in implementations:
#            stats = writeStats(stats, globals()[implementation], data, i, implementation)

#    for implementation, stats_ in stats.items():
#        plt.plot([n['size'] for n in stats[implementation]], [n['time_taken'] for n in stats[implementation]], label=implementation)
#    plt.legend()
#    plt.xlabel('Matrix size')
#    plt.ylabel('Time taken')
#    plt.show()

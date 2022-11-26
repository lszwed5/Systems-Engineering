import array
import math

arr1 = array.array("d")
arr1.extend((2.2, 5.6, 4.3, 3.0, 0.5))


def normalize(arr):
    """Returns the versor for a given vector"""
    return [arr_i / math.sqrt(sum(v_i * w_i for v_i, w_i in zip(arr, arr))) for arr_i in arr]


print(normalize(arr1))
for ele in normalize(arr1): print("%.5f" %ele)

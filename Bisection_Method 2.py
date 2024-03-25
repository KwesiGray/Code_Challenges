# BISECTION METHOD IN NUMERICAL ANALYSIS.
import math
def bisection_method(func, lower_bound, upper_bound, threshold=1e-6):
    if upper_bound - lower_bound < threshold:
        root = (lower_bound + upper_bound) / 2
        print(f"Root is approximately {root}")
        return root
    
    mid = (lower_bound + upper_bound) / 2
    mid_val = eval(func.replace('x', str(mid)))
    
    if mid_val == 0:
        print(f"Root is {mid}")
        return mid
    
    if mid_val * eval(func.replace('x', str(lower_bound))) < 0:
        return bisection_method(func, lower_bound, mid, threshold)
    else:
        return bisection_method(func, mid, upper_bound, threshold)

root = bisection_method("x**3 - 0.165 * x**2 + 3.993 * 10**-4", 0, 0.11)
print("Final Root:", root)
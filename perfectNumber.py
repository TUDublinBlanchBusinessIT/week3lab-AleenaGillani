#AleenaGillani
#07/07/2024
#perfectNumber.py

                                
from divisors import divisors


def perfectNumber(x):
    result = False
    sum_of_divisors = sum(divisors(x))
    if sum_of_divisors == x:
        result = True
    return result

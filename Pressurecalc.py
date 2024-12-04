import math

def pressure_calc(h):
    if h <= 50000:
        return 0.699 * math.exp(-0.00009*h) * 1000
    else:
        return False
    

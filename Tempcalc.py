def temp_calc(h):
    if h <= 7000:
        return (-31 - 0.00098*h)+273.15
    elif h > 7000:
        return (-23.4 - 0.00222*h)+273.15
    else:
        return False

    
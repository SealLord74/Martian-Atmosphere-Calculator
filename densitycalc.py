from Pressurecalc import pressure_calc
from Tempcalc import temp_calc

def density_calc(h):

    temp = temp_calc(h)
    pressure = pressure_calc(h)

    if temp and pressure:
        return pressure / (192.1 * temp)
    else:
        return False

height = int(input('Enter your altitude in meters: '))
temperature = temp_calc(height)
pressure = pressure_calc(height)
density = density_calc(height)

if temperature:
    print (f'the air temperature is {temperature} kelvin')
    print (f'the air pressure is {pressure} pascals')
    print (f'the air density is {density} kg/m^3')
else:
    print ('the atmosphere is too thin at this point')

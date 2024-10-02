celsius_temps = [0, 10, 20, 30, 40, 50]



def temp_convert(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


new_temps=list(map(temp_convert,celsius_temps))
print(new_temps)
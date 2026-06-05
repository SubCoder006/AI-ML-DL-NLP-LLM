def convert_temp(temp,unit):
    if unit == 'C':
        print(temp*9/5 + 32,'F');
    elif unit == 'F':
        print((temp - 32)*5/9,'C');
    else:
        print("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
    
convert_temp(100,'C')
convert_temp(212,'F')
convert_temp(38,'C')
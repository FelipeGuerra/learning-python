def converter(original_unit, coefficient):
    return original_unit * coefficient

print(converter(10, 0.3048))

def c_to_f(c):
    f = c * 9/5 + 32
    if c < -273.15:
        return "pew"
    else:
        return f
        

print(c_to_f(-300))
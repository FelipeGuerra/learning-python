temperatures = [10, -20, -289, 100]
def c_to_f(c):
    if c < -273.15:
        return c_to_f( float(input("Please don't write any message in the text file when input is lower than -273.15.")))
    else:
        f = c* 9/5 + 32
        return f
for t in temperatures:
    print(c_to_f(t))
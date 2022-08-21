def convert(s):
    f = float(s)
    c = (f - 32) * 5/9
    return c

print("99 Fah to Cel: " + str(convert(99)))
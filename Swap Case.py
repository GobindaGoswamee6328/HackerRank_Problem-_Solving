
def swap_case(s):
    new_st = "";
    for c in s:
        if c.islower():
            new_st += c.upper()
        elif c.isupper():
            new_st += c.lower()
        else:
            new_st += c
    return new_st

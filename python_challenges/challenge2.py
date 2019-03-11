def swap_case(s):
    r = ''
    for i in s:
        i = i.upper() if i.islower() else i.lower()
        r+=i
    return(r)

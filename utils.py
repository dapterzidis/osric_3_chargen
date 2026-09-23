def is_integer(val):
    try:
        val=int(val)
    except:
        pass
    return isinstance(val, int)
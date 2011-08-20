

def first_of(*args):
    """
    Outputs the first variable passed that is not False
    """
    try:
        return (x for x in args if x).next()
    except StopIteration:
        return None
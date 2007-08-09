def strIsInt(str):
    """Test given string is an integer
    """
    try:
        num = int(str)
    except ValueError:
        return False
    return True

def initialize_float_array(rows, cols):
    """Allocates a lists of lists of the given dimension with type float
    """
    mat = []
    for x in range(rows):
        mat.append([0.0] * cols)
    return mat

def initialize_int_array(rows, cols):
    """Allocates a lists of lists of the given dimension with type int
    """
    mat = []
    for x in range(rows):
        mat.append([0] * cols)
    return mat
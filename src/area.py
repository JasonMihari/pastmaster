def calculate_area_square(length):
    if not isinstance(length, (int, float)):
        raise TypeError("length must be numeric")
    if length <= 0:
        raise TypeError("length must be positive")
    return length * length

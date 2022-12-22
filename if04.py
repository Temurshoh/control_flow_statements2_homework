def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    if a>b:
        n=a
    if b>a:
        n=b
    if a==b:
        n=0
    return n
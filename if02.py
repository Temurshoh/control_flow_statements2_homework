def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    min=a
    if a>b:
        min=b
    if b>c:
        min=c
    return min
print(main(2,3,4))
print(main(34,23,12))
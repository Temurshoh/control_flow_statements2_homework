def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    max=a
    if b>a:
        max=b
    if c>b:
        max=c
    return max
print(main(2,3,4))
print(main(9,18,3))
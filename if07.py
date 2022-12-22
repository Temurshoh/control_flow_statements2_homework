def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Use the elif statments.
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"
    Args:
        temp: Temperature in Celsius.
    Returns:
        str: return answer.
    """
    if temp<0:
        n="muzlatish"
    elif temp<=10:
        n="juda sovuq"
    elif temp<=20:
        n="sovuq"
    elif temp<=30:
        n="oddiy"
    elif temp<=40:
        n="issiq"
    elif temp>40:
        n="juda issiq"

    return n
print(main(14))
print(main(2))
def compare(num1, num2):
    num1_touse = int(num1)
    num2_touse = int(num2)

    if num1 > num2:
        return f"{num1} is greater than {num2_touse}"
    if num1 < num2:
        return f"{num1} is less than {num2_touse}"
    if num1 == num2:
        return f"{num1} is equal to {num2_touse}"